import pytest
from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginUI:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    def test_username_isdsplayed(self, booting_function):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        username = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
        assert username.is_displayed() == 'False'

    def test_username_isenabled(self, booting_function):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        username = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
        assert username.is_enabled()

    def test_username_isselected(self, booting_function):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        username = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
        assert not username.is_selected()

    def test_cursor_on_username(self, booting_function):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        username = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
        active_element = self.driver.switch_to.active_element
        assert not username == active_element

    def test_password_isdsplayed(self, booting_function):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        password = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().password_locator)))
        assert not password.is_displayed()

    def test_password_isenabled(self, booting_function):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        password = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().password_locator)))
        assert password.is_enabled()

    def test_password_isselected(self, booting_function):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().password_locator)))
        assert not password.is_selected()

    def test_cursor_on_password(self, booting_function):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().password_locator)))
        active_element = self.driver.switch_to.active_element
        assert not password == active_element

    def test_login_button_isdsplayed(self, booting_function):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        login_button = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().login_button_locator)))
        assert not login_button.is_displayed()

    def test_login_button_isenabled(self, booting_function):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        login_button = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().login_button_locator)))
        assert login_button.is_enabled()

    def test_login_button_isselected(self, booting_function):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().login_button_locator)))
        assert not login_button.is_selected()

    def test_cursor_on_login_button(self, booting_function):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().login_button_locator)))
        active_element = self.driver.switch_to.active_element
        assert not login_button == active_element

    def test_verify_password_masked(self, booting_function):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        username = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
        password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, locators.WebLocators().password_locator))
        )

        # Enter username and password
        username_field = self.driver.find_element(by=By.NAME, value=locators.WebLocators().username_locator)
        username_field.send_keys(data.WebData().username)
        password_field.send_keys(data.WebData().password)

        # Check password field's "type" attribute directly
        password_type = password_field.get_attribute("type")
        assert password_type == "password"

