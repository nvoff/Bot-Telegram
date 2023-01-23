from aiogram import Bot, Dispatcher, executor, types
import asyncio

bot = Bot(token="token")
dp = Dispatcher(bot)

@dp.message_handler(content_types=['new_chat_members','left_chat_member'])
async def on_user_joined(message: types.Message):
    await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
