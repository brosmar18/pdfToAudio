from flask import Flask, render_template, request
from gtts import gTTS
import os
import PyPDF2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded PDF file
        pdf_file = request.files["pdf_file"]

        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Extract text from each page
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
