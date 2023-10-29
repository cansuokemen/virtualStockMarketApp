import time
from random import random
from random import randint


class Stock:
    stockCode = "TATEN"
    stockName = "Tatlıpınar Enerji A.Ş"
    lastPrice = 39.36
    livePrice = lastPrice


def calculate_min(stock_object: Stock):
    min_val = stock_object.lastPrice * 0.9
    return min_val


def calculate_max(stock_object: Stock):
    max_val = stock_object.lastPrice * 1.1
    return max_val




stock = Stock()

print(f"Hisse fiyatı {stock.lastPrice}")
print(f"Hisse tavan fiyatı {calculate_max(stock)}")
print(f"Hisse taban fiyatı {calculate_min(stock)}")


while True:
    possibility = randint(0, 1)
    if possibility == 0:
        stock.livePrice += random() / 1.7
    else:
        stock.livePrice -= random() / 1.7
    time.sleep(0.3)
    print(round(stock.livePrice, 2))

    if stock.livePrice > calculate_max(stock):
        print(f"Hisse: {stock.stockCode} TAVAN Yaptı")
        break
    elif stock.livePrice < calculate_min(stock):
        print(f"Hisse: {stock.stockCode} TABAN Yaptı")
        break
