from aiogram import Bot, types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

bot = Bot(token="")
dp = Dispatcher(bot)
try:
    with open("sp_gr.txt", "r", encoding="utf-8") as file:
        students = [line.rstrip("\n") for line in file]
        students= list(filter(None, students))
except FileNotFoundError:
    print(f"Файл" 'sp_gr.txt' "не найден")

try:
    with open("zadaniya.txt", "r", encoding="utf-8") as file:
        zadaniya = [line.rstrip("\n") for line in file]
        zadaniya= list(filter(None, zadaniya))
except FileNotFoundError:
    print(f"Файл" 'zadaniya.txt' "не найден")

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    buttons = [
        [types.KeyboardButton(text="Help")],
        [types.KeyboardButton(text="Что-то")]
               ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons,  resize_keyboard=True)

    await message.answer(text="Hello, <em>in absurd world</em>", parse_mode="HTML", reply_markup=keyboard)

HELP_COMMAND = """Этот бот даст задание каждому студенту на зачет сделав это в состоянии абсурда под дозой
/help - список команд
/start - начать работу"""
@dp.message_handler(lambda message: message.text == "Help")
async def help1_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")
    await message.delete()
    
@dp.message_handler(commands=["help"])
async def help2_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")


@dp.message_handler()
async def zadaniya(message:types.Message):
    import random

    a=random.choice(zadaniya)
    found=False
    for name in students:
        if name.startswith(message.text):
            found=True
            break
    if found:
        await message.answer(text=f"Задание....: {a}")
    else:
        await message.answer(text="ты лишний, абсурда не будет")

if __name__ == "main":
    executor.start_polling(dp, skip_updates=True)
