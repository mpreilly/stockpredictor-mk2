import urllib2
import simplejson as json
import pprint

pp = pprint.PrettyPrinter(indent=4)

def closes(symbol):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=Z1HX9VZ4L9F3YCI2' % symbol
    response = urllib2.urlopen(url)
    data = json.load(response)

    closes = []

    days = data["Time Series (Daily)"] # dict mapping each day to info
    pp.pprint(days)

    for key in sorted(days.keys()):
        closes.append(float(days[key]['4. close']))

    pp.pprint(closes)
    # return closes


def bollinger_bands(symbol, time_period=10):
    url = 'https://www.alphavantage.co/query?function=BBANDS&symbol=%s&interval=daily&time_period=%r&series_type=close&nbdevup=3&nbdevdn=3&apikey=Z1HX9VZ4L9F3YCI2' % (symbol,time_period)
    print url
    response = urllib2.urlopen(url)
    json_data = response.read()

    # A dict where each key is the date and the value is a dict of bot, mid, top
    data = json.loads(json_data)

    yesterdaybands = data['Technical Analysis: BBANDS']['2017-06-19']
    pp.pprint(yesterdaybands)
