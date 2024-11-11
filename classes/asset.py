# We will define the class asset for predictive purposes. The client chooses the asset


class Asset:

    def __init__(self, name, ticker, time):
        self.name = name  # name of the asset
        self.ticker = ticker  # ticker symbol
        self.time = time  # amount of years we want to track back

