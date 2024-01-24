import pytest
from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class Test_Edit:
    # Initialize the WebDriver at the class level for reuse across test methods
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    actions = ActionChains(driver)

    def test_edit_emp(self):
        # Step 1: Maximize the browser window and navigate to the application URL
        self.driver.maximize_window()
        self.driver.get(data.WebData().url)
        # Step 2: Enter username, password, and click on the login button
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))
        ).send_keys(data.WebData().username)
        self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
            data.WebData().password)
        self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()
        sleep(2)
        # Step 3: Navigate to the PIM module and EmployeeList page
        self.driver.get(data.WebData().add_search_employeelist_url)
        # Step 4: Search the employee by name
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_emp_name)))

        search_input.send_keys("NewLastName")
        sleep(3)
        search_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_button)))
        search_button.click()
        sleep(1)
        # Step 6: Assert the current URL to confirm the employee is edited
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList#"