import requests

import requests
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    return response.json()['rates'][target_currency]

def convert_currency(amount,exchange_rate):
    return amount * exchange_rate


if __name__ == "__main__":
    base_currency = input("Enter the base currency (e.g., USD): ")
    target_currency = input("Enter the target currency (e.g., CAD): ")
    amount = float(input(f"Enter the amount in {base_currency}: "))
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = convert_currency(amount, exchange_rate)
    print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency} at an exchange rate of {exchange_rate}.")