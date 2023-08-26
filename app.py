from flask import Flask, render_template, request, send_file, url_for, Response
import os
import PyPDF2
from gtts import gTTS

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
        audio_filename = "resume_audio.mp3"
        audio_file_path = os.path.join(app.static_folder, audio_filename)

        # Save the audio file
        tts.save(audio_file_path)

        return render_template("index.html", audio_filename=audio_filename)
    
    return render_template("index.html", audio_filename=None)


@app.route("/download_audio")
def download_audio():
    audio_filename = "resume_audio.mp3"
    audio_file_path = os.path.join(app.static_folder, audio_filename)

    user_filename = request.args.get('filename', 'audio')  # Get the filename parameter, default to 'audio'
    user_filename = user_filename.replace(' ', '_')  # Replace spaces with underscores
    user_filename += '.mp3'  # Add the .mp3 extension

    def generate():
        with open(audio_file_path, 'rb') as f:
            yield from f

    response = Response(generate(), content_type='audio/mpeg')
    response.headers['Content-Disposition'] = f'attachment; filename={user_filename}'
    return response



if __name__ == "__main__":
    app.run(debug=True)
