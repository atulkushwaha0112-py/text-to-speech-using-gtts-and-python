
from gtts import gTTS
import os

text = input("Enter the text you want to convert to speech: ")
language = "en"

speech = gTTS(text=text, lang=language, slow=False)
filename = "custom_voice.mp3"
speech.save(filename)

# Play the file (Windows)
os.system(f"start {filename}")
