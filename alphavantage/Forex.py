import aiohttp
from typing import Dict


class Forex():

    def __init__(self, api_key: str):
        self._api_key = api_key
        self.base_url = 'https://www.alphavantage.co/query'

    async def _get_data_response(
            self, function: str, from_currency: str, to_currency: str, interval: str, output_size: str, data_type: str, xchg: bool) -> str:
        self._validate_params(function, from_currency, to_currency)
        params = self._create_params(function, from_currency, to_currency, interval, output_size, data_type, xchg)

        print(params)

        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url, params=params) as response:
                return await response.text()

    def _validate_params(self, function: str, from_currency: str, to_currency: str):
        if function is None or len(function) == 0:
            raise Exception('Invalid parameter `function`.')
        if from_currency is None or len(from_currency) == 0:
            raise Exception('Invalid parameter `from_currency`.')
        if to_currency is None or len(to_currency) == 0:
            raise Exception('Invalid parameter `to_currency`.')

    def _create_params(
            self, function: str, from_currency: str, to_currency: str, interval: str, output_size: str, data_type: str, xchg: bool) -> Dict[str, str]:
        params = {
            'function': function,
            'apikey': self._api_key
        }

        if xchg:
            params['from_currency'] = from_currency
            params['to_currency'] = to_currency
        else:
            params['from_symbol'] = from_currency
            params['to_symbol'] = to_currency

        if interval is not None and len(interval) > 0:
            params['interval'] = interval
        if output_size is not None and len(output_size) > 0:
            params['outputsize'] = output_size
        if data_type is not None and len(data_type) > 0:
            params['datatype'] = data_type
        if data_type is not None and len(data_type) > 0:
            params['datatype'] = data_type
        if data_type is not None and len(data_type) > 0:
            params['datatype'] = data_type

        return params

    async def exchange_rate(self, from_currency: str, to_currency: str) -> str:
        return await self._get_data_response('CURRENCY_EXCHANGE_RATE', from_currency, to_currency, None, None, None, True)

    async def intraday(self, from_currency: str, to_currency: str, interval_minutes=60, output_size='compact', data_type='json') -> str:
        return await self._get_data_response(
            'FX_INTRADAY', from_currency, to_currency, str(interval_minutes) + 'min', output_size, data_type, False)

    async def daily(self, from_currency: str, to_currency: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response(
            'FX_DAILY', from_currency, to_currency, None, output_size, data_type, False)

    async def weekly(self, from_currency: str, to_currency: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response(
            'FX_WEEKLY', from_currency, to_currency, None, output_size, data_type, False)

    async def monthly(self, from_currency: str, to_currency: str, output_size='compact', data_type='json') -> str:
        return await self._get_data_response(
            'FX_MONTHLY', from_currency, to_currency, None, output_size, data_type, False)
