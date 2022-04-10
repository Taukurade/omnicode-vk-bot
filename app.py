
from vkbottle.bot import Bot
token = '81ef2d80a38bf6207b1d8eb22eb0ebac78350c6dd20760b82123aaaf53bd4eb7d05811ad13fce78d22815'
from cogs import blueprints

bot = Bot(token)

for bp in blueprints:
    bot.labeler.load(bp)
bot.run_forever()

