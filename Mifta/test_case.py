import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from element import elm
from input import addInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TestPlaceOrder(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "https://www.demoblaze.com/"
 
    #TC_001 
    def test_a_success_btn_place_order(self):
        # steps
        driver = self.browser #buka web browser
        driver.maximize_window()
        driver.get(self.url)
        driver.find_element(By.XPATH, elm.cart).click()
        driver.find_element(By.XPATH, elm.btnPlaceOrder).click()
        time.sleep(1)
        # validasi
        expected_message = "Place order"
        actual_message = driver.find_element(By.XPATH,"/html//h5[@id='orderModalLabel']").text
        self.assertEqual(expected_message,actual_message)
    
    #TC_002
    def test_success_plece_order_add_product_valid_data(self):
        #steps
        driver = self.browser #buka web browser
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
        time.sleep(3)
        driver.find_element(By.XPATH, elm.btnAddCart).click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.find_element(By.XPATH, elm.cart).click()
        driver.find_element(By.XPATH, elm.btnPlaceOrder).click()
        time.sleep(3)
        driver.find_element(By.ID, elm.name).send_keys(addInput.name)
        driver.find_element(By.ID, elm.country).send_keys(addInput.country)
        driver.find_element(By.ID, elm.city).send_keys(addInput.city)
        driver.find_element(By.ID, elm.creditcard).send_keys(addInput.card)
        driver.find_element(By.ID, elm.month).send_keys(addInput.month)
        driver.find_element(By.ID, elm.year).send_keys(addInput.year)
        driver.find_element(By.CSS_SELECTOR, "div#orderModal > div[role='document'] .btn.btn-primary").click()
        # validasi
        expected_message = "Thank you for your purchase!"
        actual_message = driver.find_element(By.XPATH,"//body/div[10]/h2[.='Thank you for your purchase!']").text
        self.assertEqual(expected_message,actual_message)

    #TC_003
    def test_a_success_place_order_no_add_product_valid_data(self):
        # steps
        driver = self.browser #buka web browser
        driver.maximize_window()
        driver.get(self.url)
        driver.find_element(By.XPATH, elm.cart).click()
        driver.find_element(By.XPATH, elm.btnPlaceOrder).click()
        time.sleep(3)
        driver.find_element(By.ID, elm.name).send_keys(addInput.name)
        driver.find_element(By.ID, elm.country).send_keys(addInput.country)
        driver.find_element(By.ID, elm.city).send_keys(addInput.city)
        driver.find_element(By.ID, elm.creditcard).send_keys(addInput.card)
        driver.find_element(By.ID, elm.month).send_keys(addInput.month)
        driver.find_element(By.ID, elm.year).send_keys(addInput.year)
        driver.find_element(By.CSS_SELECTOR, "div#orderModal > div[role='document'] .btn.btn-primary").click()
        time.sleep(3)
        # validasi
        expected_message = "Thank you for your purchase!"
        actual_message = driver.find_element(By.XPATH,"//body/div[10]/h2[.='Thank you for your purchase!']").text
        self.assertEqual(expected_message,actual_message)
    
    #TC_004
    def test_plece_order_add_product_blank_form(self):
        #steps
        driver = self.browser #buka web browser
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
        time.sleep(3)
        driver.find_element(By.XPATH, elm.btnAddCart).click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.find_element(By.XPATH, elm.cart).click()
        driver.find_element(By.XPATH, elm.btnPlaceOrder).click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "div#orderModal > div[role='document'] .btn.btn-primary").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
    
    #TC_005
    def test_success_plece_order_add_product_blank_creditcard(self):
        #steps
        driver = self.browser #buka web browser
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
        time.sleep(3)
        driver.find_element(By.XPATH, elm.btnAddCart).click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.find_element(By.XPATH, elm.cart).click()
        driver.find_element(By.XPATH, elm.btnPlaceOrder).click()
        time.sleep(3)
        driver.find_element(By.ID, elm.name).send_keys(addInput.name)
        driver.find_element(By.ID, elm.country).send_keys(addInput.country)
        driver.find_element(By.ID, elm.city).send_keys(addInput.city)
        driver.find_element(By.ID, elm.month).send_keys(addInput.month)
        driver.find_element(By.ID, elm.year).send_keys(addInput.year)
        driver.find_element(By.CSS_SELECTOR, "div#orderModal > div[role='document'] .btn.btn-primary").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)



    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()