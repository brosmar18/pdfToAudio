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

        # Create a gTTS object
        tts = gTTS(text)

        # Specify the path and filename for the audio file
        audio_file_path = "/Users/brosmar18/Downloads/resume_audio.mp3"

        # Save the audio file
        tts.save(audio_file_path)

        return render_template("index.html", audio_file_path=audio_file_path)
    
    return render_template("index.html", audio_file_path=None)


if __name__ == "__main__":
    app.run(debug=True )