import asyncio
import alphavantage


client = alphavantage.Stock('AC08TL1JSK9Q6YUH')

loop = asyncio.get_event_loop()
data = loop.run_until_complete(client.daily_adjusted('GDDY'))
loop.close()

print(data)
