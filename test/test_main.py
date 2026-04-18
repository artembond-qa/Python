from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from pages.homepage import HomePage
from pages.product import ProductPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()




def test_open_Nexus6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_nexus6()
    product_page = ProductPage(driver)
    product_page.check_title_is("Nexus 6")


def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    # driver.get("https://www.demoblaze.com/")
    homepage.click_monitor()
    # monitor_link = driver.find_element(By.LINK_TEXT, "Monitors")
    # monitor_link.click()
    time.sleep(2)
    homepage.check_products_count(2)
    # monitors = driver.find_elements(By.CSS_SELECTOR, ".card")
    # assert len(monitors) == 2