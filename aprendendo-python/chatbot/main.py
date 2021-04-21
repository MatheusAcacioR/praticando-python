from Chatbot import Chatbot
import pyttsx
import speech_recognition as sr

en = pyttsx.init()
en.setProperty('voice', b'Brazil')
rec = sr.Recognizer()

class botFalante(Chatbot):
    def escuta(self, frase = None):
        try:
            with sr.Microphone() as mic:
                fala = rec.listen(mic)
            frase = rec.recognize_google(fala, language='pt')
            frase = frase.replace('aprendi', 'aprende')
            print(frase)
        except sr.UnknownValueError:
            print('Deu erro no reconhecimento')
            return ''
        return super().escuta(frase = frase)
    def fala(self, frase):
        en.say(frase)
        en.runAndWait()
        super().fala(frase)

Bot = botFalante("Felipe")

while True:
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)
    if resp == 'tchau':
        break