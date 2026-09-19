import requests
import time
from cachetools import cached, TTLCache
cache = TTLCache(maxsize=100 ,ttl=300)

@cached(cached)
def get_exchange_rate(base_currency, target_currency):
    time.sleep(2)
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()['rates'][target_currency]


def convert_currency(amount,exchange_rate):
    return amount * exchange_rate

if __name__ == "__main__":
    base_currency = input("Enter the base currency (e.g., USD): ").strip().upper()
    target_currency = input("Enter the target currency (e.g., CAD): ").strip().upper()
    amount = float(input(f"Enter the amount in {base_currency}: "))
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    usd_amount = 100
    cad_amount = usd_amount * exchange_rate
    print(f"{amount} {base_currency} = {cad_amount:.2f} {target_currency}")
