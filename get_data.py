import urllib2
import simplejson as json
import pprint
import time

pp = pprint.PrettyPrinter(indent=4)

def closes(symbol, full_output=True):
    if full_output:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=Z1HX9VZ4L9F3YCI2' % symbol
    else:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&apikey=Z1HX9VZ4L9F3YCI2' % symbol
    response = urllib2.urlopen(url)
    data = json.load(response)

    closes = []

    days = data["Time Series (Daily)"] # dict mapping each day to info
    # pp.pprint(days)

    for key in sorted(days.keys()):
        closes.append(float(days[key]['4. close']))

    return closes

def get_price(symbol):
    close_list = closes(symbol, False)
    price = close_list[-1]  # most recent price is last element in list
    return price

def bollinger_bands(symbol, time_period=10):
    url = 'https://www.alphavantage.co/query?function=BBANDS&symbol=%s&interval=daily&time_period=%r&series_type=close&nbdevup=3&nbdevdn=3&apikey=Z1HX9VZ4L9F3YCI2' % (symbol,time_period)
    response = urllib2.urlopen(url)
    json_data = response.read()

    # A dict where each key is the date and the value is a dict of bot, mid, top
    data = json.loads(json_data)
    return data['Technical Analysis: BBANDS']
