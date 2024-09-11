from locale import currency
from sqlite3 import converters

import requests
from bs4 import BeautifulSoup
import time


class Currency:
    DOLLAR_BYN = 'https://finance.rambler.ru/calculators/converter/1-USD-BYN/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36'}

    current_converted_price = 0
    difference = 0.2

    def __init__(self):
        self.current_converted_price = float(self.get_currency_price().replace(',', '.'))

    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_BYN, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll('span', {'class': 'x9LZBMwk'})
        return convert[1].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(',', '.'))
        if currency >= self.current_converted_price + self.difference:
            print('Курс доллара сильно вырос')
        elif currency <= self.current_converted_price - self.difference:
            print('Курс доллара сильно упал')
        print('Курс доллара: 1$ = ' + str(currency))

        time.sleep(3)
        self.check_currency()


currency = Currency()
currency.check_currency()
