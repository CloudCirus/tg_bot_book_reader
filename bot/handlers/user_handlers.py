from copy import deepcopy

from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message

from bot.database.test_database import user_dict_template, users_db
from bot.filters.custom_filters import IsDelBookmarkCallbackData, IsDigitCallbackData
from bot.keyboards.bookmarks import create_bookmarks_keyboard, create_edit_keyboard
from bot.keyboards.pagination import create_pagination_keyboard
from bot.lexicons.lexicon_ru import Answers
from book.book_converter import book

router: Router = Router()


# срабатывает на команду "/start" -
# добавляет пользователя в базу данных, если его там еще не было
# и отправляет ему приветственное сообщение
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(Answers.start)
    user_id = message.from_user.id
    if user_id not in users_db:
        users_db[user_id] = deepcopy(user_dict_template)


# срабатывает на команду "/help"
# и отправляет пользователю сообщение со списком доступных команд
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(Answers.help)


# срабатывает на команду "/beginning"
# и отправляет первую страницу книги с кнопками пагинации
@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message):
    user_id = message.from_user.id
    users_db[user_id]['page'] = 1
    text = book[users_db[user_id]['page']]
    print(text)
    print(f'{users_db[user_id]["page"]}/{len(book)}')
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            f'{users_db[user_id]["page"]}/{len(book)}'
        )
    )


# срабатывает на команду "/continue"
# и отправляет страницу книги, на которой пользователь
# остановился в процессе использования бота
@router.message(Command(commands='continue'))
async def process_continue_command(message: Message):
    user_id = message.from_user.id
    text = book[users_db[user_id]['page']]
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            f'{users_db[user_id]["page"]}/{len(book)}'
        )
    )


# срабатывает на команду "/bookmarks"
# и отправляет пользователю список сохраненных закладок,
# если они есть или сообщение о том, что закладок нет
@router.message(Command(commands='bookmarks'))
async def process_bookmarks_command(message: Message):
    user_id = message.from_user.id
    if users_db[user_id]['bookmarks']:
        await message.answer(
            text=Answers.bookmarks,
            reply_markup=create_bookmarks_keyboard(
                *users_db[user_id]['bookmarks']
            )
        )
    else:
        await message.answer(text=Answers.no_bookmarks)


# срабатывает на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя с сообщением-страницей книги
@router.callback_query(Text(text='forward'))
async def process_forward_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    if users_db[user_id]['page'] < len(book):
        users_db[user_id]['page'] += 1
        text = book[users_db[user_id]['page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                f'{users_db[user_id]["page"]}/{len(book)}'
            )
        )
    await callback.answer()


# срабатывает на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя с сообщением-страницей книги
@router.callback_query(Text(text='backward'))
async def process_backward_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    if users_db[user_id]['page'] > 1:
        users_db[user_id]['page'] -= 1
        text = book[users_db[user_id]['page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                f'{users_db[user_id]["page"]}/{len(book)}'
            )
        )
    await callback.answer()


# срабатывает на нажатие инлайн-кнопки
# с номером текущей страницы и добавляет текущую страницу в закладки
@router.callback_query(lambda x: '/' in x.data and x.data.replace('/', '').isdigit())
async def process_page_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    users_db[user_id]['bookmarks'].add(users_db[user_id]['page'])
    await callback.answer('Страница добавлена в закладки!')


# срабатывает на нажатие инлайн-кнопки с закладкой из списка закладок
@router.callback_query(IsDigitCallbackData())
async def process_bookmark_press(callback: CallbackQuery):
    data, user_id = callback.data, callback.from_user.id
    text = book[int(data)]
    users_db[user_id]['page'] = int(data)
    await callback.message.edit_text(
        text=text,
        reply_markup=create_pagination_keyboard(
            f'{users_db[user_id]["page"]}/{len(book)}'
        )
    )
    await callback.answer()


# срабатывает на нажатие инлайн-кнопки "редактировать" под списком закладок
@router.callback_query(Text(text='edit_bookmarks'))
async def process_edit_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Answers.edit_bookmarks,
        reply_markup=create_edit_keyboard(
            *users_db[callback.from_user.id]['bookmarks']))
    await callback.answer()


# срабатывает на нажатие инлайн-кнопки
# "отменить" во время работы со списком закладок (просмотр и редактирование)
@router.callback_query(Text(text='cancel'))
async def process_cancel_press(callback: CallbackQuery):
    await callback.message.edit_text(text=Answers.cancel_text)
    await callback.answer()


# срабатывает на нажатие инлайн-кнопки с закладкой из списка закладок к удалению
@router.callback_query(IsDelBookmarkCallbackData())
async def process_del_bookmark_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    users_db[user_id]['bookmarks'].remove(int(callback.data[:-3]))
    if users_db[user_id]['bookmarks']:
        await callback.message.edit_text(
            text=Answers.bookmarks,
            reply_markup=create_edit_keyboard(
                *users_db[user_id]['bookmarks']
            )
        )
    else:
        await callback.message.edit_text(text=Answers.no_bookmarks)
    await callback.answer()
