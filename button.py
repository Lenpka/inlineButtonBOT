from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder
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
# Button1 = KeyboardButton(text = 'Кнопка 1')
# Button2 = KeyboardButton(text = 'Кнопка 2')
keyboard = ReplyKeyboardBuilder()
array_of_button = [KeyboardButton( text = f"Button{j*3 + i}") for i in range(1, 4) for j in range(3)]
#Keyboard = ReplyKeyboardMarkup(keyboard=[array_of_button], resize_keyboard= True, one_time_keyboard= True)
keyboard.row(*array_of_button, width = 3)

@disp.message(CommandStart())
async def start(message:Message):
    await message.answer(text = "Здарова, смотри какая клава?",
                         reply_markup=keyboard.as_markup())
    # Отправка клавиатуры



@disp.message( F.text == "Кнопка 1")
async def but1(message:Message):
    await message.answer(
text= "Прикольно, кнопочка.",


    )
@disp.message (F.text == "Кнопка 2")
async def but2(message:Message):
    await message.answer(
    text = "Ух ты! Еще одна",

)

if __name__ == "__main__":

    disp.run_polling(bot)