# from flask import Flask, request, render_template
# from PIL import Image
# import pytesseract
# import re
# import pandas as pd

# app = Flask(__name__)

# # Path to Tesseract-OCR executable (Update this path accordingly)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Function to extract expiry date
# def extract_expiry_date(content):
#     if pd.isna(content):
#         return None

#     # Convert content to string for processing
#     content = str(content)

#     # Define patterns for matching phrases and dates
#     patterns = [
#         r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}\d{2}\d{2})",  # ddmmyy (6 digits)
#         r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}/\d{2}/\d{2})",  # dd/mm/yy
#         r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}\s\w+\s\d{4})",  # dd NAME_OF_THE_MONTH yyyy
#         r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}\w+\d{4})",      # ddNAME_OF_THE_MONTHyyyy
#         r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{4}\s\w+\s\d{2})",  # yyyy NAME_OF_THE_MONTH dd
#         r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}/\d{4})"         # mm/yyyy
#     ]

#     # Loop through patterns to find a match
#     for pattern in patterns:
#         match = re.search(pattern, content, flags=re.IGNORECASE)
#         if match:
#             return match.group(2)  # Return the matched date (group 2 contains the date)

#     # Return None if no date is found
#     return None

# # Route for the home page
# @app.route('/')
# def upload_form():
#     return '''
#         <html>
#         <body>
#             <h1>Upload an Image to Extract Expiry Date</h1>
#             <form action="/upload" method="post" enctype="multipart/form-data">
#                 <input type="file" name="image">
#                 <input type="submit" value="Upload">
#             </form>
#         </body>
#         </html>
#     '''

# # Route to handle image upload and OCR
# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return "No file uploaded", 400
    
#     file = request.files['image']
#     if file.filename == '':
#         return "No file selected", 400

#     try:
#         # Open the uploaded image
#         img = Image.open(file)

#         # Extract text using pytesseract
#         extracted_text = pytesseract.image_to_string(img)

#         # Extract expiry date from the text
#         expiry_date = extract_expiry_date(extracted_text)

#         # Return the extracted date or a message if no date is found
#         if expiry_date:
#             return f"<h1>Expiry Date Found: {expiry_date}</h1>"
#         else:
#             return "<h1>No Expiry Date Found</h1>"

#     except Exception as e:
#         return f"Error: {str(e)}", 500

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, render_template_string
# from PIL import Image
# import pytesseract
# import re
# import pandas as pd

# app = Flask(__name__)

# # Path to Tesseract-OCR executable (Update this path accordingly)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Function to extract expiry date
# def extract_expiry_date(content):
#     if pd.isna(content):
#         return None

#     # Convert content to string for processing
#     content = str(content)

#     # Define patterns for matching phrases and dates
    # patterns = [
    #     r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}\d{2}\d{2})",  # ddmmyy (6 digits)
    #     r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}/\d{2}/\d{2})",  # dd/mm/yy
    #     r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}\s\w+\s\d{4})",  # dd NAME_OF_THE_MONTH yyyy
    #     r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}\w+\d{4})",      # ddNAME_OF_THE_MONTHyyyy
    #     r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{4}\s\w+\s\d{2})",  # yyyy NAME_OF_THE_MONTH dd
    #     r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}/\d{4})"         # mm/yyyy
    # ]

#     # Loop through patterns to find a match
#     for pattern in patterns:
#         match = re.search(pattern, content, flags=re.IGNORECASE)
#         if match:
#             return match.group(2)  # Return the matched date (group 2 contains the date)

#     # Return None if no date is found
#     return None

# # Route for the home page
# @app.route('/')
# def upload_form():
#     return '''
#         <html>
#         <body>
#             <h1>Upload an Image to Extract Text and Expiry Date</h1>
#             <form action="/upload" method="post" enctype="multipart/form-data">
#                 <input type="file" name="image">
#                 <input type="submit" value="Upload">
#             </form>
#         </body>
#         </html>
#     '''

# # Route to handle image upload and processing
# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return "No file uploaded", 400
    
#     file = request.files['image']
#     if file.filename == '':
#         return "No file selected", 400

#     try:
#         # Open the uploaded image
#         img = Image.open(file)

#         # Extract text using pytesseract
#         extracted_text = pytesseract.image_to_string(img)

#         # Extract expiry date from the text
#         expiry_date = extract_expiry_date(extracted_text)

#         # Render the result on the same page
#         html_template = f"""
#         <html>
#         <body>
#             <h1>OCR and Expiry Date Extraction Result</h1>
#             <h3>Uploaded Image Text:</h3>
#             <p>{extracted_text}</p>
#             <h3>Expiry Date Found:</h3>
#             <p>{expiry_date if expiry_date else "No Expiry Date Found"}</p>
#             <br>
#             <a href="/">Go Back</a>
#         </body>
#         </html>
#         """
#         return render_template_string(html_template)

#     except Exception as e:
#         return f"Error: {str(e)}", 500

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, render_template_string
from PIL import Image
import pytesseract
import re
from datetime import datetime
import pandas as pd
import os

# Set the correct Tesseract command path
pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"

# Set the correct tessdata directory path
tessdata_dir = "/app/.apt/usr/share/tesseract-ocr/5/tessdata"

# Function to extract expiry date
def extract_expiry_date(content):
    if pd.isna(content):
        return None

    # Convert content to string for processing
    content = str(content)

    # Define patterns for matching phrases and dates
    patterns = [
        r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}\d{2}\d{2})",  # ddmmyy (6 digits)
        r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}/\d{2}/\d{2})",  # dd/mm/yy
        r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}\s\w+\s\d{4})",  # dd NAME_OF_THE_MONTH yyyy
        r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}\w+\d{4})",      # ddNAME_OF_THE_MONTHyyyy
        r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{4}\s\w+\s\d{2})",  # yyyy NAME_OF_THE_MONTH dd
        r"(EXP\s|Exp\. Date\s|Exp\. Date\:\s|Exp\. Date \:\s|BEST BEFORE\s|USED BY\s)(\d{2}/\d{4})"         # mm/yyyy
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
        # Match and convert ddmmyy (6 digits) to dd/mm/yyyy
        if re.match(r"^\d{6}$", date_str):
            return datetime.strptime(date_str, "%d%m%y").strftime("%d/%m/%Y")

        # Match and convert d/mm/yy to dd/mm/yyyy
        if re.match(r"^\d{1}/\d{2}/\d{2}$", date_str):
            return datetime.strptime(date_str, "%d/%m/%y").strftime("%d/%m/%Y")

        # Match and convert dd/mm/yy to dd/mm/yyyy
        if re.match(r"^\d{2}/\d{2}/\d{2}$", date_str):
            return datetime.strptime(date_str, "%d/%m/%y").strftime("%d/%m/%Y")

        # Match and convert dd NAME_OF_THE_MONTH yyyy to dd/mm/yyyy
        if re.match(r"^\d{2}\s\w+\s\d{4}$", date_str):
            return datetime.strptime(date_str, "%d %b %Y").strftime("%d/%m/%Y")

        # Match and convert d NAME_OF_THE_MONTH yyyy to dd/mm/yyyy
        if re.match(r"^\d\s\w+\s\d{4}$", date_str):
            return datetime.strptime(date_str, "%d %b %Y").strftime("%d/%m/%Y")

        # Match and convert ddNAME_OF_THE_MONTHyyyy to dd/mm/yyyy
        if re.match(r"^\d{2}\w{3}\d{4}$", date_str):
            return datetime.strptime(date_str, "%d%b%Y").strftime("%d/%m/%Y")

        # Match and convert yyyy NAME_OF_THE_MONTH dd to dd/mm/yyyy
        if re.match(r"^\d{4}\s\w+\s\d{2}$", date_str):
            return datetime.strptime(date_str, "%Y %b %d").strftime("%d/%m/%Y")

        # Match and convert mm/yyyy to mm/yyyy (no change needed)
        if re.match(r"^\d{2}/\d{4}$", date_str):
            return date_str  # Already in the correct format

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

        # Extract expiry date from the text
        expiry_date = extract_expiry_date(extracted_text)

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
    app.run()
