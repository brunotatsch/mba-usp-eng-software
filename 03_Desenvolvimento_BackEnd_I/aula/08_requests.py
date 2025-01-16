import requests

response = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
data = response.json()
# print(data["USDBRL"]["bid"])
dollar_exchange_rate = float(data["USDBRL"]["bid"])
print(f"Dolar Exchance Rate of dollar: R$ {dollar_exchange_rate:.2f}")
