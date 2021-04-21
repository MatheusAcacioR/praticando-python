import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("1410967289:AAFUxToMkE50zlnSRNSNgALwhSLm1FraEng")
bot = Chatbot("Melinda")

def ReceiveMessage(msg):
    frase = bot.escuta(msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)

    "Maneiras de capturar o chatID da conversa do telegram"
    # chatID = msg['chat']['id']
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    "Maneiras de capturar o chatID da conversa do telegram"

    telegram.sendMessage(chatID, resp)
telegram.message_loop(ReceiveMessage)

while True:
    pass
