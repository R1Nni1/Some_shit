import datetime
import telebot
from pyowm import *
from pyowm.utils.config import get_default_config
bot=telebot.TeleBot('5292414027:AAEKWvN6Ce7SniuB4vDvtnKksHwccOBGPZ8')
keypool=telebot.types.ReplyKeyboardMarkup(True)
keypool.row("Привет")
keypool.row("Погода")
@bot.message_handler(command=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id,"Привет !",reply_markup=keypool)
language = get_default_config()
language['language'] = 'ru'
owm=OWM("3733bcd746dd112dc083e7c19c2ddcbc",language)
weather_is=False
@bot.message_handler()
def echo_all(message):
	global weather_is
	if message.text.lower()	=="привет":
		bot.send_message(message.chat.id, "Привет", reply_markup=keypool)
	if message.text.lower()=="погода":
		weather_is=True
		bot.send_message(message.chat.id, "Введите место, где вы хотите узнать погоду")
	if weather_is==True and message.text.lower()!="погода":
		try:
			weather_place=owm.weather_manager().weather_at_place(str(message.text)).weather
			toprint=""
			toprint+=f"Сейчас на улице : {weather_place.detailed_status} \nтемпература: {weather_place.temperature('celsius').get('temp')} градусов \nскорость ветра: {weather_place.wind().get('speed')} м/с \nоблачность: {weather_place.clouds}% \n"
			rainy = str(weather_place.rain)
			print(rainy)
			if rainy!="{}":
				toprint+=f"кол-во осадков: {rainy[5:len(rainy)-1]} мм."
			bot.send_message(message.chat.id, toprint,reply_markup=keypool)
		except:
			bot.send_message(message.chat.id, "Не вверный ввод", reply_markup=keypool)
		finally: weather_is=False
print("Started")
bot.infinity_polling()
