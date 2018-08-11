import aiohttp


class AlphaVantage:

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = 'https://www.alphavantage.co/query'

    async def get_data_response(self, function: str, symbol: str, interval: str, output_size: str, data_type: str) -> str:
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
