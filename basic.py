
from gtts import gTTS
import os

text = "Hello! This is your computer speaking."
language = "en"

speech = gTTS(text=text, lang=language, slow=False)
speech.save("output.mp3")

# Play the file (Windows)
os.system("start output.mp3")

# For Linux or Mac
# os.system("mpg321 output.mp3")
