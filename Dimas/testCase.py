import pytest
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from element import elem
from data import addData
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # variable data
        self.url = "https://www.demoblaze.com/"
    
    #def tearDown(self):
     ## self.browser.quit()

        #TC_001 Validasi Contact Popup Form
    def test_success_open_popup_form(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        driver.find_element(By.XPATH, elem.menuContact).click()
        time.sleep(1)

        ##VALIDASI
        expected_message = "New message"
        actual_message = driver.find_element(By.XPATH,"//body/div[1]/div/div/div[1]/h5").text
        self.assertEqual(expected_message,actual_message)

         #TC_002 Test send contact with valid data
    def test_verify_submit_contact_valid_format(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuContact).click()
        time.sleep(3)
        driver.find_element(By.ID, elem.cEmail).send_keys(addData.email)
        driver.find_element(By.ID, elem.cIdName).send_keys(addData.nama)
        driver.find_element(By.ID, elem.cIdMessage).send_keys(addData.messages)
        ##driver.find_element(By.XPATH, elem.btnSend).click()
        driver.find_element(
        By.CSS_SELECTOR, "#exampleModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        expectedAlertMessage = "Thanks for the message!!"
        ##time.sleep(10)
        ##Captured Alert Text (Actual Text)
        actualAlertMessage = driver.switch_to.alert.text()
        ##Assertion
        self.assertEquals(expectedAlertMessage, actualAlertMessage)
        ##Accept the alert (Click OK)
        driver.switch_to.alert.accept()


        # try:
        #   response_data = WebDriverWait(driver, 3).until(EC.alert_is_present())
        #   response_text = response_data.text
        #   driver.switch_to.alert.accept()
        #   assert response_text == " Thanks for the messages!!"

        # except:
        #     pytest.fail("Failed")

        #TC_003 Test_Send_message_without_proper_email
    def test_verify_submit_contact_valid_format(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(5)
        driver.find_element(By.XPATH, elem.menuContact).click()
        time.sleep(3)
        driver.find_element(By.ID, elem.cEmail).send_keys("dimas")
        driver.find_element(By.ID, elem.cIdName).send_keys(addData.nama)
        driver.find_element(By.ID, elem.cIdMessage).send_keys(addData.messages)
        ##driver.find_element(By.XPATH, elem.btnSend).click()
        driver.find_element(
        By.CSS_SELECTOR, "#exampleModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        
        ##VALIDASI
        try:
          response_data = WebDriverWait(driver, 3).until(EC.alert_is_present())
          response_text = response_data.text
          driver.switch_to.alert.accept()
          assert response_text == " Please fill in the email correctly!!"

        except:
            pytest.fail("Failed")

            #TC_004 Test_Send_message_without_email
    def test_verify_submit_contact_valid_format(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(5)
        driver.find_element(By.XPATH, elem.menuContact).click()
        time.sleep(3)
        driver.find_element(By.ID, elem.cEmail).send_keys("")
        driver.find_element(By.ID, elem.cIdName).send_keys(addData.nama)
        driver.find_element(By.ID, elem.cIdMessage).send_keys(addData.messages)
        ##driver.find_element(By.XPATH, elem.btnSend).click()
        driver.find_element(
        By.CSS_SELECTOR, "#exampleModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        
        ##VALIDASI
        try:
          response_data = WebDriverWait(driver, 3).until(EC.alert_is_present())
          response_text = response_data.text
          driver.switch_to.alert.accept()
          assert response_text == "Email Cannot be Empty!!"

        except:
            pytest.fail("Failed")

    def test_verify_submit_contact_With_empty_form(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(5)
        driver.find_element(By.XPATH, elem.menuContact).click()
        time.sleep(3)
        driver.find_element(By.ID, elem.cEmail).send_keys("")
        driver.find_element(By.ID, elem.cIdName).send_keys("")
        driver.find_element(By.ID, elem.cIdMessage).send_keys("")
        ##driver.find_element(By.XPATH, elem.btnSend).click()
        driver.find_element(
        By.CSS_SELECTOR, "#exampleModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        
        ##VALIDASI
        try:
          response_data = WebDriverWait(driver, 10).until(EC.alert_is_present())
          response_text = response_data.text
          driver.switchTo_alert.getText.accept()
          assert response_text == "Cant Send Message With Empty Form !!"

        except:
            pytest.fail("Failed")

if __name__ == "__main__":
     unittest.main()
