from pdf2docx import Converter

pdf_path = "C:\\Users\\Kumari\\Desktop\\myproject\\output.pdf"
output_path = r"C:/Users/Kumari/Desktop/myproject/file.docx"

cv = Converter(pdf_path)
cv.convert(output_path, start=0, end=None)
cv.close()


# import fitz

# pdf_path = "C:\\Users\\Kumari\\Desktop\\myproject\\output.pdf"
# output_path = r"C:/Users/Kumari/Desktop/myproject/file.docs"

# pdf_document = fitz.open(pdf_path)
# page = pdf_document.load_page(0)


# text = page.get_text("text")

# try:
#     with open(output_path, "w", encoding="utf-8") as output_file:
#         output_file.write(text)
# except Exception as e:
#     print("Permission Is detained :", e)
