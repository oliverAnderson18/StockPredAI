from classes.driver import Driver
from userInput import asset
import time

driver = Driver("https://finance.yahoo.com/")

driver.accept_cookies()
driver.search_for_asset(asset)
time.sleep(5)
driver.search_historical_data(asset)
