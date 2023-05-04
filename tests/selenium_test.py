from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

URL = "8306_Bobokhonov_AKh-app-1:5000"

class TestSelenium:
    def setup_method(self):
        binary = FirefoxBinary("/firefox/firefox")
        self.driver = webdriver.Firefox(firefox_binary=binary)
    def test_login(self):
        self.driver.get(f"http://{URL}/")
        header = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Enter Name:')]")
        assert header != None

        name_field = self.driver.find_element(By.NAME, "name")
        name_field.send_keys("test")

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("test2")

        assert password_field.get_attribute('value') == 'test2'

        password_field.send_keys(Keys.RETURN)

        self.driver.implicitly_wait(2)

        assert self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Unauthorized')]") != None
        assert self.driver.current_url == f"http://{URL}/login"     
    def teardown_method(self):
        self.driver.close()
