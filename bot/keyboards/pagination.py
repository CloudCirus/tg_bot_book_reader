from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.lexicons.lexicon_ru import ButtonNames, Callbacks


# генерируем клавиатуру для страниц книги
def create_pagination_keyboard(page_number: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*[
        InlineKeyboardButton(text=ButtonNames.backward, callback_data=Callbacks.backward),
        InlineKeyboardButton(text=page_number, callback_data=page_number),
        InlineKeyboardButton(text=ButtonNames.forward, callback_data=Callbacks.forward),
    ])
    return kb_builder.as_markup()
