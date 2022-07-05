# pip install python-telegram-bot --upgrade
from telegram import *
from telegram.ext import *
from requests import *


updater = Updater(token='TOKEN')
_dispatcher = updater.dispatcher

# o parâmetro update contém a mensagem que o usuário enviou e quem enviou
# o parametro context é usado para enviar as mensagens
pessoa_aleatoria = "Pessoa aleatória"
imagem_aleatoria = "Foto aleatória"

url_imagem_aleatoria = "https://picsum.photos/1200"
url_pessoa_aleatoria = "https://thispersondoesnotexist.com/image"


def startCommand(update: Update, context: CallbackContext):
    # retorna quem enviou a mensagem
    # print(update.effective_chat.username)
    # retorna qual é a mensagem
    # print(update.message.text)
    # passando os botões que serão exibidos para o usuário
    buttons = [[KeyboardButton(imagem_aleatoria)], [
        KeyboardButton(pessoa_aleatoria)]]
    # mandando o bot criar o teclado com esses botões
    
    # update.effective_chat.id ===> pegando o CHAT ID da conversa
    context.bot.sendMessage(chat_id=update.effective_chat.id, text="bem vindo ao meu bot <3", reply_markup=ReplyKeyboardMarkup(
        buttons))  # reply_markup é uma marcação de teclado de resposta que recebe os botões


def messageHandler(update: Update, context: CallbackContext):
    # controlando o recebimento das mensagens
    # print(update.message.text)
    if pessoa_aleatoria in update.message.text:
        imagem = get(url_pessoa_aleatoria).content
    if imagem_aleatoria in update.message.text:
        imagem = get(url_imagem_aleatoria).content
    if imagem:
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[
                                   InputMediaPhoto(imagem, caption="imagem escolhida")])


# handler para o input do usuário
_dispatcher.add_handler(CommandHandler("start", startCommand))
_dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
# _dispatcher.add_error_handler()

# rodando
updater.start_polling()
