import telebot
from config import TOKEN
from logic_ai import get_class

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo']) # Бот будет реагировать когда ему отправят картинку
def send_class(message):
    
    file_info = bot.get_file(message.photo[-1].file_id) # получаем информацию о картинке

    file_name = file_info.file_path.split('/')[-1] # получаем имя картинки

    downloaded_file = bot.download_file(file_info.file_path) # скачиваем картинку

    with open(file_name, 'wb') as new_file: # создаем новый файл

        new_file.write(downloaded_file) # сохраняем в этот файл картинку 

    result = get_class(file_name)
    
    bot.reply_to(message, result)

bot.infinity_polling()