import json
import requests
import re, datetime
import AlphaRequestsFunctions 

# Functions below

tickerInput = input("What ticker do you want to check today?").upper() 

actionInput = input("What would you like to do? \n1. Get the latest Quote \n2. Check last high price \n")

if actionInput == '1':
    a = AlphaRequestsFunctions.AlphaRequests(tickerInput)
    quotePrice = a.getQuoteLatest()
    print("Stock: " + tickerInput + "\nPrevious close price: " + quotePrice["08. previous close"] + "\nLast refreshed: " + quotePrice["07. latest trading day"])
if actionInput == '2':
    a = AlphaRequestsFunctions.AlphaRequests(tickerInput)
    todayPrice = a.getTodayHighPrice()

    if isinstance(todayPrice, str):
        print("Issue with stock symbol provied")
    else:
        print("Stock: " + tickerInput + "\nHigh price: " + todayPrice["price"] + "\nLast refreshed: " + todayPrice["time"])


