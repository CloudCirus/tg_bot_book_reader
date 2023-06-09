from dataclasses import dataclass, asdict
from typing import Tuple, Dict

from pydantic import BaseModel


@dataclass
class Answers:
    start = '<b>Привет, читатель!</b>\n\n' \
            'Это бот, в котором ты можешь прочитать книгу.\n\n' \
            'Чтобы посмотреть список доступных команд - набери /help'

    help = '<b>Это бот-читалка</b>\n\nДоступные команды:\n\n/beginning - ' \
           'перейти в начало книги\n/continue - продолжить ' \
           'чтение\n/bookmarks - посмотреть список закладок\n/help - ' \
           'справка по работе бота\n\nЧтобы сохранить закладку - ' \
           'нажмите на кнопку с номером страницы\n\n<b>Приятного чтения!</b>'

    no_bookmarks = 'У вас пока нет ни одной закладки.\n\nЧтобы ' \
                   'добавить страницу в закладки - во время чтения ' \
                   'книги нажмите на кнопку с номером этой ' \
                   'страницы\n\n/continue - продолжить чтение'

    bookmarks = '<b>Это список ваших закладок:</b>'
    edit_bookmarks = '<b>Редактировать закладки</b>'

    cancel_text = '/continue - продолжить чтение'


@dataclass
class ButtonNames:
    edit_bookmarks = '❌ РЕДАКТИРОВАТЬ'
    delete = '❌'
    cancel = 'ОТМЕНИТЬ'
    forward = '>>'
    backward = '<<'


@dataclass
class Callbacks:
    forward = 'forward'
    backward = 'backward'
    edit_bookmarks = 'edit_bookmarks'
    cancel = 'cancel'
    delete = 'del'


@dataclass
class Commands:
    start = '/start'
    help = '/help'
    beginning = '/beginning'
    bookmarks = '/bookmarks'
    contin = '/continue'


def get_menu_args() -> list[dict]:
    _commands = Commands()
    return [
        {'command': _commands.beginning, 'description': 'В начало книги'},
        {'command': _commands.contin, 'description': 'Продолжить чтение'},
        {'command': _commands.bookmarks, 'description': 'Мои закладки'},
        {'command': _commands.help, 'description': 'Справка по работе бота'}
    ]
