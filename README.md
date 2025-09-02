# text-to-speech-using-gtts-and-python

<link href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css" rel="stylesheet"></link>

<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet"></link>

<h1>🎤 Text-to-Speech Converter using gTTS in Python</h1>

  <!-- WhatsApp Channel Promo (Theme-Compatible) -->
<ul style="list-style: none; padding-left: 0; margin-top: 10px; margin-bottom: 20px; font-family: Arial, sans-serif;">
  <li style="margin: 8px 0; font-size: 18px;">
    <i class="fab fa-whatsapp" style="margin-right: 10px;"></i>
    <a href="https://whatsapp.com/channel/0029Vb5oq3gBA1f23Latsb3a" target="_blank" style="text-decoration: none;">
      📢 Stay updated with tutorials, projects & coding hacks — <strong>Join our WhatsApp Channel</strong>
    </a>
  </li>
</ul>

<p>
Have you ever wanted to make your computer <strong>speak out loud</strong> using your own Python code? With <strong>gTTS (Google Text-to-Speech)</strong>, you can easily convert any text into an audio file. This is super useful for building <i>voice assistants</i>, making <i>audio notes</i>, or even creating your own AI chatbot's voice.
</p>

<hr />

<h2>🔧 What is gTTS?</h2>
<p>
gTTS stands for <strong>Google Text-to-Speech</strong>. It is a Python library and CLI tool to extract the spoken text from Google Translate. It's super simple and effective for making basic TTS (Text-to-Speech) programs.
</p>

<hr />

<h2>✅ How It Works</h2>
<ul>
  <li><i class="fa-solid fa-code"></i> You type a text.</li>
  <li><i class="fa-solid fa-cloud-arrow-down"></i> The text is sent to Google's TTS API.</li>
  <li><i class="fa-solid fa-file-audio"></i> It returns an MP3 audio file.</li>
  <li><i class="fa-solid fa-volume-high"></i> You can play the file using any media player.</li>
</ul>

<hr />

<h2>💡 Installation</h2>
<p>First, install the library using pip:</p>

<pre><code class="language-bash">pip install gTTS</code></pre>

<hr />

<h2>👶 Basic Example Code</h2>

<pre><code class="language-python">
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
</code></pre>
<hr />
<pre><code class="language-python">🗂️ Commonly gTTS supported languages 
af: Afrikaans
ar: Arabic
bn: Bengali
en: English
fr: French
de: German
gu: Gujarati
hi: Hindi
it: Italian
ja: Japanese
kn: Kannada
ml: Malayalam
mr: Marathi
ne: Nepali
pa: Punjabi
ta: Tamil
te: Telugu
ur: Urdu
zh-CN: Chinese (Mandarin/China)
</code></pre>


<h2>🐢 What does slow=False mean?</h2>
<h3>The slow parameter controls speech speed:</h3>
<pre><code class="language-python">
slow=False: ✅ Normal speed (default, ideal for general use)
slow=True: 🐢 Slower speed, useful for language learners or clarity
</code></pre>

<hr />


<h2>🧠 Advanced Version with Input</h2>
<p>This version lets the user type custom text to convert:</p>

<pre><code class="language-python">
from gtts import gTTS
import os

text = input("Enter the text you want to convert to speech: ")
language = "en"

speech = gTTS(text=text, lang=language, slow=False)
filename = "custom_voice.mp3"
speech.save(filename)

# Play the file (Windows)
os.system(f"start {filename}")
</code></pre>

<hr />

<h2>⚙️ Tips, Tricks, and Hacks</h2>
<ul>
  <li>🎧 Use different languages by changing <code>lang</code> like <code>'hi'</code> for Hindi, <code>'fr'</code> for French, etc.</li>
  <li>🗂️ Combine gTTS with <code>pyttsx3</code> to create offline and online versions.</li>
  <li>🎛️ Adjust speed using <code>slow=True</code> if you want a slow voice (good for teaching tools).</li>
  <li>🧪 Combine with <code>speech_recognition</code> to create a full voice assistant!</li>
</ul>

<hr />

<h2>📱 Use on Different Devices</h2>

<h3>💻 Windows</h3>
<pre><code class="language-python">
os.system("start output.mp3")  # plays using default player
</code></pre>

<h3>🐧 Linux</h3>
<pre><code class="language-python">
os.system("mpg321 output.mp3")
</code></pre>

<h3>🍏 MacOS</h3>
<pre><code class="language-python">
os.system("afplay output.mp3")
</code></pre>


<hr />


<h2>🚀 Final Thoughts</h2>
<p>
gTTS is one of the easiest ways to add voice to your Python projects. From making talking robots to automating announcements or creating fun tools, the possibilities are endless.
</p>

<p>
Want to go even deeper? Try combining gTTS with:
</p><ul>
  <li>Flask – to make a voice bot website</li>
  <li>Telegram Bot – to make a speaking chatbot</li>
  <li>Audio Editor – use <code>pydub</code> for trimming/combining audio</li>
</ul>
<p></p>

<p><i class="fa-solid fa-thumbs-up"></i> Hope this guide helped you! Share your voice bot in the comments!</p>
