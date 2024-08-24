import telebot
from logik import Text2ImageAPI
import time
from config import TOKEN, API_KEY, SECRET_KEY

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def hendle_message(message):
    prompt = message.text

    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API_KEY, SECRET_KEY)
    model_id = api.get_model()
    uuid = api.generate(prompt, model_id)
    images = api.check_generation(uuid)[0]

    file_path = "generated_image.jpg"
    api.save_image(images, file_path)

    with open(file_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Подождите бот пишет ответ\
""")
    time.sleep(2)
    bot.reply_to(message, """\
привет напиши /help
""")

# Handle '/help'
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
Подождите бот пишет ответ\
""")
    time.sleep(2)
    bot.reply_to(message, """\
И так что же я могу тебе
предложить...минутку...Ах-точно
вспомнил я могу замазовать лица...
Просто пришли мне картинку на которой 
есть лицо челловека и я его замажу\
""")

bot.polling()