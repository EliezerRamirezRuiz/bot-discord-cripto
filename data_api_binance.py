import aiohttp
import ccxt
import asyncio
from discord import Embed


"""
api_key = config('TOKEN_BINANCE_PUBLIC')
secret_key = config('TOKEN_BINANCE_PRIVATE')
"""

binance = ccxt.binance({
    'rateLimit': 1000,  # unified exchange property
    'enableRateLimit': True,
    'options': {
        'adjustForTimeDifference': True,  # exchange-specific option
    },
})


# Get data with a ticker 
def show_ticker(cripto: str) -> str:
    """This function show values about the ticker, The cripto is string and you
    should pass a string and if you pass other values, this gonna pass a error"""
    try:
        task = binance.fetch_ticker(cripto)
        if task != None:
            ticker = f'''symbol: {task["symbol"]},
                            date time: {task["datetime"]},
                            high: {task["high"]},
                            low: {task["low"]},
                            open: {task["open"]},
                            close: {task["close"]},
                            change: {task["change"]}'''
            return ticker
        
    except TypeError:
        return 'Only string, please try again'

# Function to return a valid json object
async def json_url():
    """
    The function return a json from the https://api.binance.com/api/v3/ticker/price 
    that it'll be used in the function get_keys_cripto to return all keys into the json 
    object
    """
    async with aiohttp.ClientSession() as resp:
        async with resp.get('https://api.binance.com/api/v3/ticker/price') as t:
            text = await t.json()
    return text


# Function to get keys from binance
async def get_keys_cripto(list_cripto=None) -> None:
    """ 
    This function return a list of keys about the ticker that we are ask
    to the url with the aiohttp.ClientSession from the json_url. 
    The principal purpose is help to the users or developers that wants to use
    the cripto_bot. 
    """

    error_cripto = """Sorry something went wrong,
        please try again or contact the administrator"""

    if list_cripto is None:
        list_cripto = []
        try:
            values_cripto = await json_url()

            for i in values_cripto:
                list_cripto.append(i['symbol'])

            return list_cripto

        except:
            return error_cripto


# Function get price
async def get_price(symbol):
    """
    Function basic to get the price of a ticker and nothing else
    """
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                return data["price"]
    except:
        return """we couldn't get the price,
                check if the coin is available"""


# Function get data 
async def get_info_cripto(symbol:str) -> list:
    """
    Function to get information about a ticker from binance
    so basic, is diferrent that use the library ccxt
    """
    try:
        price = await get_price(symbol) 
        print(f"El precio actual de {symbol} es {price}")
        obj = [symbol, price]
        print(obj)
        return obj
        
    except TypeError:
        return 'only string'


# Function convert async
async def convert_string(a) -> str:
    obj = await a
    b = " ".join(obj)
    return b


# Function normal
def convert_message_embed(Title:str, Url:str|None, Description:str, Name:str|None, Value:str|None, Text:str|None):
    """Function to create a message embed with paremeters so basic"""
    message = Embed(title=Title, url=Url,
                    description=Description, color=1)
    message.add_field(name=Name, value=Value, inline=False)
    message.set_footer(text=Text)

    return message
