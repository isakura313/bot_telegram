import telebot
import random
token = '1396541073:AAFpXgEZMbBVdSyAkX0z91T0sHtOaAHoSrE'

bot = telebot.TeleBot(token)
bad_words = ["не пиши сюда больше", "кто тебя вообще пустил в этот чат?", "😥"]

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    chislo = random.randint(0, 1)
    if(message.text == "как дела?"):
        message.text = "нормально. Давай не будем об этом"
        bot.send_message(message.chat.id, message.text)
    if(message.text == "game"):
        bot.send_dice(message.chat.id)
    elif(chislo):
        message.text = random.choice(bad_words)
        bot.send_message(message.chat.id, message.text)


bot.infinity_polling()
