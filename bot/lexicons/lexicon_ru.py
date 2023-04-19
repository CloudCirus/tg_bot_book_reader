from dataclasses import dataclass, asdict


@dataclass
class Answers:
    start = '<b>Привет, читатель!</b>\n\nЭто бот, в котором '
    'ты можешь прочитать книгу Рэя Брэдбери "Марсианские '
    'хроники"\n\nЧтобы посмотреть список доступных '
    'команд - набери /help'

    help = '<b>Это бот-читалка</b>\n\nДоступные команды:\n\n/beginning - '
    'перейти в начало книги\n/continue - продолжить '
    'чтение\n/bookmarks - посмотреть список закладок\n/help - '
    'справка по работе бота\n\nЧтобы сохранить закладку - '
    'нажмите на кнопку с номером страницы\n\n<b>Приятного чтения!</b>'

    no_bookmarks = 'У вас пока нет ни одной закладки.\n\nЧтобы '
    'добавить страницу в закладки - во время чтения '
    'книги нажмите на кнопку с номером этой '
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


@dataclass
class MenuCommandsArgs:
    beginning = {'command': '/beginning', 'description': 'В начало книги'}
    continue_com = {'command': '/continue', 'description': 'Продолжить чтение'}
    bookmarks = {'command': '/bookmarks', 'description': 'Мои закладки'}
    help = {'command': '/help', 'description': 'Справка по работе бота'}

    @classmethod
    def to_dict(cls):
        return asdict(cls())