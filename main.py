import telebot
from telebot import types
import datetime

bot = telebot.TeleBot('6874543945:AAEYlaPxjoXhBwmfuufkKbOJ6qsqcCHzHSA')


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


# Функция для обработки команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    help_message = """
🤖 Привет! Я бот для удобного просмотра расписания в институте.

Я создан в рамках курса по разработке пользовательского интерфейса студенткой группвы 4311-22 Уламасовой Арина.
Вот что я могу:

/start - начать взаимодействие с ботом
/help - получить справку о боте и доступных командах
/week - узнать, четная ли текущая неделя
/kstu - получить ссылку на официальный сайт КНИТУ
/vk - получить ссылку на официальную группа вконтакте КНИТУ
/location - получить адреса всех учебных корпусов
    """
    bot.send_message(message.chat.id, help_message)


# Обработчик для команды /location
@bot.message_handler(commands=['location'])
def handle_location(message):
    locations = """
    Местонахождение учебных корпусов:

    Корпус «А» - г. Казань, ул. К. Маркса, 68
    Корпус «Б», «В», «О» - г. Казань, ул. К. Маркса, 72
    Корпус «Д», «Е», «Л», «М» - г. Казань, ул. Сибирский тракт, 12
    Корпус «К» - г. Казань, ул. Толстого, 8/31
    Корпус «Г» - г. Казань, ул. Попова, 10
    Корпус «И» - г. Казань, ул. Сибирский тракт, 41
    Корпус «Т» - г. Казань, ул. Толстого, 6 корпус 1
    """
    bot.send_message(message.chat.id, locations)


# Обработчик для команды /vk
@bot.message_handler(commands=['vk'])
def handle_vk_group(message):
    vk_group_url = "https://vk.com/knitu"
    bot.send_message(message.chat.id,
                     f"Группа Казанского национального технического университета (КазНИТУ) во ВКонтакте: {vk_group_url}")


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
    if not is_even_week():
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


@bot.message_handler(func=lambda message: message.text == "Четверг")
def handle_thursday(message):
    if is_even_week():
        schedule = not """
        📅 *Четверг* 

        🕚 11:20 - АИС В-302а - Титцов
        🕛 13:00 - АИС В-302а - Титцов
        🕟 14:40 - АИС В-302а - Титцов
        """
    else:
        schedule = """
        📅 *Четверг* 

        🕚 11:20 - ЭП В-319 - Феликсовна
        🕛 13:00 - АИС В-302а - Титцов
        🕟 14:40 - АИС В-302а - Титцов
        """

    bot.send_message(message.chat.id, schedule, parse_mode="Markdown")


# Функция для обработки нажатия на кнопку "Пятница"
@bot.message_handler(func=lambda message: message.text == "Пятница")
def handle_friday(message):
    if not is_even_week():
        schedule = """
        📅 *Пятница* 

        🕗 8:00 - РПИ В-302б - Вотякова Л. Р.
        🕚 9:40 - РПИ В-302б - Вотякова Л. Р.
        🕛 13:00 - Физ-ра - Мирас - Тренер Михаил
        """
    else:
        schedule = """
        📅 *Пятница* 

        🕛 13:00 - Физ-ра - Мирас - Тренер Михаил
        """

    bot.send_message(message.chat.id, schedule, parse_mode="Markdown")


# Функция для обработки нажатия на кнопку "Расписание на текущую неделю"
@bot.message_handler(func=lambda message: message.text == "Расписание на текущую неделю")
def handle_current_week_schedule(message):
    if not is_even_week():
        schedule = """
        (чет неделя)
        📅 *Расписание на текущую неделю* 

        📆 *Понедельник*

        🕤 9:40 - СИИ О-105 - Аскарович
        🕚 11:20 - Защ. Инф В-302а - Аскарович
        🕛 13:00 - СИИ О-105 - Аскарович
        🕟 14:40 - РПИ В-101 - Вотякова Л. Р.

        📆 *Вторник*

        🕗 8:00 - Физ-ра - Мирас - Тренер Михаил

        📆 *Среда*

        🕤 9:40 - ПИС В-101 - Панченко О. В.
        🕚 11:20 - ПИС В-101 - Панченко О. В.
        🕟 13:00 - - ЭП В-319 - Феликсовна
        🕟 14:40 - - ЭП В-319 - Феликсовна

        📆 *Четверг*

        🕚 11:20 - АИС В-302а - Титцов
        🕛 13:00 - АИС В-302а - Титцов
        🕟 14:40 - АИС В-302а - Титцов

        📆 *Пятница*

        🕗 8:00 - РПИ В-302б - Вотякова Л. Р.
        🕚 9:40 - РПИ В-302б - Вотякова Л. Р.
        🕛 13:00 - Физ-ра - Мирас - Тренер Михаил
        """
    else:
        schedule = """
         (нечет неделя)
        📅 *Расписание на текущую неделю*

        📅 *Понедельник*

        🕤 9:40 - СИИ О-105 - Аскарович
        🕚 11:20 - Защ. Инф В-302а - Аскарович
        🕛 13:00 - Защ. Инф В-302а - Аскарович
        🕟 14:40 - РПИ В-101 - Вотякова Л. Р.


        📅 *Вторник*

        🕗 8:00 - Физ-ра - Мирас - Тренер Михаил


        📅 *Среда*

        🕤 9:40 - ПИС В-101 - Панченко О. В.
        🕚 11:20 - ПИС В-101 - Панченко О. В.
        🕟 14:40 - ПИС В-101 - Панченко О. В.


        📅 *Четверг* 

        🕚 11:20 - ЭП В-319 - Феликсовна
        🕛 13:00 - АИС В-302а - Титцов
        🕟 14:40 - АИС В-302а - Титцов


        📅 *Пятница* 

        🕛 13:00 - Физ-ра - Мирас - Тренер Михаил
        """

    bot.send_message(message.chat.id, schedule, parse_mode="Markdown")


# Функция для обработки нажатия на кнопку "Расписание на след неделю"
@bot.message_handler(func=lambda message: message.text == "Расписание на следующую неделю")
def handle_current_week_schedule(message):
    if is_even_week():
        schedule = """
         (чет неделя)
        📅 *Расписание на следующую неделю*
        
        📆 *Понедельник*

        🕤 9:40 - СИИ О-105 - Аскарович
        🕚 11:20 - Защ. Инф В-302а - Аскарович
        🕛 13:00 - СИИ О-105 - Аскарович
        🕟 14:40 - РПИ В-101 - Вотякова Л. Р.

        📆 *Вторник*

        🕗 8:00 - Физ-ра - Мирас - Тренер Михаил

        📅 *Среда* 

        🕤 9:40 - ПИС В-101 - Панченко О. В.
        🕚 11:20 - ПИС В-101 - Панченко О. В.
        🕟 13:00 - ЭП В-318 - Феликсовна
        🕟 14:40 - ЭП В-318 - Феликсовна
        
        📆 *Четверг*

        🕚 11:20 - АИС В-302а - Титцов
        🕛 13:00 - АИС В-302а - Титцов
        🕟 14:40 - АИС В-302а - Титцов

        📆 *Пятница*

        🕗 8:00 - РПИ В-302б - Вотякова Л. Р.
        🕚 9:40 - РПИ В-302б - Вотякова Л. Р.
        🕛 13:00 - Физ-ра - Мирас - Тренер Михаил
        """
    else:

        schedule = """
         (нечет неделя)
        📅 *Расписание на текущую неделю* 

        📅 *Понедельник*

        🕤 9:40 - СИИ О-105 - Аскарович
        🕚 11:20 - Защ. Инф В-302а - Аскарович
        🕛 13:00 - Защ. Инф В-302а - Аскарович
        🕟 14:40 - РПИ В-101 - Вотякова Л. Р.


        📅 *Вторник*

        🕗 8:00 - Физ-ра - Мирас - Тренер Михаил


        📅 *Среда*

        🕤 9:40 - ПИС В-101 - Панченко О. В.
        🕚 11:20 - ПИС В-101 - Панченко О. В.
        🕟 14:40 - ПИС В-101 - Панченко О. В.


        📅 *Четверг* 

        🕚 11:20 - ЭП В-319 - Феликсовна
        🕛 13:00 - АИС В-302а - Титцов
        🕟 14:40 - АИС В-302а - Титцов


        📅 *Пятница* 

        🕛 13:00 - Физ-ра - Мирас - Тренер Михаил
        """

    bot.send_message(message.chat.id, schedule, parse_mode="Markdown")


# Функция для обработки команды /week
@bot.message_handler(commands=['week'])
def handle_week(message):
    week_type = "нечетная" if is_even_week() else "четная"
    bot.send_message(message.chat.id, f"Текущая неделя: {week_type}", parse_mode="Markdown")


# Функция для обработки команды /kstu
@bot.message_handler(commands=['kstu'])
def handle_kstu(message):
    kstu_url = "https://www.kstu.ru/"
    bot.send_message(message.chat.id,
                     f"Официальный сайт Казанского национального исследовательского технологического университетп (КНИТУ): {kstu_url}")


# Обработчик для сообщения "блин"
@bot.message_handler(func=lambda message: message.text.lower() == "блин")
def handle_blin(message):
    bot.send_message(message.chat.id,
                     "Не расстраивайтесь. Если не получается что-то найти, вы можете воспользоваться командной /help")


# Обработчик для сообщения "где моя пара"
@bot.message_handler(func=lambda message: message.text.lower() == "где моя пара")
def handle_schedule_location(message):
    bot.send_message(message.chat.id,
                     "Для получения адресов всех корпусов, вы можете воспользоваться командной /location")


# Обработчик для сообщения "я голоден"
@bot.message_handler(func=lambda message: message.text.lower() == "я голоден")
def handle_hungry(message):
    bot.send_message(message.chat.id,
                     "Это печально. Но вы всегда можете покушать в столовой в Д корпусе или в кафетерии Б корпусе.")


# Обработчик для неизвестных команд или сообщений
@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.send_message(message.chat.id, "Извините, я Вас не понял.")


# Запускаем бота
bot.polling()
