import asyncio
import alphavantage

API_KEY = ''

forex_client = alphavantage.Forex(API_KEY)

loop = asyncio.get_event_loop()
xchg_rate_data = loop.run_until_complete(forex_client.intraday('USD', 'INR'))
loop.close()

print(xchg_rate_data)
