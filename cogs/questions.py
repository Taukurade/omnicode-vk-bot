from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import FuncRule
from vkbottle import Keyboard, KeyboardButtonColor, Text
from .keyboards import *
bp = BotLabeler()


@bp.message(FuncRule(lambda msg: 'опрос' == msg.text.lower()))
async def q(message: Message):
    d=questions()
    await message.answer(d[0][0], keyboard=d[1][0])
@bp.message(payload_map=[('q',int)])
async def asking(msg: Message):
    i=int(msg.get_payload_json()['q'])
    d=questions()
    
    await msg.answer(d[0][i], keyboard=d[1][i].get_json())
