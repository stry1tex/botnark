# -*- coding: utf8 -*-
import telebot
import config
import random
from telebot import types
from requests import get
from config import TOKEN
import sqlite3
import time




bot = telebot.TeleBot(TOKEN)



# КНОПКИ ПРИ /START ---------------------------------------------------------------------------
def main():
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	buy = types.KeyboardButton('🏡 Города')
	profile = types.KeyboardButton('🤖 Профиль')
	otzivi = types.KeyboardButton('🗒 Отзывы')
	contact = types.KeyboardButton('💬 Обратная связь')
	rules = types.KeyboardButton('📖 Правила')
	markup.add(buy, profile, otzivi, contact, rules)
	return markup




# ПРИВЕТСТВЕННОЕ СООБЩЕНИЕ ---------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Вас приветствует магазин <b>Bender Shop</b>\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n❗️ <b>Обратите внимание:</b>\n\n<b>Наш магазин не имеет в поиске:</b>\n- Активных зеркал и копий\n- Наш магазин не имеет шопа на гидре\n\n<b>Остерегайтесь мошенников</b> и проверяйте введенный Вами адрес! (@b3ndershopbot)\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n❗️ Переход на наш канал, обращение к модераторам осуществляется <b>ТОЛЬКО</b> через бота.\n\n<b>Удачных покупок и приятного отдыха!</b>', reply_markup=main(), parse_mode='html')
# ОТВЕТЫ + привязка кнопок к ответу-------------------------------------------------------------
@bot.message_handler(content_types=['text'])
def otveti(message):
	chat_id = message.chat.id

	if message.text == '🏡 Города':
		markup = types.InlineKeyboardMarkup()
		msc = types.InlineKeyboardButton("🌆 Серпухов", callback_data = 'serpuhov')
		spb = types.InlineKeyboardButton("🌃 Подольск", callback_data = 'podolsk')
		moscow = types.InlineKeyboardButton('🌅 Москва', callback_data = 'moskva1')
		dmitrov = types.InlineKeyboardButton('🌌 Дмитров', callback_data = 'dmitrov')
		markup.add(msc, spb, moscow, dmitrov)

		bot.send_message(message.chat.id, '❕ Выберите подходящий город:', reply_markup=markup)
	elif message.text == '💬 Обратная связь':
		bot.send_message(message.chat.id, '✅ Наш оператор (24/7) - @benderoperator\n\nПисать по делу!')

	elif message.text == '🗒 Отзывы':
		bot.send_message(message.chat.id, 'Наши отзывы https://t.me/joinchat/T8KnSpBFPJc3GeJh')

	elif message.text == "🤖 Профиль":
		markup = types.InlineKeyboardMarkup()
		balancebuy = types.InlineKeyboardButton('Пополнить баланс', callback_data = 'balancebuy1')
		markup.add(balancebuy)
		bot.send_message(message.chat.id, '💸 Ваш личный кабинет\n➖➖➖➖➖➖➖➖➖➖➖➖\nБаланс: <b>0</b>\nВсего покупок: <b>0</b>\nПриглашённых пользователей: <b>0</b>', reply_markup=markup, parse_mode = 'html')

	
	elif message.text == '📖 Правила':
		bot.send_message(message.chat.id, '📚 Правила оформления покупок:\n\n➕ Перевод средств осуществляется СТРОГО по указанным реквизитам.\n\n➕ Сумма платежа должна быть равна сумме пополнения. Не больше и не меньше!\n\n➕ Если возникли трудности на стадии заказа, и Вы вынужденно обратились в поддержку - ОБЯЗАТЕЛЬНО предоставляйте фото, либо скриншот платежа.\n\nСообщения по типу:\n- Бро, посмотри, там же все видно.\n- Бро, аппарат не дал чек.\n- Бро, я не знал, что там комиссия.\n- Бро, мы на 300р больше положили за сервис.\n⚠️ Категорически игнорируются!\n\n📚 Правила общения с оператором:\n\n➕ Общайтесь вежливо, по ту сторону сидит такой же живой человек, как и Вы.\n\n➕ Старайтесь формулировать обращение к оператору емко и лаконично, в одно сообщение.\n\n➕ Обращаться в поддержку только по существу!\n\n➕ Поддержка не ведёт продаж и не занимается привлечением клиентов! (Только решение споров).\n\n➕ Формулировать обращение к оператору необходимо в течении 24 часов с момента оформления сделки.\n\nСообщения по типу:\n- Бро, как проверить что ты не фейк.\n- Бро, дай пробу, я всех своих подтяну.\n- Бро, 100р не хватает, дай скидку.\n\n⚠️ Категорически игнорируются!')



# ИНЛАЙН КЛАВИАТУРА, ГОРОДА / ТОВАР
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
		if call.message:
			if call.data == 'serpuhov':
				markup = types.InlineKeyboardMarkup()
				mef = types.InlineKeyboardButton("Меф 1гр", callback_data = 'mef')
				sk = types.InlineKeyboardButton("Альфа 0,5гр", callback_data = 'sk')
				sp = types.InlineKeyboardButton("Ромашка 1гр", callback_data = 'sp')
				hassh = types.InlineKeyboardButton("Изолятор 0,5гр", callback_data = 'hash')
				skblue = types.InlineKeyboardButton("Альфа синяя 0,3гр", callback_data = 'skblue')
				markup.add(mef, sk, sp, hassh, skblue)

				bot.send_message(call.message.chat.id, '❕ Выберите подходящий товар:', reply_markup=markup)

			elif call.data == 'podolsk':
				markup = types.InlineKeyboardMarkup()
				mefspb = types.InlineKeyboardButton("Меф 0,5гр", callback_data = 'mefspb')
				skspb = types.InlineKeyboardButton("Альфа 0,3гр", callback_data = 'skspb')
				spspb = types.InlineKeyboardButton("Ромашка 3гр", callback_data = 'spspb')
				hasshspb = types.InlineKeyboardButton("Белая вдова 1гр", callback_data = 'hashspb')
				skredspb = types.InlineKeyboardButton("Альфа red 2гр", callback_data = 'skredspb')
				extasy = types.InlineKeyboardButton("Экстази 2шт", callback_data = 'extasy')

				markup.add(mefspb, skspb, spspb, hasshspb, skredspb, extasy)

				bot.send_message(call.message.chat.id, '❕ Выберите подходящий товар:', reply_markup=markup)

			elif call.data == 'moskva1':
				markup = types.InlineKeyboardMarkup()
				mef = types.InlineKeyboardButton("Меф 3гр", callback_data = 'mefmoscow')
				sk = types.InlineKeyboardButton("Альфа мука 2гр", callback_data = 'skmoscow')
				sp = types.InlineKeyboardButton("Ромашка 5гр", callback_data = 'spmoscow')
				hassh = types.InlineKeyboardButton("Euro гаш 0,5гр", callback_data = 'hashmoscow')
				skblue = types.InlineKeyboardButton("Альфа крисы 0,3гр", callback_data = 'skbluemoscow')
				markup.add(mef, sk, sp, hassh, skblue)

				bot.send_message(call.message.chat.id, '❕ Выберите подходящий товар:', reply_markup=markup)	

			elif call.data == 'dmitrov':
				markup = types.InlineKeyboardMarkup()
				xtcdmitrov = types.InlineKeyboardButton("Экстази 2шт", callback_data = 'xtsdmitrov')
				skdmitrov = types.InlineKeyboardButton("Альфа крис 1гр", callback_data = 'alphadmitrov')
				spdmitrov = types.InlineKeyboardButton("Ромашка 2гр", callback_data = 'spicedmitrov')
				skbluedmitrov = types.InlineKeyboardButton("Альфа крисы 0,3гр", callback_data = 'skbluedmitrov')
				markup.add(xtcdmitrov, skdmitrov, skbluedmitrov, spdmitrov)

				bot.send_message(call.message.chat.id, '❕ Выберите подходящий товар:', reply_markup=markup)					






#ДМИТРОВ
			elif call.data == 'xtsdmitrov':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '💊 <b>Вы выбрали:</b> Экстази 2 штуки\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1700\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
			
			elif call.data == 'alphadmitrov':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '💎 <b>Вы выбрали:</b> Альфа кристаллы 1 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1500\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
			
			elif call.data == 'spicedmitrov':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '🌿 <b>Вы выбрали:</b> Ромашка 2 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1750\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
			
			elif call.data == 'skbluedmitrov':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '💎 <b>Вы выбрали:</b> Альфа крисы 0,3 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1150\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
			

#МОСКВА
			elif call.data == 'mefmoscow':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '💎 <b>Вы выбрали:</b> Мефедрон 3 грамма\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 3400\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
			
			elif call.data == 'skmoscow':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '💎 <b>Вы выбрали:</b> Альфа мука 2 грамма\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1999\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
			
			elif call.data == 'spmoscow':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '🌿 <b>Вы выбрали:</b> Ромашка 5 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 3000\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
			
			elif call.data == 'hashmoscow':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '🍫 <b>Вы выбрали:</b> Гашиш "Euro" 0,5 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1400\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
			
			elif call.data == 'skbluemoscow':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '💎 <b>Вы выбрали:</b> Альфа крисы white 0,3 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1100\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')

# СЕРПУХОВ / ПоДОЛЬСК =  ТОВАРЫ, ДА/НЕТ
			elif call.data == 'mef':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '💎 <b>Вы выбрали:</b> Мефедрон 1 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1550\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
			
			elif call.data == 'sk':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '💎 <b>Вы выбрали:</b> Альфа 0,5 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1450\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
			
			elif call.data == 'sp':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '🌿 <b>Вы выбрали:</b> Ромашка 1 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1400\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
			
			elif call.data == 'hash':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '🍫 <b>Вы выбрали:</b> Гашиш изолятор 0,5 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1350\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
			
			elif call.data == 'skblue':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '💎 <b>Вы выбрали:</b> Альфа синий цвет 0,3 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1100\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
			#СПБ ТОВАРЫ
			elif call.data == 'mefspb':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '💎 <b>Вы выбрали:</b> Мефедрон 0,5 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1250\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
				
			elif call.data == 'skspb':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '💎 <b>Вы выбрали:</b> Альфа 0,3 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1150\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
				
			elif call.data == 'spspb':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '🌿 <b>Вы выбрали:</b> Ромашка 3 грамма\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 2100\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
				
			elif call.data == 'hashspb':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '🍀 <b>Вы выбрали:</b> Бошки "Белая вдова" 1 грамм\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1550\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
				
			elif call.data == 'skredspb':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '💎 <b>Вы выбрали:</b> Альфа красного цвета 2 грамма\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1950\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
				
			elif call.data == 'extasy':
				markup = types.InlineKeyboardMarkup()
				yes = types.InlineKeyboardButton("✅ Да", callback_data = 'da')
				no = types.InlineKeyboardButton("❌ Нет", callback_data = 'net')
				markup.add(yes, no)

				bot.send_message(call.message.chat.id, '💊 <b>Вы выбрали:</b> Экстази "Bentley" 260MG / 2 штуки\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💵 <b>Стоимость:</b> 1600\n\n🧲 <b>Тип клада:</b> Магнит\n\n♻️ <b>Вы уверены в своём выборе?</b>', reply_markup=markup, parse_mode='html')
				
			elif call.data == 'da':
				bot.send_message(call.message.chat.id, '❗️ На вашем балансе недостаточно средств\n❗️ Пополнить баланс можно в профиле.')

			elif call.data == 'net':
				bot.send_message(call.message.chat.id, '❗️ В таком случае вы можете выбрать другой товар, или перейти в основное меню - /start')

			elif call.data == 'balancebuy1':
				markup = types.InlineKeyboardMarkup()
				qiwi = types.InlineKeyboardButton('🥝 QIWI', callback_data = 'qiwi1')
				btc = types.InlineKeyboardButton('〽️ BTC', callback_data = 'btc1')
				markup.add(qiwi, btc)

				bot.send_message(call.message.chat.id, '❕ Выберите способ оплаты:', reply_markup=markup)

			elif call.data == 'qiwi1':
				markup = types.InlineKeyboardMarkup()
				popolnil = types.InlineKeyboardButton('✅ Я ввёл', callback_data = 'popolnil1')
				markup.add(popolnil)

				bot.send_message(call.message.chat.id, '❗️ Введите нужную сумму пополнения, после чего нажмите на кнопку снизу:', reply_markup=markup)

			elif call.data == 'popolnil1':
				markup = types.InlineKeyboardMarkup()
				profit = types.InlineKeyboardButton('Проверить оплату', callback_data = 'profit1')
				markup.add(profit)

				bot.send_message(call.message.chat.id, '💳 QIWI Кошелёк: <b>79851647182</b>\n💬 Комментарий: <b>1438288FJa{qfAshmao80912</b>\n\n🔺 ВНИМАНИЕ! Перевод без комментария будет <b>АНУЛИРОВАН</b>, деньги пойдут магазину в карман.\n\n🔺 Также переводить нужно <b>РОВНО</b> столько, сколько указали в пополнении (т.е указали 1500 рублей, переводите <b>РОВНО</b> 1500 рублей)', reply_markup=markup, parse_mode='html')


			elif call.data == 'profit1':
				bot.send_message(call.message.chat.id, '❌ Платёж не был найден')


			elif call.data == 'btc1':
				markup = types.InlineKeyboardMarkup()
				yavvel = types.InlineKeyboardButton('✅ Я ввёл', callback_data = 'yavvel')
				markup.add(yavvel)
				bot.send_message(call.message.chat.id, '❗️ Введите нужную сумму пополнения (в биткоинах), после чего нажмите на кнопку снизу:', reply_markup=markup)

			elif call.data == 'yavvel':
				markup = types.InlineKeyboardMarkup()
				profit2 = types.InlineKeyboardButton('Проверить оплату', callback_data = 'profit3')
				markup.add(profit2)
				bot.send_message(call.message.chat.id, '💳 BTC Кошелёк: <b>1F5YD6XdD2aYAygT1spcgj3omFQPgXh3Lo</b>\n\n🔺 ВНИМАНИЕ! Переводить нужно <b>РОВНО</b> столько, сколько указали в пополнении (т.е указали 0,00020 BTC, переводите <b>РОВНО</b> 0,00020 BTC, иначе бот не засчитает перевод)', reply_markup=markup, parse_mode='html')


			elif call.data == 'profit3':
				bot.send_message(call.message.chat.id, '❌ Платёж не был найден!')

			else:
				bot.send_message(message.chat.id, 'Я тебя не понимаю, нажми на одну из кнопок!')



		




		
bot.polling()