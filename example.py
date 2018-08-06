import alphavantage

client = alphavantage.AlphaVantage('')
client.get_data('TIME_SERIES_DAILY', 'MSFT')
