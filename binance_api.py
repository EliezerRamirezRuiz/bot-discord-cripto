import aiohttp
import asyncio

async def get_price(session, symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    async with session.get(url) as response:
        data = await response.json()
        return data["price"]

async def get_info_cripto(symbol):
    async with aiohttp.ClientSession() as session:
        price = await get_price(session, symbol) 
        print(f"El precio actual de {symbol} es {price}")
        obj = [symbol, price]
        return obj



