import pytest
from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from orange_add import Add
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class Test_Add:
    # Initialize the WebDriver at the class level for reuse across test methods
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    actions = ActionChains(driver)

    def test_add_emp(self):
        
        # Step 1: Boot up the application and perform login
        Add.booting_function(self)
        Add.login(self)
        # Step 2: Navigate to the PIM module and click on 'Add' button
        pim_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
        pim_link.click()

        click_add = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().add_button_locator)))
        click_add.click()

        # Step 3: Fill in employee details
        self.actions.send_keys(Keys.TAB).perform()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().fname_locator))).send_keys(
            data.WebData().add_fname)
        print("First Name filled")
        sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().mname_locator))).send_keys(
            data.WebData().add_mname)
        print("Middle Name filled")
        sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().lname_locator))).send_keys(
            data.WebData().add_lname)
        print("Last Name filled")
        sleep(2)

        emp_id = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().emp_id_locator)))
        emp_id.clear()
        emp_id.send_keys(data.WebData().add_emp_id)
        print("Employee ID filled")
        sleep(3)

        toggle = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().toggle_locator)))
        toggle.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().uname_locator))).send_keys(
            data.WebData().add_username)
        print("UserName filled")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pass_locator))).send_keys(
            data.WebData().add_password)
        print("Password filled")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().confirm_pass_locator))).send_keys(
            data.WebData().confirm_password)
        print("Confirm Password filled")
        sleep(3)

        self.actions.send_keys(Keys.TAB).perform()

        # Step 4: Save the employee details
        save = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().save_locator)))
        save.click()
        sleep(3)
        # Step 5: Fill in the personal details and save
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().form_locator)))

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().first_name_locator)))

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().other_id_locator))).clear()
        self.driver.find_element(By.XPATH, locators.WebLocators().other_id_locator).send_keys("id")

        self.driver.find_element(By.XPATH, locators.WebLocators().ssn_number_locator).clear()
        self.driver.find_element(By.XPATH, locators.WebLocators().ssn_number_locator).send_keys("ssn01")

        self.driver.find_element(By.XPATH, locators.WebLocators().license_number_locator).clear()
        self.driver.find_element(By.XPATH, locators.WebLocators().license_number_locator).send_keys("LIC456")

        self.driver.find_element(By.XPATH, locators.WebLocators().sin_number_locator).clear()
        self.driver.find_element(By.XPATH, locators.WebLocators().sin_number_locator).send_keys("sin01")
        
        save_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().save_button_locator)))
        save_button.click()

        save_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().save_button_locator2)))
        save_button.click()
        sleep(2)

        # Step 5: Navigate to the EmployeeList page and search for the added employee
        self.driver.get(data.WebData().add_search_employeelist_url)

        
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_emp_name)))
        search_input.send_keys(data.WebData().add_lname)

        sleep(3)
        search_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_button)))
        search_button.click()
        sleep(15)
        # Step 6: Assert the current URL to confirm the employee is added
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList#"


if __name__ == "__main__":
    add = Test_Add()
    add.test_add_emp()
