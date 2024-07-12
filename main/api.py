import requests


def get_currency_rate(base_currency, target_currency):
    api_key = "6ed686216c64fb792432da78"
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'].get(target_currency, None)
