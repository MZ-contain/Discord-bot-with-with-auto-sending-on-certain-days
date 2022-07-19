import discord
from discord.ext import tasks, commands
from datetime import datetime
from datetime import date
from datetime import time
TOKEN = ''
PREFIX = '!'#Префикс перед командой(можно изменить)
bot = commands.Bot(command_prefix=PREFIX, help_command=None)
bot.remove_command('help')
today = date.today()
@bot.event
async def on_ready():
    print('Bot logged as {}'.format(bot.user))

@bot.command()# Команда для того, чтоб писать от имен бота
async def r(ctx, *, text):
    def channel_conv(text):
        value  = text.split(" ")
        string = value[0]

        if string.isdigit():
            return (
                client.get_channel(int(string)),
                text.replace(string, "")
            )
        elif string.startswith("<#"):
            return (
                client.get_channel(int(string[2:20])),
                text.replace(string, "")
            )
        else:
            return (
                None,
                text
            )

    try:
        channel = channel_conv(text)
        await channel[0].send(channel[1])
    except:
        await ctx.message.delete()
        await ctx.send(text)

@tasks.loop(seconds = 1.0 )
async def auto_send():
    a = today.weekday # Проверяет день недели
    if a == 0 :
            channel = await bot.fetch_channel(926201516963029014)#Вместо этого числа вписать айди своего канала
            await channel.send('Захват будет через два часа')
    else :
        pass

@tasks.loop(hours = 18.0 )
async def zp_send():
    b = today.weekday # Проверяет день месяца
    if b == 28 :
            channel = await bot.fetch_channel(926201516963029014)#Вместо этого числа вписать айди своего канала
            await channel.send('Скоро получение ЗП')
    else :
        pass

@tasks.loop(hours = 18.0 )
async def sob():
    c = today.weekday() # Проверяет день недели
    if c == 5 or c == 6 :
        channel = await bot.fetch_channel(926201516963029014)#Вместо этого числа вписать айди своего канала
        await channel.send('Сегодня будет собрание')
    else :
        pass


auto_send.start()
zp_send.start()
sob.start()
bot.run(TOKEN)