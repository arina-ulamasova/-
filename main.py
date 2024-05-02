import telebot
from telebot import types
import datetime

bot = telebot.TeleBot('6783981544:AAGjKpBtu5tgPkm9yvN2OYr2AEY0yborSI0')

@bot.message_handler(commands=['start'])
def handle_start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Понедельник")
    item2 = types.KeyboardButton("Вторник")
    item3 = types.KeyboardButton("Среда")
    item4 = types.KeyboardButton("Четверг")
    item5 = types.KeyboardButton("Пятница")
    item6 = types.KeyboardButton("Расписание на текущую неделю")
    item7 = types.KeyboardButton("Расписание на следующую неделю")
    markup.add(item1, item2, item3, item4, item5, item6, item7)


    bot.send_message(message.chat.id, "Чем могу вам помочь? Используйте /help если у вас возникли вопросы",
                     reply_markup=markup)

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Помощь по боту...")


# Функция для определения четности недели
def is_even_week():
    today = datetime.date.today()
    week_number = today.isocalendar()[1]
    return week_number % 2 == 0


# Функция для обработки нажатия на кнопку "Понедельник"
@bot.message_handler(func=lambda message: message.text == "Понедельник")
def handle_monday(message):
    if is_even_week():
        schedule = """
        📅 *Понедельник*

        🕤 9:40 - СИИ О-105 - Аскарович
        🕚 11:20 - Защ. Инф В-302а - Аскарович
        🕛 13:00 - Защ. Инф В-302а - Аскарович
        🕟 14:40 - РПИ В-101 - Вотякова Л. Р.
        """
    else:
        schedule = """
        📅 *Понедельник*

        🕤 9:40 - СИИ О-105 - Аскарович
        🕚 11:20 - Защ. Инф В-302а - Аскарович
        🕛 13:00 - СИИ О-105 - Аскарович
        🕟 14:40 - РПИ В-101 - Вотякова Л. Р.
        """

    bot.send_message(message.chat.id, schedule, parse_mode="Markdown")


# Функция для обработки нажатия на кнопку "Вторник"
@bot.message_handler(func=lambda message: message.text == "Вторник")
def handle_tuesday(message):
    schedule = """
    📅 *Вторник*

    🕗 8:00 - Физ-ра - Мирас - Тренер Михаил
    """
    bot.send_message(message.chat.id, schedule, parse_mode="Markdown")


# Функция для обработки нажатия на кнопку "Среда"
@bot.message_handler(func=lambda message: message.text == "Среда")
def handle_wednesday(message):
    if is_even_week():
        schedule = """
        📅 *Среда* 

        🕤 9:40 - ПИС В-101 - Панченко О. В.
        🕚 11:20 - ПИС В-101 - Панченко О. В.
        🕟 13:00 - ЭП В-318 - Феликсовна
        🕟 14:40 - ЭП В-318 - Феликсовна
        """
    else:
        schedule = """
        📅 *Среда*

        🕤 9:40 - ПИС В-101 - Панченко О. В.
        🕚 11:20 - ПИС В-101 - Панченко О. В.
        🕟 14:40 - ПИС В-101 - Панченко О. В.
        """

    bot.send_message(message.chat.id, schedule, parse_mode="Markdown")


# Запускаем бота
bot.polling()