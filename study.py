import datetime
import telebot
bot=telebot.TeleBot('5292414027:AAEKWvN6Ce7SniuB4vDvtnKksHwccOBGPZ8')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
@bot.message_handler()
def echo_all(message):
	if message.text.lower()	=="привет":
		bot.send_message(message.chat.id, "Тебе тоже", reply_markup=keypool)
	if message.text.lower()	=="сколько времени ?":
		now =datetime.datetime.now()
		bot.send_message(message.chat.id, str(now.strftime("%H:%M:%S")), reply_markup=keypool)
	if message.text.lower()	=="пока":
		bot.send_message(message.chat.id, "Удачи !", reply_markup=keypool)
		bot.stop_bot()
	if message.text.lower()	=="какой день недели ?":
		bot.send_message(message.chat.id, str(datetime.datetime.now().strftime("%A")), reply_markup=keypool)
keypool=telebot.types.ReplyKeyboardMarkup(True)
keypool.row("Привет", "Пока", "Сколько времени ?", "Какой день недели ?")
bot.polling()