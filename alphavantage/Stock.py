from .AlphaVantage import AlphaVantage


class Stock(AlphaVantage):

    def __init__(self, api_key):
        super().__init__(api_key)

    async def intraday(self, symbol: str, interval_minutes=60, output_size='compact', data_type='json') -> str:
        return await self.get_data_response('TIME_SERIES_INTRADAY', symbol, str(interval_minutes) + 'min', output_size, data_type)

    async def daily(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self.get_data_response('TIME_SERIES_DAILY', symbol, None, output_size, data_type)

    async def daily_adjusted(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self.get_data_response('TIME_SERIES_DAILY_ADJUSTED', symbol, None, output_size, data_type)

    async def weekly(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self.get_data_response('TIME_SERIES_WEEKLY', symbol, None, output_size, data_type)

    async def weekly_adjusted(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self.get_data_response('TIME_SERIES_WEEKLY_ADJUSTED', symbol, None, output_size, data_type)

    async def monthly(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self.get_data_response('TIME_SERIES_MONTHLY', symbol, None, output_size, data_type)

    async def monthly_adjusted(self, symbol: str, output_size='compact', data_type='json') -> str:
        return await self.get_data_response('TIME_SERIES_MONTHLY_ADJUSTED', symbol, None, output_size, data_type)

    async def batch_quotes(self, symbol: str, data_type='json') -> str:
        return await self.get_data_response('TIME_SERIES_MONTHLY_ADJUSTED', symbol, None, None, data_type)
