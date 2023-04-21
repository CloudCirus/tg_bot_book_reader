from aiogram import Bot
from aiogram.types import BotCommand

from bot.lexicons.lexicon_ru import get_menu_args


# Настройки кнопки Menu бота
async def set_main_menu(bot: Bot) -> None:
    main_menu_commands = [BotCommand(
        **kwargs
    ) for kwargs in get_menu_args()]
    await bot.set_my_commands(main_menu_commands)
