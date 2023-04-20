from aiogram import Router
from aiogram.types import Message

router: Router = Router()


# реагирует на любые сообщения пользователя вне основной логики
@router.message()
async def send_echo(message: Message):
    await message.answer(f'Я не умею обрабатывать такие сообщения: {message.text}')
