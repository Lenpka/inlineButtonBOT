from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
import asyncio
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)
from environs import Env
env:Env = Env()
env.read_env()
BOT_TOKEN = env("BOT_TOKEN")
bot = Bot(BOT_TOKEN)
disp = Dispatcher()
# Кнопки и клавиатура
Button1 = KeyboardButton(text = 'Кнопка 1')
Button2 = KeyboardButton(text = 'Кнопка 2')
Keyboard = ReplyKeyboardMarkup(keyboard=[[Button1, Button2]], resize_keyboard= True, one_time_keyboard= True)

@disp.message(CommandStart())
async def start(message:Message):
    await message.answer(text = "Здарова, смотри какие кнопки внизу, давай глянем?",
                         reply_markup=Keyboard)
    # Отправка клавиатуры



@disp.message( F.text == "Кнопка 1")
async def but1(message:Message):
    await message.answer(
text= "Прикольно, кнопочка.",
reply_markup= ReplyKeyboardRemove()

    )
@disp.message (F.text == "Кнопка 2")
async def but2(message:Message):
    await message.answer(
    text = "Ух ты! Еще одна",
    reply_markup= ReplyKeyboardRemove()
)

if __name__ == "__main__":

    disp.run_polling(bot)