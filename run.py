import asyncio

from aiogram import Bot, Dispatcher

from bot.configs.config import BotConfig
from logs_settings import create_logger
from bot.handlers.user_handlers import router as user_router
from bot.handlers.other_handlers import router as other_router
from bot.keyboards.main_menu import set_main_menu
from book.book_converter import prepare_book


async def main():
    create_logger(__name__, 'Starting bot')

    bot_config = BotConfig()

    bot = Bot(token=bot_config.token, parse_mode='HTML')
    dp = Dispatcher()

    await set_main_menu(bot)

    dp.include_router(user_router)
    dp.include_router(other_router)

    # пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    prepare_book('book/books/test_book_2.txt')
    asyncio.run(main())
