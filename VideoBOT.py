import telebot
from telebot import types
parts = ''
music = ''
data = ''
contact = ''

bot = telebot.TeleBot("1283650510:AAEn5xJg_QtMTgpdPtgANYkNLi7fwoCEsV8")

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Моё Портфолио', 'Цены на Услуги')
keyboard.row('Обо Мне', 'Заказать Монтаж')

def send(id, text):
    bot.send_message(id, text, reply_markup = keyboard)

@bot.message_handler(content_types = ['text'])
def main(message):
    id = message.chat.id
    msg = message.text

    if msg == '/start':
        send(id, 'Привет, меня зовут Андрей и я круто делаю монтаж! Пожалуйста выберите из меню ниже то, что Вы хотели бы узнать:')
    elif msg == 'Моё Портфолио':
        send(id, 'Примеры моих работ в группе: ✔https://vk.com/club194363569✔')
    elif msg == 'Цены на Услуги':
        send(id, 'ПРИМЕР РАССЧЁТА ЦЕНЫ:\r\n✔300 руб - просто соединить видео в одно с обычными плавными переходами.\r\n✔Ещё +50 руб - наложить фоновую музыку с затуханиями и возрастаниями в начале, конце и в перерывах (если видео состоит из нескольких глав и частей - пример в группе)\r\n✔Ещё +25 руб - это сделать разные переходы.\r\n✔Ещё + 75 руб - это добавить 1 всплывающую надпись в какой-то 1 момент видео.')
    elif msg == 'Обо Мне':
        send(id, 'Я Андрей. Заказы я могу выполнять с ПН до ПТ с 17 часов вечера и иногда в 1 из выходных дней, что нужно обговаривать заранее;')
    elif msg == 'Заказать Монтаж':
        bot.send_message(message.from_user.id, 'Если вы хотите крутой монтаж, то напишите сколько частей видео нужно соединить?')
        bot.register_next_step_handler(message, reg_parts)

def reg_parts(message):
    global parts
    parts = message.text
    bot.send_message(message.from_user.id, 'Нужна ли фоновая музыка?')
    bot.register_next_step_handler(message, reg_music)

def reg_music(message):
    global music
    music = message.text
    bot.send_message(message.from_user.id, 'До какой даты нужно сделать работу?')
    bot.register_next_step_handler(message, reg_data)

def reg_data(message):
    global data
    data = message.text
    bot.send_message(message.from_user.id, 'Напишите ваше имя и как с вами связаться:')
    bot.register_next_step_handler(message, reg_contact)

def reg_contact(message):
    global contact
    contact = message.text
    bot.send_message(message.from_user.id, 'Заявка отправлена успешно!')
    bot.send_message(chat_id = -490711905, text = "НОВАЯ ЗАЯВКА ОТ ВИДЕО БОТА: " + "Частей в видео: " + parts + "; Фоновая музыка: " + music + "; Дата сдачи: " + data + "; Клиент: " + contact + ";")




bot.polling(none_stop = True)



