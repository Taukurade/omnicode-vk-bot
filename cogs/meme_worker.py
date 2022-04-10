from re import T
from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import FuncRule, AttachmentTypeRule
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, PhotoMessageUploader
from .database import User, Meme,Methods
from .keyboards import *
import requests
from datetime import datetime as dt
import random


bp = BotLabeler()
api = API(token="81ef2d80a38bf6207b1d8eb22eb0ebac78350c6dd20760b82123aaaf53bd4eb7d05811ad13fce78d22815")#club token
p_upl = PhotoMessageUploader(api)
memes=[]
@bp.message(FuncRule(lambda msg: msg.text.lower() == 'мемы'))
@bp.message(payload_map=[('meme','new')])
async def meme_send(msg: Message):
    Methods.put_memes_in_db()
    mm=get_meme(msg.from_id,)
    if mm < 0:
        await msg.answer("К сожалению неоцененных мемов не осталось :( приходите еще или загрузите свои :3", keyboard=start_keyb())
    else:
        dir= "memes/"+Methods.get_meme_by_id(mm)
        key = Keyboard(one_time=True)
        key.add(Text('👍',{'like':mm}),KeyboardButtonColor.POSITIVE)
        key.add(Text('👎',{'dislike':mm}),KeyboardButtonColor.NEGATIVE)
        key.row()
        key.add(Text('Другой мем',{'meme':'new'}),KeyboardButtonColor.PRIMARY)
        x=await msg.answer("загружаю мем...")
        await msg.answer("Держи :3",attachment=await p_upl.upload(dir), keyboard=key.get_json())
        await api.messages.delete(x.message_id)

@bp.message(FuncRule(lambda msg: msg.text.lower() == 'статистика'))
async def stat(msg: Message):
    await msg.answer("статистика",attachment='',)

@bp.message(payload_map=[('like', int)])
async def like(msg: Message):
    Methods.set_like_dislike(msg.from_id,int(msg.get_payload_json()['like']),1)
    await msg.answer('Вы поставили 👍', keyboard=start_keyb())

@bp.message(payload_map=[('dislike', int)])
async def like(msg: Message):
    Methods.set_like_dislike(msg.from_id,int(msg.get_payload_json()['dislike']),2)
    await msg.answer('Вы поставили 👎', keyboard=start_keyb())
    
@bp.message(AttachmentTypeRule('photo'))
async def upload_meme(msg: Message):
    r = requests.get(msg.attachments[0].photo.sizes[-1].url,allow_redirects=True)
    open(f"{msg.from_id}_{dt.timestamp(dt.now())}.jpg",'wb').write(r.content)
    await msg.answer('Новый мем в нашей коллекции! Спасибо! :3', keyboard=start_keyb())
    


def get_meme(user_id):
    res = []
    
    for meme in Methods.get_memes():
        if meme not in Methods.get_rated_memes(user_id):
            res.append(meme)
        else:
            pass
    if len(res) < 1:
        return -1
    return random.choice(res)

    
    
