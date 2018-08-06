import alphavantage

client = alphavantage.AlphaVantage('')
data = client.get_data('TIME_SERIES_DAILY', 'MSFT')
print(data)
