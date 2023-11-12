class Price:
    def __init__(self, value: float):
        if not isinstance(value, float):
            value = float(value)
        self.value = round(value, 2)


    def from_eur(self, amount: float):
        return Price(amount * 4.5)

    def from_usd(self, amount: float):
        return Price(amount * 3.8)

    def __str__(self):
        return f"{self.value:.2f} PLN"

result = Price(0)

some_price = result.from_usd(25)
some_other_price = result.from_eur(80)
print(some_price)
print(some_other_price)