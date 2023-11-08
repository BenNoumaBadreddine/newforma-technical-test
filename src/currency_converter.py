
class CurrencyConverter:
    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency != to_currency:
            if from_currency in self.exchange_rates and to_currency in self.exchange_rates:

                return amount * self.exchange_rates[to_currency] / self.exchange_rates[from_currency]
            else:
                raise ValueError(f"Invalid currency codes {from_currency}.")
        return amount

    def set_exchange_rate(self, currency_code, exchange_rate):
        self.exchange_rates[currency_code] = exchange_rate

    def get_exchange_rate(self, currency_code):
        if currency_code in self.exchange_rates:
            return self.exchange_rates[currency_code]
        else:
            raise ValueError("Exchange rate not found for the currency code.")

