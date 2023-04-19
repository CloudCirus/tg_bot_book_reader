from aiogram import Bot
from aiogram.types import BotCommand

from lexicons.lexicon_ru import MenuCommandsArgs


# Настройки кнопки Menu бота
async def set_main_menu(bot: Bot) -> None:
    main_menu_commands = [BotCommand(
        **kwargs
    ) for kwargs in MenuCommandsArgs.to_dict().values()]
    await bot.set_my_commands(main_menu_commands)
