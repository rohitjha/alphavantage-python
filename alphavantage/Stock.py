import aiohttp


class Stock():

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = 'https://www.alphavantage.co/query'

    async def _get_data_response(self, function: str, symbol: str, interval: str, output_size: str, data_type: str) -> str:
        self._validate_params(function, symbol, data_type)

        params = {
            'function': function,
            'symbol': symbol,
            'datatype': data_type,
            'apikey': self.api_key
        }

        if interval is not None and len(interval) > 0:
            params['interval'] = interval
        if output_size is not None and len(output_size) > 0:
            params['outputsize'] = output_size

        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url, params=params) as response:
                return await response.text()

    def _validate_params(self, function, symbol, data_type):
        if function is None or len(function) == 0:
            raise Exception('Invalid parameter `function`.')
        if symbol is None or len(symbol) == 0:
            raise Exception('Invalid parameter `symbol`.')
        if data_type not in ['json', 'csv'] and data_type is not None:
            raise Exception(
                'Invalid parameter `data_type`. Acceptable values are `json` and `csv`.')

    async def intraday(self, symbol: str, interval_minutes=60, output_size='compact', data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_INTRADAY', symbol, str(interval_minutes) + 'min', output_size, data_type)

    async def daily(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_DAILY', symbol, None, output_size, data_type)

    async def daily_adjusted(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_DAILY_ADJUSTED', symbol, None, output_size, data_type)

    async def weekly(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_WEEKLY', symbol, None, output_size, data_type)

    async def weekly_adjusted(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_WEEKLY_ADJUSTED', symbol, None, output_size, data_type)

    async def monthly(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_MONTHLY', symbol, None, output_size, data_type)

    async def monthly_adjusted(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_MONTHLY_ADJUSTED', symbol, None, output_size, data_type)

    async def batch_quotes(self, symbol: str, data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_MONTHLY_ADJUSTED', symbol, None, None, data_type)
