import telebot
from telebot import types
from telebot import types

# Указываем токен
bot = telebot.TeleBot('6748696729:AAGPhflNL26tCYYSic7CeN5_ZGWFKQFXCks')


@bot.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        def number_telephone(function_call):
            bot.send_message(function_call.from_user.id, text='можете оставить свои контакты и свами свяжется менджер\n'
                                                              'или можете начать общение с ним в чате')


        if function_call.data == "yes":
            print('id пользователя +', function_call.message.chat.id)
            second_mess = "ниже будут представленны категории"
            markup_group = types.InlineKeyboardMarkup()
            bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup_group)
            bot.answer_callback_query(function_call.id)
            keyboard = types.InlineKeyboardMarkup()
            # По очереди готовим текст и обработчик для каждого знака зодиака
            key_oven = types.InlineKeyboardButton(text='Ремонт ноутбука', callback_data='laptop')
            keyboard.add(key_oven)
            pc = types.InlineKeyboardButton(text='Ремонт компьютера', callback_data='pc')
            keyboard.add(pc)
            mobile = types.InlineKeyboardButton(text='Ремонт телефона', callback_data='mobile')
            keyboard.add(mobile)
            printer = types.InlineKeyboardButton(text='Ремонт принтера', callback_data='printer')
            keyboard.add(printer)
            bot.send_message(function_call.from_user.id, text='Выберите устройство', reply_markup=keyboard)

        if function_call.data == 'laptop':
            keyboard = types.InlineKeyboardMarkup()
            # По очереди готовим текст и обработчик для каждого знака зодиака
            key_oven = types.InlineKeyboardButton(text='не включается', callback_data='laptop_Not_included')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='не заряжается', callback_data='laptop_Not_charging')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Отсутствует  изображение', callback_data='laptop_Missing_image')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Чистка ноутбука', callback_data='laptop_Laptop_cleaning')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Сильно шумит\греется', callback_data='laptop_noisy_heated')
            keyboard.add(key_oven)
            bot.send_message(function_call.from_user.id, text='Выберите поломку', reply_markup=keyboard)

        elif function_call.data == 'pc':

            keyboard = types.InlineKeyboardMarkup()
            # По очереди готовим текст и обработчик для каждого знака зодиака
            key_oven = types.InlineKeyboardButton(text='не включается', callback_data='pc_Not_included')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Отсутствует  изображение', callback_data='pc_Missing_image')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Сильно шумит', callback_data='pc_noise')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Чистка компьютера', callback_data='pc_cleaning')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Не загружает ОС Windows', callback_data='pc_Does_not_load_Windows_OS')
            keyboard.add(key_oven)
            bot.send_message(function_call.from_user.id, text='Выберите поломку', reply_markup=keyboard)


        elif function_call.data == 'mobile':
            keyboard = types.InlineKeyboardMarkup()
            # По очереди готовим текст и обработчик для каждого знака зодиака
            key_oven = types.InlineKeyboardButton(text='не включается', callback_data='mobile_Not_included')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Разбит дисплей', callback_data='mobile_display_broken')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Не заряжается', callback_data='mobile_Not_charging')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Попала влага', callback_data='mobile_Moisture_got_in')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Другое', callback_data='mobile_Other')
            keyboard.add(key_oven)
            bot.send_message(function_call.from_user.id, text='Выберите поломку', reply_markup=keyboard)

        elif function_call.data == 'printer':
            keyboard = types.InlineKeyboardMarkup()
            # По очереди готовим текст и обработчик для каждого знака зодиака
            key_oven = types.InlineKeyboardButton(text='Заправка картриджей', callback_data='printer_Refilling_cartridges')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Не захватывает бумагу', callback_data='printer_Does_not_capture_paper')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Зажевывает бумагу', callback_data='printer_Chews_paper')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Грязно печатает', callback_data='printer_Dirty_typing')
            keyboard.add(key_oven)
            key_oven = types.InlineKeyboardButton(text='Другое', callback_data='printer_other')
            keyboard.add(key_oven)
            bot.send_message(function_call.from_user.id, text='Выберите поломку', reply_markup=keyboard)


        # обработчики для ноутбука
        elif function_call.data == 'laptop_Not_included' or function_call.data =='laptop_Not_charging' or function_call.data =='laptop_Missing_image':
            bot.send_message(function_call.from_user.id,
                             text='Необходима диагностика. Можете оставить контакты, чтобы менеджер связался с вами и сориентировал по цене и срокам')
        elif function_call.data == 'laptop_Laptop_cleaning':
            bot.send_message(function_call.from_user.id,
                             text='Техническое обслуживание ноутбука от 1500р. Можете оставить контакты, чтобы менеджер связался с вами и сориентировал по цене и срокам')
        elif function_call.data == 'laptop_noisy_heated':
            bot.send_message(function_call.from_user.id,
                             text='Техническое обслуживание ноутбука от 1500р + возможная замена вентилятора. Можете оставить контакты, чтобы менеджер связался с вами и сориентировал по цене и срокам')

        # обработчики для пк
        elif function_call.data == 'pc_Not_included' or function_call.data == 'pc_Missing_image':
            bot.send_message(function_call.from_user.id,
                             text='Необходима диагностика. Можете оставить контакты, чтобы менеджер связался с вами и сориентировал по цене и срокам')
            number_telephone(function_call)
        elif function_call.data == 'pc_noise':
            bot.send_message(function_call.from_user.id,
                             text='Техническое обслуживание компьютера от 1000р. Можете оставить контакты, чтобы менеджер связался с вами и сориентировал по цене и срокам ')
        elif function_call.data == 'pc_cleaning':
            bot.send_message(function_call.from_user.id,
                             text='Техническое обслуживание компьютера от 1000р. Можете оставить контакты, чтобы менеджер связался с вами и сориентировал по цене и срокам ')
        elif function_call.data == 'pc_Does_not_load_Windows_OS':
            bot.send_message(function_call.from_user.id,
                             text='Переустановка ОС Windows от 1500р. Можете оставить контакты, чтобы менеджер связался с вами и сориентировал по цене и срокам ')

            # обработчики для телефона
        elif function_call.data == 'mobile_Not_included' or function_call.data == 'mobile_Other':
            bot.send_message(function_call.from_user.id,
                             text='Необходима диагностика. Можете оставить контакты, чтобы менеджер связался с вами и сориентировал по цене и срокам')
        elif function_call.data == 'mobile_display_broken':
            bot.send_message(function_call.from_user.id,
                             text='Замена дисплея от 1800р + запчасть. Можете оставить контакты, чтобы менеджер связался с вами и сориентировал по цене и срокам')
        elif function_call.data == 'mobile_Not_charging':
            bot.send_message(function_call.from_user.id,
                             text='Замена разъема зарядки от 1200р. Можете оставить контакты, чтобы менеджер связался с вами и сориентировал по цене и срокам')
        elif function_call.data == 'mobile_Moisture_got_in':
            bot.send_message(function_call.from_user.id,
                             text='Чистка от залития от 1500р. Можете оставить контакты, чтобы менеджер связался с вами и сориентировал по цене и срокам')

        # обработчики для принтера
        elif function_call.data == 'printer_Refilling_cartridges':
            bot.send_message(function_call.from_user.id,
                             text='Заправка только черно-белых лазерных картриджей, от 400р')
        elif function_call.data == 'printer_Does_not_capture_paper' or function_call.data == 'printer_Chews_paper' or function_call.data == 'printer_Dirty_typing' or function_call.data == 'printer_other':
            bot.send_message(function_call.from_user.id,
                             text='Можете оставить контакты, чтобы менеджер связался с вами и сориентировал по цене и срокам')










@bot.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, тут будет какое-то приветствие"
    print(message.from_user.first_name, "+" , message.from_user.last_name)
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='увидеть перечень услуг', callback_data='yes')
    markup.add(button_yes)
    bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
    print('id пользователя', message.chat.id)




while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        pass
