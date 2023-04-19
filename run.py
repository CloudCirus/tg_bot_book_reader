import asyncio

from aiogram import Bot, Dispatcher
from bot.configs import BotConfig
from logs_settings import create_logger


async def main():
    create_logger(__name__, 'Starting bot')

    bot_config = BotConfig()

    bot = Bot(token=bot_config.token, parse_mode='HTML')
    dp = Dispatcher()

    # TODO главное меню бота

    # TODO Регистриуем роутеры в диспетчере

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
