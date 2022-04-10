import re
from vkbottle import Keyboard, KeyboardButtonColor, Text, Location, OpenLink, ShowSnackbarEvent
def start_keyb():
    key = Keyboard(one_time=True)
    key.add(Text('Опрос'), KeyboardButtonColor.PRIMARY)
    key.row()
    key.add(Text('Мемы'), KeyboardButtonColor.SECONDARY)
    key.add(Text('Статистика'), KeyboardButtonColor.SECONDARY)
    
    return key.get_json()

def questions():
    v=[
        'Что-ж, начнем!\n Кнопка зеленая?',
        'Кнопка красная?',
        'Кнопка синяя?',
        'Кнопка серая?',
        'Где находится питер?',
        'Вы поставите мне звездочку на гитхабе?',
        'Здесь несколько кнопок?',
        'Здесь несколько разных кнопок?',
        'Спасибо за прохождение опроса!'
    ]
    d = [
        Keyboard(one_time=True),
        Keyboard(one_time=True),
        Keyboard(one_time=True),
        Keyboard(one_time=True),
        Keyboard(one_time=True),
        Keyboard(one_time=True),
        Keyboard(one_time=True),
        Keyboard(one_time=True),
        Keyboard(one_time=True)
    ]
    #кнопка зеленая?
    d[0].add(Text('Да',{'q':1}), KeyboardButtonColor.POSITIVE)
    #кнопка красная?
    d[1].add(Text('Да',{'q':2}), KeyboardButtonColor.NEGATIVE)
    #кнопка синяя?
    d[2].add(Text('Да',{'q':3}), KeyboardButtonColor.PRIMARY)
    #кнопка серая?
    d[3].add(Text('Да',{'q':4}), KeyboardButtonColor.SECONDARY)
    #где находится Питер?
    d[4].add(Location(({'q':5})))
    #вы поставите мне звездочку на гитхабе?
    d[5].add(OpenLink('https://github.com/Taukurade/omnicode-vk-bot','Поставить',{'q':6}))
    d[5].row()
    d[5].add(Text('Уже стоит',{'q':6}),KeyboardButtonColor.POSITIVE)
    d[5].add(Text('Нет',{'q':6}),KeyboardButtonColor.NEGATIVE)
    #здеь несколько кнопок? 
    d[6].add(Text('Да',{'q':7}), KeyboardButtonColor.SECONDARY)
    d[6].row()
    d[6].add(Text('Да',{'q':7}), KeyboardButtonColor.SECONDARY)
    d[6].add(Text('Да',{'q':7}), KeyboardButtonColor.SECONDARY)
    #здесь несколько разных кнопок?
    d[7].add(Text('Да',{'q':8}), KeyboardButtonColor.PRIMARY)
    d[7].add(Text('Ага',{'q':8}), KeyboardButtonColor.SECONDARY)
    d[7].row()
    d[7].add(Text('Нет(Да)',{'q':8}), KeyboardButtonColor.NEGATIVE)
    #Спасибо за прохождение опроса!
    d[8].add(Text('Опрос'), KeyboardButtonColor.PRIMARY)
    d[8].row()
    d[8].add(Text('Мемы'), KeyboardButtonColor.SECONDARY)
    d[8].add(Text('Статистика'), KeyboardButtonColor.SECONDARY)
    return v,d