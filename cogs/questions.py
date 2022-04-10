from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import FuncRule
from vkbottle import Keyboard, KeyboardButtonColor, Text
from .keyboards import *
bp = BotLabeler()


@bp.message(FuncRule(lambda msg: 'опрос' == msg.text.lower()))
async def q(message: Message):
  
    await message.answer("Что-ж, начнем!\n Кнопка зеленая?", keyboard=questions()[0])
@bp.message(payload_map=[(int)])
async def like(msg: Message):
    i=int(msg.get_payload_json())
    v=[
        '',
        'Кнопка красная?',
        'Кнопка синяя?',
        'Кнопка серая?',
        'Где находится питер?',
        'Вы поставите мне звездочку на гитхабе?',
        'Здесь несколько кнопок?',
        'Здесь несколько разных кнопок?',
        'Спасибо за прохождение опроса!'
    ]
    await msg.answer(v[i], keyboard=questions()[i].get_json())
