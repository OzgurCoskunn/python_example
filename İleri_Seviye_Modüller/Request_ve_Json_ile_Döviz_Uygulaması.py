#import requests

#import sys
#url = "http://api.fixer.io/latest?base="

#birinci_doviz = input("Birinci Döviz:")
#ikinci_döviz = input("İkinci Döviz:")
#miktar = float(input("Miktar:"))


#response = requests.get(url + birinci_doviz)

#json_verisi = response.json()
#try:
#    print(json_verisi["rates"][ikinci_döviz] * miktar)
#except KeyError:
#    sys.stderr.write("Lütfen para birimlerini doğru girin")
#    sys.stderr.flush()

#************************ api key geldi **************************
import requests

url = "https://api.apilayer.com/fixer/latest?base=USD&symbols=EUR,GBP"

payload = {}
headers = {
  "apikey": "5MzCGWH4aWuwx893Kyzv2D7s4QWhQIb6"
}


response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)



