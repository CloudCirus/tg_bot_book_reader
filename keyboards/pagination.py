from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicons.lexicon_ru import ButtonNames, Callbacks


# генерируем клавиатуру для страниц книги
def create_pagination_keyboard(page_number: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*[
        InlineKeyboardButton(text=ButtonNames.forward, callback_data=Callbacks.forward),
        InlineKeyboardButton(text=str(page_number)),
        InlineKeyboardButton(text=ButtonNames.backward, callback_data=Callbacks.backward)
    ])
    return kb_builder.as_markup()
