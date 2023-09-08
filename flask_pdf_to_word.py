from flask import Flask, request, render_template 
from pdf2docx import Converter
import os
from urllib.parse import quote

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
os.makedirs(UPLOAD_FOLDER,exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/upload", methods = ['GET', 'POST'])

def upload_pdf():
    if request.method == 'POST':
        pdf_file = request.files["pdf_file"]
        
        if pdf_file and pdf_file.filename.endswith(".pdf"):
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
            pdf_file.save(pdf_path)

            output_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename.replace('.pdf','.docx'))

            cv = Converter(pdf_path)
            cv.convert(output_path, start=0, end=None)
            cv.close()


            docx_filename = pdf_file.filename.replace('.pdf', '.docx')
            encoded_docx_filename = quote(docx_filename)

            return f"upload/{encoded_docx_filename}"


    return render_template("uploads.html")

if __name__=="__main__":
    app.run(debug=True)

