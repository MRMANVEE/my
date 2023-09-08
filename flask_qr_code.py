from flask import Flask 
from pdf2docx import Converter

app = Flask(__name__)
@app.route("/upload")
def upload_pdf():
     pdf_path = "C:\\Users\\Kumari\\Desktop\\myproject\\output.pdf"
     output_path = r"C:/Users/Kumari/Desktop/myproject/file.docx"

     cv = Converter(pdf_path)
     cv.convert(output_path, start=0, end=None)
     cv.close()
if __name__=="__main__":
     app.run(debug=True)