import ccxt
from decouple import config
import asyncio
import aiohttp
from bs4 import BeautifulSoup

# inicializar exchange con credenciales
binance = ccxt.binance({
    'rateLimit': 3000,
    'enableRateLimit': True,
    'options': {
        'adjustForTimeDifference': True,
    },
    'apiKey': config('TOKEN_BINANCE_PUBLIC'),
    'secret': config('TOKEN_BINANCE_PRIVATE'),
})


# obtener ticker de BTC/USDT
async def show_ticker(cripto:str):
    ticker = await binance.fetch_ticker(cripto)
    return ticker

async def main():
    async with aiohttp.ClientSession() as resp:
        async with resp.get('https://api.binance.com/api/v3/ticker/price') as t:
            text = await t.read()
    return BeautifulSoup(text, 'html.parser')

async def xd():
    obj_bs = await main()
    for i in obj_bs:
        for j in i:
            print(j)


asyncio.run(xd())
     

#LUGAR DE DONDE ENCONTRA LOS PARES DE CRIPTO MONEDAS
"https://www.binance.com/es/markets/spot"

