import discord
import asyncio
import requests
import ctx
import random
import time, threading

DISCORD_BOT_TOKEN = 'NDcwNjkwNjMzODI1MjU1NDI0.DxEEZw.wijI1jIlACy1q1cX0kNzsaNcr4k'

BTC_PRICE_URL_coinmarketcap = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=RUB'

client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
@client.event

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!Миша'):
        log(message)
        Misha_rand = ['Бан нахуй ему дайте , он даже меня заебал','Я бы ему на лицо нассал','Хай бэбибон','Он ебаный чсв кид, пизди его ногами нахуй']
        await client.send_message(message.channel, random.choice(Misha_rand))
    if message.content.startswith('!pidor'):
        log(message)
        mem = []
        for member in message.server.members:
            mem.append(member)
            user = str(random.choice(mem))
        pidoras = discord.utils.get(message.server.members, name=user.split('#')[0], discriminator=user.split('#')[1])
        pidoras = pidoras.mention
        #pidoras = random.choice(lol)
        await client.send_message(message.channel, random.choice(['Система поиска пидорасов активирована', 'Происходит взлом...', 'Фиксим краши', 'Дебажу...']))
        await client.send_message(message.channel, random.choice(['Сегодня пидор дня у нас ', 'Вжух, и ты пидор ', 'Да ты пидорас, ']) + pidoras)
    if message.content.startswith('!Шар'):
        log(message)
        yes_no = ['да','Нет','Сервера не отвечают бим-бом 404....','бля хз']
        await client.send_message(message.channel,random.choice(yes_no))
    if message.content.startswith('!h'):
        log(message)
        pidoras = discord.utils.get(message.server.members, name='MishaRicco', discriminator='3165')
        pidoras = pidoras.mention
        await client.send_message(message.channel,'!Миша - базарит за Михаила Рико {}\n!pidor - рандомный блять пидорас с сервера нахуй\n!Шар - Да нет пидора рандомного ответ'.format(pidoras))
def log(message):
    try:
        print('=================================================')
        print('New Message!')
        print('Text: {0.content}'.format(message))
        print('Server: {0}'.format(message.server.name))
        print('=================================================')
    except:
        print('=================================================')
        print('New Message!')
        print('Text: {0.content}'.format(message))
        print('=================================================')
client.run(DISCORD_BOT_TOKEN)