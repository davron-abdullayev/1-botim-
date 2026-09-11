import os
import asyncio
from aiogram import Bot,Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.filters import CommandStart

load_dotenv()

dp=Dispatcher()
bot=Bot(token=os.getenv("TOKEN"))




@dp.message(CommandStart())
async def starthandler(message:Message):
      await message.answer("Salom botimizga hush kelibsiz")


async def main():
      await dp.start_polling(bot)


if __name__=="__main__":
      asyncio.run(main())