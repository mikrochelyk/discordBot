import discord
from discord.ext import commands
from config import settings
import requests

class MyClient(discord.Client):
    async def on_ready(self):
        print('{0}' ' ...Going dark.'.format(self.user)) #выводит сообщение и показывает, что бот активен

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message)) #отслеживает и выводит сообщения юзеров из канала в программу

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Hi, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена

bot = commands.Bot(command_prefix = settings['prefix'])

async def slyva(ctx):
    response = requests.get('https://image.shutterstock.com/z/stock-photo-berlin-germany-september-luxury-estate-car-bmw-series-e-in-the-city-street-1662104107.jpg') #get-запрос
    json_data = response.json()

    embed = discord.Embed(color = 0xff9900, title = 'My brother') #создание Embed'a
    embed.set.image(url = json_data['link']) #Устанавливаем картинку embed'a
    await ctx.send(embed = embed)