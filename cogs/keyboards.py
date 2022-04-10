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
    d = [
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
    d[0].add(Text('Да',{1}), KeyboardButtonColor.POSITIVE)
    #кнопка красная?
    d[1].add(Text('Да',{2}), KeyboardButtonColor.NEGATIVE)
    #кнопка синяя?
    d[2].add(Text('Да',{3}), KeyboardButtonColor.PRIMARY)
    #кнопка серая?
    d[3].add(Text('Да',{4}), KeyboardButtonColor.SECONDARY)
    #где находится Питер?
    d[4].add(Location({5}))
    #вы поставите мне звездочку на гитхабе?
    d[5].add(OpenLink('https://github.com/Taukurade/omnicode-vk-bot','Поставить',{6}))
    #здеь несколько кнопок?
    d[6].add(Text('Да',{7}), KeyboardButtonColor.SECONDARY)
    d[6].add(Text('Да',{7}), KeyboardButtonColor.SECONDARY)
    d[6].add(Text('Да',{7}), KeyboardButtonColor.SECONDARY)
    #здесь несколько разных кнопок?
    d[7].add(Text('Да',{8}), KeyboardButtonColor.PRIMARY)
    d[7].add(Text('Ага',{8}), KeyboardButtonColor.SECONDARY)
    d[7].add(Text('Нет(Да)',{8}), KeyboardButtonColor.NEGATIVE)
    return d