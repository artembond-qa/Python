from selenium.webdriver.common.by import By


class HomePage:


    def __init__(self, browser):
        self.driver = browser


    def open(self):
        self.driver.get("https://www.demoblaze.com/")

    def click_nexus6(self):
        Nexus6 = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Nexus 6')]")
        Nexus6.click()

    def click_monitor(self):
        monitor_link = self.driver.find_element(By.LINK_TEXT, "Monitors")
        monitor_link.click()

    def check_products_count(self, count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, ".card")
        assert len(monitors) == count