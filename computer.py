class puter:

    def __init__(self):
        self.__pricemax= 900

    def sell(self):
        print("selling price{}".format(self.__pricemax))

    def setting(self, price):
        self.__pricemax =price

a=puter()
a.sell()

a.__pricemax=1000
a.sell()

a.setting (1000)
a.sell()
        