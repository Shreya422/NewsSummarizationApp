from gtts import gTTS
from googletrans import Translator
import os

def generate_hindi_speech(text, output_path="output.mp3"):
    """
    Translates English text to Hindi and converts it to speech.
    """
    translator = Translator()
    translated_text = translator.translate(text, src="en", dest="hi").text
    tts = gTTS(text=translated_text, lang="hi")
    tts.save(output_path)
    return output_path
