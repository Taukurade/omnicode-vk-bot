import re
from peewee import *
import os
db = SqliteDatabase('users.db')

class Model(Model):
    class Meta:
        database = db
        primary_key = False
class Meme(Model):
    meme_id = IntegerField(primary_key=True)
    dir = TextField(unique=True)

class User(Model):
    user_id = IntegerField()
    meme = IntegerField(unique=True)
    status = IntegerField(default=0)
db.create_tables([Meme, User])
class Methods:
    def set_like_dislike(user_id,meme,ldsl):
        """
        ldsl: int
        0 - не оценено
        1 - лайк
        2 - дизлайк
        """
        query=User.select().where(User.user_id==user_id and User.meme==meme)
        if query.exists():
            query.like = ldsl
        else:
            User.create(user_id=user_id,meme=meme,status=ldsl)
            pass
    
    def put_memes_in_db():
        memes = os.listdir('memes')
        for meme in memes:
            if Meme.select().where(Meme.dir == meme).exists():
                pass
            else:
                Meme.create(dir=meme) 
    def calc_statistic(user_id):
        
        total_likes = len(User.select().where(User.status == 1))
        total_dislikes = len(User.select().where(User.status == 2))
        
        user_likes = len(User.select().where(User.user_id==user_id and User.status == 1))
        user_dislikes = len(User.select().where(User.user_id==user_id and User.status == 2))
        return {'total_l':total_likes,'total_d':total_dislikes,'user_l':user_likes,'user_d':user_dislikes}
    def get_memes():
        
        return [x.meme_id for x in Meme.select().where(1==1)]
    def get_rated_memes(user_id):
        return [x.meme for x in User.select().where(User.user_id==user_id and (User.status == 1 or User.status == 2))]

    def get_meme_by_id(id):
        return [x.dir for x in Meme.select().where(Meme.meme_id == id)][0]


