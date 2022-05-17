class Mint:
    present_year = 2021

    def __init__(self):
        self.update()

    def create(self, coin):
        "*** YOUR CODE HERE ***"
        return coin(self.year)

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = self.present_year


class Coin:
    cents = None  # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        return self.cents + max(0,Mint.present_year-self.year-50)


class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10

mint = Mint()
mint.year
dime = mint.create(Dime)
dime.year
Mint.present_year = 2101  # Time passes
nickel = mint.create(Nickel)
nickel.year     # The mint has not updated its stamp yet
nickel.worth()  # 5 cents + (80 - 50 years)
