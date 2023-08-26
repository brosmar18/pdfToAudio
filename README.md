# PDF to Audio Converter

This repository contains a Python script that converts the text content of a PDF resume into an audio file using the gTTS (Google Text-to-Speech) library. This allows you to listen to your resume instead of reading it, which can be particularly helpful for accessibility or convenience.

## How It Works

The Python script in `main.py` performs the following steps:

1. **Open PDF File**: The script opens a PDF file named `resume2023.pdf` in binary mode.

2. **Extract Text**: It creates a PDF reader object using the `PyPDF2` library and iterates through each page of the PDF, extracting the text content.

3. **Create gTTS Object**: The extracted text is then used to create a gTTS (Google Text-to-Speech) object.

4. **Save Audio File**: The gTTS object is saved as an MP3 audio file named `resume_audio.mp3`.

5. **Play Audio**: The audio file is played using the system's default audio player.

## Usage

1. Ensure you have Python 3.x installed on your system.

2. Install required libraries:

`pip install gtts PyPDF2`


3. Place your PDF resume (`resume2023.pdf`) in the same directory as the script (`main.py`).

4. Run the script:

`python main.py`


5. After execution, an audio file named `resume_audio.mp3` will be generated. You can listen to this file to hear the content of your PDF resume.

## Notes

- The script uses the `PyPDF2` library to work with PDF files and the `gTTS` library for text-to-speech conversion.
- The generated audio file can be useful for accessibility purposes or for reviewing your resume on-the-go.
- Feel free to customize the script according to your preferences or add error handling as needed.

## Author

[Bryan Gonzalez](https://github.com/brosmar18)

If you find this project helpful, consider giving it a star and connecting with me!


