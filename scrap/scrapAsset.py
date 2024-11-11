from classes.driver import Driver
from classes.asset import Asset

driver = Driver("https://finance.yahoo.com/")


asset = Asset("BITCOIN", "BTC-USD", 5)

driver.accept_cookies()
driver.search_for_asset(asset)

