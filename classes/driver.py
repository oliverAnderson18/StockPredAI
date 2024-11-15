from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from classes.asset import Asset
import time


class Driver:

    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.url = url

    def accept_cookies(self) -> None:
        self.driver.get(self.url)
        time.sleep(5)

        # We click the scroll button
        scrollDown = self.driver.find_element(By.ID, "scroll-down-btn")
        scrollDown.click()

        time.sleep(5)
        # We click the accept cookies button
        acceptCookies = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/form/div[2]/div[2]/button[1]")
        acceptCookies.click()

    def search_for_asset(self, asset: Asset) -> None:
        searchBar = self.driver.find_element(By.ID, "ybar-sbq")
        searchBar.click()

        # Now we will search for the asset by its ticker symbol

        searchBar.send_keys(asset.ticker)
        searchBar.send_keys(Keys.ENTER)

    def search_historical_data(self, asset: Asset) -> None:
        historicalData = self.driver.find_element(By.XPATH,
                                                  "/html/body/div[2]/main/section/section/aside/section/nav/ul/li[5]/a/span")
        historicalData.click()

        # Now we will click how long back we want to track

        datesButton = self.driver.find_element(By.XPATH,
                                               "/html/body/div[2]/main/section/section/section/article/div[1]/div[1]/div[1]/button/span")
        datesButton.click()

        # And we choose how far back we want to track

        date = self.driver.find_element(By.CSS_SELECTOR, "button[value='" + asset.time + "']")
        date.click()
