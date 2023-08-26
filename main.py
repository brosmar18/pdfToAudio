from gtts import gTTS
import os 
import PyPDF2

# Open the PDF file
pdf_file = open('resume2023.pdf', 'rb')

# PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

