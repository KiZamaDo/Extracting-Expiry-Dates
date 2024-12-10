from flask import Flask, request, render_template_string
from PIL import Image
import pytesseract
import re
from datetime import datetime
import pandas as pd
import os

app = Flask(__name__)

# Set the correct Tesseract command path for Heroku
pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"

# Set the correct tessdata directory path for Heroku
tessdata_dir = "/app/.apt/usr/share/tesseract-ocr/5/tessdata"

# Function to extract expiry date
def extract_expiry_date(content):
    if pd.isna(content):
        return None

    # Convert content to string for processing
    content = str(content)

    # Remove extra spaces or newlines that could interfere with regex matching
    content = re.sub(r'\s+', ' ', content)

    # Define patterns for matching expiry date phrases and dates
    patterns = [
        r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}\s\w+\s\d{4})",  # dd MMM yyyy
        r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}/\d{2}/\d{4})",  # dd/mm/yyyy
        r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}\d{2}\d{4})",  # ddmmyyyy
        r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}\s\w+\s\d{2})",  # dd MMM yy
        r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}/\d{2}/\d{2})"   # dd/mm/yy
    ]

    # Loop through patterns to find a match
    for pattern in patterns:
        match = re.search(pattern, content, flags=re.IGNORECASE)
        if match:
            return match.group(2)  # Return the matched date (group 2 contains the date)

    return None  # Return None if no date is found

# Function to standardize dates
def convert_date(date_str):
    # Handle "NO" as "NOV" for November
    date_str = date_str.replace("NO", "NOV")

    try:
        # Match and convert dd NAME_OF_THE_MONTH yyyy to dd/mm/yyyy
        if re.match(r"^\d{2}\s\w+\s\d{4}$", date_str):
            return datetime.strptime(date_str, "%d %b %Y").strftime("%d/%m/%y")

        # Match and convert dd/mm/yyyy to dd/mm/yyyy (no change needed)
        if re.match(r"^\d{2}/\d{2}/\d{4}$", date_str):
            return datetime.strptime(date_str, "%d/%m/%Y").strftime("%d/%m/%y")

        # Match and convert ddmmyyyy to dd/mm/yyyy
        if re.match(r"^\d{8}$", date_str):
            return datetime.strptime(date_str, "%d%m%Y").strftime("%d/%m/%y")

        # Match and convert dd MMM yy to dd/mm/yy
        if re.match(r"^\d{2}\s\w{3}\s\d{2}$", date_str):
            return datetime.strptime(date_str, "%d %b %y").strftime("%d/%m/%y")

        # Match and convert dd/mm/yy to dd/mm/yy (no change needed)
        if re.match(r"^\d{2}/\d{2}/\d{2}$", date_str):
            return datetime.strptime(date_str, "%d/%m/%y").strftime("%d/%m/%y")

    except ValueError:
        return None  # Return None if date is invalid

    return None  # If no match, return None


# Route for the home page
@app.route('/')
def upload_form():
    return '''
        <html>
        <body>
            <h1>Upload an Image to Extract Text and Expiry Date</h1>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="image">
                <input type="submit" value="Upload">
            </form>
        </body>
        </html>
    '''


# Route to handle image upload and processing
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['image']
    if file.filename == '':
        return "No file selected", 400

    try:
        # Open the uploaded image
        img = Image.open(file)

        # Extract text using pytesseract (include tessdata dir)
        extracted_text = pytesseract.image_to_string(img, config=f'--tessdata-dir "{tessdata_dir}"')

        # Print the extracted text for debugging
        print("Extracted Text:", extracted_text)

        # Extract expiry date from the text
        expiry_date = extract_expiry_date(extracted_text)

        # Print the extracted expiry date for debugging
        print("Extracted Expiry Date:", expiry_date)

        # Standardize the expiry date
        standardized_date = convert_date(expiry_date) if expiry_date else None

        # Render the result in table format
        html_template = f"""
        <html>
        <body>
            <h1>OCR and Expiry Date Extraction Result</h1>
            <table border="1">
                <tr>
                    <th>Image Content</th>
                    <th>Expiry Date</th>
                    <th>Standardized Date</th>
                </tr>
                <tr>
                    <td>{extracted_text}</td>
                    <td>{expiry_date if expiry_date else "Not Found"}</td>
                    <td>{standardized_date if standardized_date else "Not Found"}</td>
                </tr>
            </table>
            <br>
            <a href="/">Go Back</a>
        </body>
        </html>
        """
        return render_template_string(html_template)

    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
