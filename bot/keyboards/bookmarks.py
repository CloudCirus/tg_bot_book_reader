from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.lexicons.lexicon_ru import ButtonNames, Callbacks
from book.book_converter import book


def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(args):
        kb_builder.row(InlineKeyboardButton(
            text=f'{button} - {book[button][:100]}',
            callback_data=str(button)))
    # Добавляем в клавиатуру в конце две кнопки "Редактировать" и "Отменить"
    kb_builder.row(
        InlineKeyboardButton(
            text=ButtonNames.edit_bookmarks,
            callback_data=Callbacks.edit_bookmarks),
        InlineKeyboardButton(
            text=ButtonNames.cancel,
            callback_data=Callbacks.cancel),
        width=2)
    return kb_builder.as_markup()


def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(args):
        kb_builder.row(
            InlineKeyboardButton(
                text=f'{ButtonNames.delete} {button} - {book[button][:100]}',
                callback_data=f'{button}{Callbacks.delete}')
        )
    # Добавляем в конец клавиатуры кнопку "Отменить"
    kb_builder.row(
        InlineKeyboardButton(
            text=ButtonNames.cancel,
            callback_data=Callbacks.cancel)
    )
    return kb_builder.as_markup()
