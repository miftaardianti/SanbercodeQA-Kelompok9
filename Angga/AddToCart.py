import time
import unittest
from data import DataUser
from selenium import webdriver 
from element import Element, Element
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class AddToCartTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "https://www.demoblaze.com/"
    

    #TC-001 Memasukan product ke Cart dengan login
    def test_1(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(3)
        driver.find_element(By.XPATH, Element.Login).click()
        time.sleep(3)
        driver.find_element(By.ID, Element.User).send_keys(DataUser.username)
        driver.find_element(By.ID, Element.Pass).send_keys(DataUser.password)
        driver.find_element(By.XPATH, Element.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, Element.SamsungS6).click()
        time.sleep(5)
        driver.find_element(By.XPATH, Element.AddCart).click()
        time.sleep(5)
        driver.switch_to.alert.accept()
        driver.find_element(By.XPATH, Element.Cart).click()
        time.sleep(5)

        

    #TC-002 Memasukan product ke Cart tanpa login
    def test_2(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(3)
        driver.find_element(By.XPATH, Element.NokiaLumia).click()
        time.sleep(5)
        driver.find_element(By.XPATH, Element.AddCart).click()
        time.sleep(5)
        driver.switch_to.alert.accept()
        driver.find_element(By.XPATH, Element.Cart).click()
        time.sleep(10)

    #TC-003 - TC-005 Kesesuaian Nama, Harga dan Deskripsi pada Cart Page dan Home Page
    def test_3(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(3)
        driver.find_element(By.XPATH, Element.Login).click()
        time.sleep(3)
        driver.find_element(By.ID, Element.User).send_keys(DataUser.username)
        driver.find_element(By.ID, Element.Pass).send_keys(DataUser.password)
        driver.find_element(By.XPATH, Element.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, Element.Cart).click()
        time.sleep(5)
        driver.find_element(By.XPATH, Element.Homepage).click()
        time.sleep(3)
        driver.find_element(By.XPATH, Element.SamsungS6).click()
        time.sleep(5)

    #TC-006 Hapus product dari cart page
    def test_4(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(3)
        driver.find_element(By.XPATH, Element.Login).click()
        time.sleep(3)
        driver.find_element(By.ID, Element.User).send_keys(DataUser.username)
        driver.find_element(By.ID, Element.Pass).send_keys(DataUser.password)
        driver.find_element(By.XPATH, Element.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, Element.Cart).click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='tbodyid']/tr/td[4]/a").click()
        time.sleep(5)


if __name__ == "__main__":
     unittest.main()