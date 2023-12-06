import speech_recognition as sr
from elevenlabs import generate, play, set_api_key
import os

set_api_key(os.environ['ELEVEN_API_KEY'])

class AudioInterface:
    def listen(self) -> str:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print('Say something!')
            audio = recognizer.listen(source)

        text = recognizer.recognize_whisper_api(
            audio,
            api_key=os.environ['OPENAI_API_KEY']
        )

        return text

    def speak(self, text):
        audio = generate(
            text=text,
            voice='Kevin',
            model='eleven_monolingual_v1'
        )
        play(audio)