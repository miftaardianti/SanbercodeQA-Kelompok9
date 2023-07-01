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

    def test_a_success_login(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.demoblaze.com/")  # buka situs
        time.sleep(3)
        # Gunakan Username dan Password yang sudah terdaftar/teregistrasi
        browser.find_element(By.ID, "login2").click()
        time.sleep(3)
        browser.find_element(By.ID, "loginusername").send_keys(
            "test450"
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "loginpassword").send_keys(
            "kelompok123"
        )  # isi password
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()  # klik tombol submit
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.ID, "nameofuser").text
        self.assertIn('Welcome', response_data)
        

    def test_b_failed_login_with_unregistered_username(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.demoblaze.com/")  # buka situs
        time.sleep(3)
        # Gunakan Username dan Password yang belum terdaftar/teregistrasi
        browser.find_element(By.ID, "login2").click()
        time.sleep(3)
        browser.find_element(By.ID, "loginusername").send_keys(
            "test450lsj"
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "loginpassword").send_keys(
            "kelompok1234"
        )  # isi password
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()  # klik tombol submit
        time.sleep(3)

        # validasi
        expectedAlertMessage = "User does not exist."
        time.sleep(3)
        ##Captured Alert Text (Actual Text)
        actualAlertMessage = browser.switch_to.alert.text
        ##Assertion
        self.assertEqual(expectedAlertMessage, actualAlertMessage)
        ##Accept the alert (Click OK)
        browser.switch_to.alert.accept()

    def test_c_failed_login_with_wrong_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.demoblaze.com/")  # buka situs
        time.sleep(3)
        # Gunakan Username yang valid (terdaftar) dan Password yang tidak valid
        browser.find_element(By.ID, "login2").click()
        time.sleep(3)
        browser.find_element(By.ID, "loginusername").send_keys(
            "test450"
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "loginpassword").send_keys(
            "kelompok9"
        )  # isi password
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()  # klik tombol submit
        time.sleep(3)

        # validasi
        expectedAlertMessage = "Wrong password."
        time.sleep(3)
        ##Captured Alert Text (Actual Text)
        actualAlertMessage = browser.switch_to.alert.text
        ##Assertion
        self.assertEqual(expectedAlertMessage, actualAlertMessage)
        ##Accept the alert (Click OK)
        browser.switch_to.alert.accept()

    def test_d_failed_login_with_wrong_username(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.demoblaze.com/")  # buka situs
        time.sleep(3)
        # Gunakan Username yang tidak valid (belum terdaftar) dan Password yang valid (sudah terdaftar/digunakan)
        browser.find_element(By.ID, "login2").click()
        time.sleep(3)
        browser.find_element(By.ID, "loginusername").send_keys(
            "testprogram478"
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "loginpassword").send_keys(
            "kelompok123"
        )  # isi password
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()  # klik tombol submit
        time.sleep(3)

        # validasi
        expectedAlertMessage = "User does not exist."
        time.sleep(3)
        ##Captured Alert Text (Actual Text)
        actualAlertMessage = browser.switch_to.alert.text
        ##Assertion
        self.assertEqual(expectedAlertMessage, actualAlertMessage)
        ##Accept the alert (Click OK)
        browser.switch_to.alert.accept()
    
    def test_e_failed_login_with_empty_username_and_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.demoblaze.com/")  # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "login2").click()
        time.sleep(3)
        browser.find_element(By.ID, "loginusername").send_keys(
            ""
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "loginpassword").send_keys(
            ""
        )  # isi password
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()  # klik tombol submit
        time.sleep(3)

        # validasi
        expectedAlertMessage = "Please fill out Username and Password."
        time.sleep(3)
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