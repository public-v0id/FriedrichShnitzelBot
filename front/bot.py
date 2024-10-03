import cfg
import telebot
from telebot import types


bot = telebot.TeleBot(cfg.cfg)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Чтобы пользоваться ботом необходимо заполнить анкету')
    bot.send_message(message.chat.id, 'Для начла выберете ваш пол')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bt1 = types.KeyboardButton('Мужской')
    bt2 = types.KeyboardButton('Женский')
    markup.add().row(bt1, bt2)


if __name__ == '__main__':
    bot.polling(non_stop=True)
