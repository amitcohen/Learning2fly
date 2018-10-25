import re
import urllib
import urllib.request

list = ['FB', 'GOOG', 'BABA', 'AAPL', 'MSFT', 'TSLA', 'NVDA', 'AMD', 'EBAY', 'AMZN', 'TWTR', 'BA']
URL = 'https://www.nasdaq.com/symbol/'

for stock in list:
    stock_url = URL + stock
    GetHtmal = urllib.request.urlopen(stock_url).read()
    DecodeHtml = GetHtmal.decode("utf-8")

    search_results = re.search('<div id="qwidget_lastsale" class="qwidget-dollar">', DecodeHtml)
    #print(search_results)
    start = search_results.end()
    end = start + 7
    price = DecodeHtml[start:end]
    price2 = price.replace("<", "")
      
    print(stock + ': ' + price2)

#str.replace("is", "was")
'''
URL = 'https://www.nasdaq.com/symbol/GOOG'
GetHtmal = urllib.request.urlopen(URL).read()
DecodeHtml = GetHtmal.decode("utf-8")
#print(DecodeHtml)

search_results = re.search('<div id="qwidget_lastsale" class="qwidget-dollar">', DecodeHtml)
print(search_results)
start = search_results.end()
end = start + 7
##print('start= ', start)
##print('end= ', end)

price = DecodeHtml[start:end]
print(price, 'Closing price: ', price)
'''