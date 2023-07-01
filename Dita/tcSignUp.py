import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_a_success_signup(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.demoblaze.com/")  # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "signin2").click()
        time.sleep(3)
        browser.find_element(By.ID, "sign-username").send_keys(
            "Kelompok9batch46"
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "sign-password").send_keys(
            "kelompok123"
        )  # isi password
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()  # klik tombol submit
        time.sleep(3)

        # validasi
        expectedAlertMessage = "Sign up successful."
        time.sleep(5)
        ##Captured Alert Text (Actual Text)
        actualAlertMessage = browser.switch_to.alert.text
        ##Assertion
        self.assertEqual(expectedAlertMessage, actualAlertMessage)
        ##Accept the alert (Click OK)
        browser.switch_to.alert.accept()

    def test_b_failed_signup_with_empty_username(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.demoblaze.com/")  # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "signin2").click()
        time.sleep(3)
        browser.find_element(By.ID, "sign-username").send_keys(
            ""
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "sign-password").send_keys(
            "kelompok123"
        )  # isi password
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()  # klik tombol submit
        time.sleep(3)

        # validasi
        expectedAlertMessage = "Please fill out Username and Password."
        time.sleep(5)
        ##Captured Alert Text (Actual Text)
        actualAlertMessage = browser.switch_to.alert.text
        ##Assertion
        self.assertEqual(expectedAlertMessage, actualAlertMessage)
        ##Accept the alert (Click OK)
        browser.switch_to.alert.accept()

    def test_c_failed_signup_with_empty_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.demoblaze.com/")  # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "signin2").click()
        time.sleep(3)
        browser.find_element(By.ID, "sign-username").send_keys(
            "Kelompok9QAB"
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "sign-password").send_keys(
            ""
        )  # isi password
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()  # klik tombol submit
        time.sleep(3)

        # validasi
        expectedAlertMessage = "Please fill out Username and Password."
        time.sleep(5)
        ##Captured Alert Text (Actual Text)
        actualAlertMessage = browser.switch_to.alert.text
        ##Assertion
        self.assertEqual(expectedAlertMessage, actualAlertMessage)
        ##Accept the alert (Click OK)
        browser.switch_to.alert.accept()

    def test_d_failed_signup_with_empty_username_and_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.demoblaze.com/")  # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "signin2").click()
        time.sleep(3)
        browser.find_element(By.ID, "sign-username").send_keys(
            ""
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "sign-password").send_keys(
            ""
        )  # isi password
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()  # klik tombol submit
        time.sleep(3)

        # validasi
        expectedAlertMessage = "Please fill out Username and Password."
        time.sleep(5)
        ##Captured Alert Text (Actual Text)
        actualAlertMessage = browser.switch_to.alert.text
        ##Assertion
        self.assertEqual(expectedAlertMessage, actualAlertMessage)
        ##Accept the alert (Click OK)
        browser.switch_to.alert.accept()
    
    def test_e_failed_signup_with_registered_username(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.demoblaze.com/")  # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "signin2").click()
        time.sleep(3)
        browser.find_element(By.ID, "sign-username").send_keys(
            "test450"
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "sign-password").send_keys(
            "kelompok123"
        )  # isi password
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()  # klik tombol submit
        time.sleep(3)

        # validasi
        expectedAlertMessage = "This user already exist."
        time.sleep(5)
        ##Captured Alert Text (Actual Text)
        actualAlertMessage = browser.switch_to.alert.text
        ##Assertion
        self.assertEqual(expectedAlertMessage, actualAlertMessage)
        ##Accept the alert (Click OK)
        browser.switch_to.alert.accept()

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()