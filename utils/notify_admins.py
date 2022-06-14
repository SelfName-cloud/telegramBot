import logging

from aiogram import Dispatcher
from data.config import admins_id


async def startup_notify(dp: Dispatcher):
    for admin in admins_id:
        try:
            message = 'Bot is ready!'
            await dp.bot.send_message(chat_id=admin, text=message)
        except Exception as ex:
            logging.exception(ex)


