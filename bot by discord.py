import discord #Импортируем библиотеку discord.py
from discord.ext import commands


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user)) #Когда бот будет запущен в консоль будет написано сообщение

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message)) #Все сообщения с серверов на котором стоит бот, будут поступать вам в консоль
        
client = MyClient()
client.run('токен бота') #Запуск бота
