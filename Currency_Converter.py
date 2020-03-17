#Currency Converter - www.101computing.net/currency-converter/
import json, urllib

#See full lists of valid currencies on https://free.currencyconverterapi.com/api/v6/currencies
validCurrencies = ["EUR","GBP","USD","JPY"]

#Requires an API key, ask for it here: https://free.currencyconverterapi.com/free-api-key

#For example for me:
API_key = "c94e9961dac0ab6dfc22"

#Display banner
print("$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€")
print("$£¥€                            $£¥€")
print("$£¥€     Currency Converter     $£¥€")
print("$£¥€                            $£¥€")
print("$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€")
print("")
print("List of currencies: ")
print("  GBP - British Pound £")
print("  JPY - Japanese Yen ¥")
print("  EUR - Euro €")
print("  USD - US Dollar $")
print("")

#Initialise key variables
currencyFrom = ""
currencyTo = ""
amount = 0

#Retrieve user inputs
while not currencyFrom in validCurrencies:
  currencyFrom = input("Enter Currency to convert From: (e.g. GBP)").upper()
  
while not currencyTo in validCurrencies:
  currencyTo = input("Enter Currency to convert To: (e.g. EUR)").upper()

amount = float(input("Enter amount to convert: (e.g. 10.00)"))

#A JSON request to retrieve the required exchange rate
url = "https://free.currencyconverterapi.com/api/v6/convert?q="+currencyFrom + "_" + currencyTo +"&compact=y"+"&apiKey="+API_key

print(url)

response = urllib.urlopen(url)
result = json.loads(response.read())

print(result)
   
   
#Let's extract the required information
exchangeRate=result[currencyFrom + "_" + currencyTo]
rate = exchangeRate["val"]

#Output exchange rate and converted amount
print("")
print("Exchange rate: 1 " + currencyFrom + " = " + str(rate) + " " + currencyTo)
print(str(amount) + " " + currencyFrom + " = " + ("{0:.2f}".format(amount*rate)) + " " + currencyTo)
