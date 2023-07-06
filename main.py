import os

from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')
bot = AsyncTeleBot(TOKEN, parse_mode='HTML')


#создание меню кнопок
@bot.message_handler(commands=['help',  'start'])
async def send_hello(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, 'Вы найдете здесь все популярные мемы!', disable_notification=True, protect_content=True)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    one_b = '2021⚡'
    two_b = '2020🔥'
    three_b = '2019💧'
    four_b = '2018⚡'
    five_b = '2017✨'
    six_b = '2016⚡'
    seven_b = '2022✨'
    eight_b = '2023⚡'
    markup.add(eight_b, seven_b, one_b, row_width=3)
    markup.add(two_b, three_b, row_width=2)
    markup.add(four_b, five_b, six_b, row_width=3)
    await bot.send_message(chat_id, '✨Menu✨', reply_markup=markup)

@bot.message_handler(commands=['a', 'mem2023'])
async def send_dada(message):
    chat_id = message.from_user.id
    await bot.send_audio(chat_id, 'https://zvukogram.com/mp3/cats/1200/ya-musulman.mp3')

@bot.message_handler(commands=['a', 'mem2022'])
async def send_nono(message):
    chat_id = message.from_user.id
    await bot.send_audio(chat_id, 'https://zvukogram.com/mp3/cats/1200/chin-chan-chon-chi-chicha-chochi.mp3')

@bot.message_handler(commands=['a', 'mem2021'])
async def send_youtube(message):
    chat_id = message.from_user.id
    await bot.send_audio(chat_id, 'https://zvukogram.com/mp3/cats/1200/ahaha-razryivnaya.mp3')

@bot.message_handler(commands=['b', 'mem2020'])
async def send_tikt(message):
    chat_id = message.from_user.id
    await bot.send_audio(chat_id, 'https://zvukogram.com/mp3/cats/1200/o-povezlo-povezlo.mp3')

@bot.message_handler(commands=['c', 'mem2019'])
async def send_razrv(message):
    chat_id = message.from_user.id
    await bot.send_audio(chat_id, 'https://zvukogram.com/mp3/cats/1200/es-minus-ehuuu.mp3')

@bot.message_handler(commands=['d', 'mem2018'])
async def send_funny(message):
    chat_id = message.from_user.id
    await bot.send_audio(chat_id, 'https://zvukogram.com/mp3/cats/1200/lya-tyi-kryisa1.mp3')

@bot.message_handler(commands=['e', 'mem2017'])
async def send_smehe(message):
    chat_id = message.from_user.id
    await bot.send_audio(chat_id, 'https://zvukogram.com/mp3/cats/1200/opa-kogo-to-hlopnuli.mp3')

@bot.message_handler(commands=['f', 'mem2016'])
async def send_smex(message):
    chat_id = message.from_user.id
    await bot.send_audio(chat_id, 'https://zvukogram.com/mp3/cats/1200/otdai-salo.mp3')



@bot.callback_query_handler(func=lambda call:True)
async def handle_callback(call):
    chat_id = call.message.chat.id
    button_call = call.data
    if button_call == '2021':
        await bot.send_message(chat_id, '/mem2021')
    elif button_call == '2020':
        await bot.send_message(chat_id, '/mem2020')
    elif button_call == '2019':
        await bot.send_message(chat_id, '/mem2019')
    elif button_call == '2018':
        await bot.send_message(chat_id, '/mem2018')
    elif button_call == '2017':
        await bot.send_message(chat_id, '/mem2017')
    elif button_call == '2016':
        await bot.send_message(chat_id, '/mem2016')
    elif button_call == '2023':
        await bot.send_message(chat_id, '/mem2023')
    elif button_call == '2022':
        await bot.send_message(chat_id, '/mem2022')
    else:
        await bot.send_message(chat_id, 'Вы попали не туда...')





















































import asyncio
asyncio.run(bot.polling())