from discord.ext import commands
from decouple import config
from data_api_binance import *

import discord
import logging
  

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config('PREFIX'), intents=intents, help_command=None)



@bot.event
async def on_ready():
    print('puta')


@bot.command()
async def ticker(ctx, cripto):
    """ here we use show_ticker from data_api_binance """
    message = show_ticker(cripto)
    await ctx.send(message)


@bot.command()
async def info_cripto(ctx, cripto:str):
    try:
        data = await get_info_cripto(cripto)
        await ctx.send(f"Cripto: {data[0]}\n Valor: {data[1]}")
    except:
        await ctx.send("Cripto not found")


@bot.command()
async def get_names_cripto(ctx):
    try:
        message = discord.Embed(title="Hello User",
                          url='https://api.binance.com/api/v3/ticker/price',
                          description="what's going on",
                          color=1)
        
        """convert_message_embed("Names cripto","https://api.binance.com/api/v3/ticker/price",
        "Url to looking for symbol to consult with orden function","Functions to use","info_cripto and others",
        "message: Shatterd bot")"""
        await ctx.send(message=message)
    except:
        await ctx.send('XD')


@bot.command()
async def hello(ctx):
    embed = discord.Embed(title="Hello User",
                          url='https://api.binance.com/api/v3/ticker/price',
                          description="what's going on",
                          color=1)
    embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", 
                     icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg")
    embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=True)
    embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=True)
    embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")
    await ctx.send(embed=embed)


# LUGAR DE DONDE ENCONTRA LOS PARES DE CRIPTO MONEDAS
"""
https://www.binance.com/es/markets/spot
https://api.binance.com/api/v3/ticker/price
"""


def main():
    try:
        return bot.run(config('TOKEN_BOT'))
    except:
        logging.info('error')


if __name__ == '__main__':
    main()
    