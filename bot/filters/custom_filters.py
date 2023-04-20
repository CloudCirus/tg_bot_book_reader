from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from bot.lexicons.lexicon_ru import Callbacks


class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return isinstance(callback.data, str) and callback.data.isdigit()


class IsDelBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return isinstance(callback.data, str) and Callbacks.delete \
            in callback.data and callback.data[:-3].isdigit()
