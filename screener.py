import get_data
import csv
import time
import random
from termcolor import colored

def bot_bollinger_screener():
    all_stocks = []

    with open('data/nyse_stocks.csv','rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[5] != 'n/a':
                all_stocks.append(row.pop(0))

    print len(all_stocks)
    random.shuffle(all_stocks)  #shuffle so that it selects stocks in random order

    for stock in all_stocks:
        try:
            bands = get_data.bollinger_bands(stock)
        except KeyError:
            print colored(stock, 'red')
            continue

        current_time = time.strftime("%Y-%m-%d %H:%M:00")
        yesterday = '2017-07-03'

        if current_time in bands:
            print stock, current_time
            current_bands = bands[time.strftime("%Y-%m-%d %H:%M:00")]
        elif yesterday in bands:
            print stock, yesterday
            current_bands = bands[yesterday]
        else:
            continue


        bottom_band = float(current_bands['Real Lower Band'])
        price = get_data.get_price(stock)


        difference = price * .02 # alert if price is within 2% of bottom band
        if price - difference < bottom_band:
            print colored('MATCH: ', 'green'), stock, price, bottom_band

if __name__ == "__main__":
    bot_bollinger_screener()
