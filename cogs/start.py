from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import FuncRule
from vkbottle import Keyboard, KeyboardButtonColor, Text
from .keyboards import *
bp = BotLabeler()


@bp.message(FuncRule(lambda msg: 'привет' == msg.text.lower()))
@bp.message(payload={'command': 'start'})
async def hi(message: Message):
    key = Keyboard(one_time=True)
    key.add(Text('Опрос'), KeyboardButtonColor.PRIMARY)
    key.row()
    key.add(Text('Мемы'), KeyboardButtonColor.SECONDARY)
    key.add(Text('Статистика'), KeyboardButtonColor.SECONDARY)

    await message.answer("Привет вездекодерам!", keyboard=start_keyb())
    