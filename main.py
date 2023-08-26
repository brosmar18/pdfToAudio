from gtts import gTTS
import os
import PyPDF2

# Open the PDF file
pdf_file = open('resume2023.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from each page
text = ''
for page in pdf_reader.pages:
    text += page.extract_text()

# Close the PDF file
pdf_file.close()

# Print the extracted text
print(text)

# create gTTS object
tts = gTTS(text)

# Save audio file
tts.save("resume_audio.mp3")

# Play audio using default audio player
os.system("resume.audio.mp3")
