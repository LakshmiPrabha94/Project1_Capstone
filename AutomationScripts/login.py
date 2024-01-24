from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    # Initialize the WebDriver at the class level for reuse across methods
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def start(self):
        # Step 1: Maximize the browser window and navigate to the application URL
        self.driver.maximize_window()
        self.driver.get(data.WebData().url)

    def shutdown(self):
        # Step 6: Close the browser
        self.driver.quit()

    def login(self):
        try:
            # Step 2: Enter username, password, and click on the login button
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
                data.WebData().username)
            print("Entering username:", data.WebData().username)
            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
                data.WebData().password)
            print("Entering password:", data.WebData().password)
            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()
            print("Clicking the login button")
            print("Welcome to OrangeHRM!!!")

        except NoSuchElementException as e:
            # Handle NoSuchElementException and print the error
            print("Error : ", e)
        finally:
            # Step 5: Wait for 3 seconds and then close the browser
            self.shutdown()


if __name__ == '__main__':
    # Step 0: Create an instance of the Login class
    login_page = Login()
    # Step 1: Start the browser and navigate to the application URL
    login_page.start()
    # Step 2: Perform login
    login_page.login()
