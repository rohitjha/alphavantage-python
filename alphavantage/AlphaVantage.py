import aiohttp
import asyncio


class AlphaVantage:
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://www.alphavantage.co/query'


    async def _get_data(self, function, symbol, output_size, data_type):
        params = {
            'function': function,
            'symbol': symbol,
            'outputsize': output_size,
            'datatype': data_type,
            'apikey': self.api_key
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url, params=params) as response:
                return await response.text()


    def get_data(self, function, symbol, output_size='compact', data_type='json'):
        loop = asyncio.get_event_loop()
        data = loop.run_until_complete(self._get_data(function, symbol, output_size, data_type))
        loop.close()
        return data
