from discord.ext import commands
from decouple import config
from functions import *

import discord
import logging
  

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config('PREFIX'), intents=intents, help_command=None)


@bot.command()
async def ticker(ctx, cripto):
    """ here we use show_ticker from data_api_binance """
    message = show_ticker(cripto)
    await ctx.send(message)


@bot.command()
async def info_cripto(ctx, cripto:str):
    try:
        data = await get_info_cripto(cripto)
        await ctx.send(f"Cripto: {data[0]}\nValor: {data[1]}")
    except:
        await ctx.send("Cripto not found")


@bot.command()
async def get_names_cripto(ctx):
    try:
        await write('text.txt')
        await asyncio.sleep(1)
        await ctx.send(file=discord.File("text.txt"))
    except:
        await ctx.send("XD")
    finally:
        await truncate('text.txt')

@bot.command()
async def price_cripto(ctx, cripto:str):
    try:
        cripto = await get_price(cripto)
        await ctx.send(cripto)
    except:
        await ctx.send("Cripto not found, please seek the symbol available")


def main():
    return bot.run(config('TOKEN_BOT'))



if __name__ == '__main__':
    main()
    