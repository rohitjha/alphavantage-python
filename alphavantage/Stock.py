import aiohttp
from typing import List, Dict


class Stock():

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = 'https://www.alphavantage.co/query'

    async def _get_data_response(
            self, function: str, symbol: str, symbols: List[str], interval: str, output_size: str, data_type: str) -> str:
        self._validate_params(function, data_type)
        params = self._create_params(
            function, symbol, symbols, interval, output_size, data_type)

        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url, params=params) as response:
                return await response.text()

    def _validate_params(self, function, data_type):
        if function is None or len(function) == 0:
            raise Exception('Invalid parameter `function`.')
        if data_type not in['json', 'csv'] and data_type is not None:
            raise Exception(
                'Invalid parameter `data_type`. Acceptable values are `json` and `csv`.')

    def _create_params(
            self, function: str, symbol: str, symbols: List[str], interval: str, output_size: str,
            data_type: str) -> Dict[str, str]:
        params = {
            'function': function,
            'datatype': data_type,
            'apikey': self.api_key
        }

        if interval is not None and len(interval) > 0:
            params['interval'] = interval
        if output_size is not None and len(output_size) > 0:
            params['outputsize'] = output_size
        if symbol is not None and len(symbol) > 0:
            params['symbol'] = symbol
        if symbols is not None and len(symbols) > 0:
            params['symbols'] = ','.join(symbols)

        return params

    async def intraday(self, symbol: str, interval_minutes=60, output_size='compact', data_type='json') -> str:
        return await self._get_data_response(
            'TIME_SERIES_INTRADAY', symbol, None, str(interval_minutes) + 'min', output_size, data_type)

    async def daily(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_DAILY', symbol, None, None, output_size, data_type)

    async def daily_adjusted(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_DAILY_ADJUSTED', symbol, None, None, output_size, data_type)

    async def weekly(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_WEEKLY', symbol, None, None, output_size, data_type)

    async def weekly_adjusted(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_WEEKLY_ADJUSTED', symbol, None, None, output_size, data_type)

    async def monthly(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_MONTHLY', symbol, None, None, output_size, data_type)

    async def monthly_adjusted(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response('TIME_SERIES_MONTHLY_ADJUSTED', symbol, None, None, output_size, data_type)

    async def batch_quotes(self, symbols: list, data_type='json') -> str:
        return await self._get_data_response('BATCH_STOCK_QUOTES', None, symbols, None, None, data_type)
