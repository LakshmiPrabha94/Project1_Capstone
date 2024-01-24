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


class Login_UI:
    # Initialize the WebDriver at the class level for reuse across methods
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def start(self):
        # Maximize the browser window, navigate to the application URL, and set implicit wait
        self.driver.maximize_window()
        self.driver.get(data.WebData().url)
        self.driver.implicitly_wait(10)

    def shutdown(self):
        # Close the browser
        self.driver.quit()

    def username_isdsplayed(self):
        # Start the browser, locate the username field, and check if it is displayed
        self.start()
        username = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
        if username.is_displayed():
            return True
        else:
            return False

    def username_isenabled(self):
        # Start the browser, locate the username field, and check if it is enabled
        self.start()
        username = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
        if username.is_enabled():
            return True
        else:
            return False

    def username_isselected(self):
        # Start the browser, locate the username field, and check if it is selected
        self.start()
        username = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
        if username.is_selected():
            return True
        else:
            return False

    def cursor_on_username(self):
        # Start the browser, locate the username field, and check if it has focus
        self.start()
        username = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
        active_element = self.driver.switch_to.active_element
        if username == active_element:
            return True
        else:
            return False

    def password_isdsplayed(self):
        # Start the browser, locate the password field, and check if it is displayed
        self.start()
        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().password_locator)))
        if password.is_displayed():
            return True
        else:
            return False

    def password_isenabled(self):
        # Start the browser, locate the password field, and check if it is enabled
        self.start()
        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().password_locator)))
        if password.is_enabled():
            return True
        else:
            return False

    def password_isselected(self):
        # Start the browser, locate the password field, and check if it is selected
        self.start()
        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().password_locator)))
        if password.is_selected():
            return True
        else:
            return False

    def cursor_on_password(self):
        # Start the browser, locate the password field, and check if it has focus
        self.start()
        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().password_locator)))
        active_element = self.driver.switch_to.active_element
        if password == active_element:
            return True
        else:
            return False

    def verify_password_masked(self):
        self.start()
        try:
            # Verify if the password field is masked (input type is password)
            # Explicit wait for password field to be clickable
            password_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, locators.WebLocators().password_locator))
            )

            # Enter username and password
            username_field = self.driver.find_element(by=By.NAME, value=locators.WebLocators().username_locator)
            username_field.send_keys(data.WebData().username)
            password_field.send_keys(data.WebData().password)

            # Check password field's "type" attribute directly
            password_type = password_field.get_attribute("type")
            if password_type == "password":
                print("Password field is masked.")
                return True
            else:
                print("Password field is not masked.")
                return False

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

        finally:
            self.shutdown()

    def login_button_isdsplayed(self):
        # Start the browser, locate the login field, and check if it is displayed
        self.start()
        login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().login_button_locator)))
        if login_button.is_displayed():
            return True
        else:
            return False

    def login_button_isenabled(self):
        # Start the browser, locate the login field, and check if it is enabled
        self.start()
        login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().login_button_locator)))
        if login_button.is_enabled():
            return True
        else:
            return False

    def login_button_isselected(self):
        # Start the browser, locate the login field, and check if it is selected
        self.start()
        login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().login_button_locator)))
        if login_button.is_selected():
            return True
        else:
            return False

    def cursor_on_login_button(self):
        # Start the browser, locate the login field, and check if it has focus
        self.start()
        login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().login_button_locator)))
        active_element = self.driver.switch_to.active_element
        if login_button == active_element:
            return True
        else:
            return False


if __name__ == '__main__':
    # Create an instance of the Login_UI class
    login_page = Login_UI()
    # Start the browser and navigate to the application URL
    login_page.start()
    # Perform Login UI functions
    print("Username Is_dispalyed:", login_page.username_isdsplayed())
    print("Username Is_enabled: ", login_page.username_isenabled())
    print("Username Is_selected: ", login_page.username_isselected())
    print("Username Is_focused: ", login_page.cursor_on_username())
    print("Password Is_dispalyed:", login_page.password_isdsplayed())
    print("Password Is_enabled: ", login_page.password_isenabled())
    print("Password Is_selected: ", login_page.password_isselected())
    print("Password Is_focused: ", login_page.cursor_on_password())

    print("Login Button Is_dispalyed:", login_page.login_button_isdsplayed())
    print("Login Button Is_enabled: ", login_page.login_button_isenabled())
    print("Login Button Is_selected: ", login_page.login_button_isselected())
    print("Login Button Is_focused: ", login_page.cursor_on_login_button())
    print("Password Is password masked: ", login_page.verify_password_masked())



