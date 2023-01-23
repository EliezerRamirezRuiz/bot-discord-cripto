from discord.ext import commands
from decouple import config
from binance_api import *

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
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def info_cripto(ctx, cripto:str):
    try:
        data = await get_info_cripto(cripto)
        await ctx.send(f"Cripto: {data[0]} \n Valor: {data[1]}")
    except:
        await ctx.send(f"sir, that cripto is not available. if you want to know what cripto you want to know, put !help")


@bot.command()
async def hello(ctx):
    embed = discord.Embed(title="Hello User",
                          url='https://www.google.com',
                          description="what's going on",
                          color=1)
    embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", 
                     icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg")
    
    embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
    embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=False)
    embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=True)
    embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=True)
    embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")
    await ctx.send(embed=embed)





def main():
    try:
        return bot.run(config('TOKEN_BOT'))
    except:
        logging.info('error')


if __name__ == '__main__':
    main()
    