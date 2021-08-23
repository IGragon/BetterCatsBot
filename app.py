from aiogram.utils import executor
from aiogram.utils.executor import start_webhook

from config import WEBHOOK_PATH, WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT
from handlers import dp
from loader import bot, storage


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


if __name__ == '__main__':  # start webhook with necessary parameters
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
