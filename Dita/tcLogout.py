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

    def test_a_success_logout(self):
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
        browser.find_element(By.ID, "logout2").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.ID, "login2").text
        self.assertIn('Log in', response_data)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()