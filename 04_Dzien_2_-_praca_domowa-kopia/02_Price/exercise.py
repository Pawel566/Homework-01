class Price23Vat:
    def __init__(self, prize_brutto):
        self._pretax = prize_brutto
        self._net = self._pretax / 1.23
        self._tax = self._pretax - self._net

    def get_net(self):
        return self._net

    def get_pretax(self):
        return self._pretax

    def get_tax(self):
        return self._tax

    def set_net(self, value):
        self._net = value
        self._pretax = self.net * 1.23
        self._tax = self._pretax - self._net

    def set_pretax(self, value):
        self._pretax = value
        self._net = self._pretax / 1.23
        self._tax = self._pretax - self._net

    def set_tax(self, value):
        self._tax = value
        self._pretax = self._tax * 0.23
        self._net = self._pretax / 1.23

price_1 = Price23Vat(450)
print(price_1.get_net())
print(price_1.get_tax())
print(price_1.get_pretax())

price_2 = Price23Vat(123)
print(price_2.get_net())
print(price_2.get_tax())
print(price_2.get_pretax())
