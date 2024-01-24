# Importing necessary modules and classes
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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class Edit:
    # Initialize the WebDriver at the class level for reuse across methods
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    actions = ActionChains(driver)

    
    def booting_function(self):
        try:
            # Maximize the browser window and navigate to the application URL
            self.driver.maximize_window()
            self.driver.get(data.WebData().url)
            print("Browser started successfully.")
            return True
        except Exception as e:
            print(f"ERROR: Unable to start the browser: {e}")
            return False

    def shutdown(self):
        # Close the browser
        self.driver.quit()

    def login(self):
        try:
            # Enter username, password, and click on the login button
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))
            )
            self.driver.find_element(by=By.NAME, value=locators.WebLocators().username_locator).send_keys(
                data.WebData().username
            )

            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
                data.WebData().password
            )

            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()
            print("Login successful.")
            return True
        except Exception as e:
            print(f"Error during login: {e}")
            return False

    def edit_emp(self):
        try:
            # Navigate to PIM and Employee pages to edit employee details
            pim_link = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
            pim_link.click()

            # click on the employee to edit
            employee_link = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().employee_link_locator)))
            employee_link.click()
            print("Employee List is loaded.")

            edit_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().edit_button_locator)))
            edit_button.click()
            print("Edit Button clicked")

            self.actions.send_keys(Keys.TAB).perform()

            # Now edit the employee information                      
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().form_locator)))

            first_name = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().first_name_locator)))
            first_name.clear()
            first_name.send_keys("NewFirstName")
            print("F Name is edited.")
            sleep(3)

            middle_name = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().middle_name_locator)))
            middle_name.clear()
            middle_name.send_keys("NewMidddleName")
            print("MName is edited.")
            sleep(3)

            self.driver.find_element(By.XPATH, locators.WebLocators().last_name_locator).clear()
            self.driver.find_element(By.XPATH, locators.WebLocators().last_name_locator).send_keys("NewLastName")
            print("LName is edited.")
            sleep(2)

            nick_name = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().nick_name_locator)))
            nick_name.clear()
            nick_name.send_keys("NewNickName")
            sleep(3)

            self.driver.find_element(By.XPATH, locators.WebLocators().employee_id_locator).clear()
            self.driver.find_element(By.XPATH, locators.WebLocators().employee_id_locator).send_keys("120347")
            sleep(2)

            self.driver.find_element(By.XPATH, locators.WebLocators().other_id_locator).clear()
            self.driver.find_element(By.XPATH, locators.WebLocators().other_id_locator).send_keys("id")
            sleep(2)

            self.driver.find_element(By.XPATH, locators.WebLocators().ssn_number_locator).clear()
            self.driver.find_element(By.XPATH, locators.WebLocators().ssn_number_locator).send_keys("ssn01")
            sleep(2)

            self.driver.find_element(By.XPATH, locators.WebLocators().license_number_locator).clear()
            self.driver.find_element(By.XPATH, locators.WebLocators().license_number_locator).send_keys("license3456")
            sleep(2)

            self.driver.find_element(By.XPATH, locators.WebLocators().sin_number_locator).clear()
            self.driver.find_element(By.XPATH, locators.WebLocators().sin_number_locator).send_keys("sin01")
            sleep(2)

            # Save the changes
            save_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().save_button_locator)))
            save_button.click()
            sleep(2)
            save_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().save_button_locator2)))
            save_button.click()
            sleep(2)

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Create an instance of the Edit class
    edit = Edit()
    # Start the browser and navigate to the application URL
    if edit.booting_function() and edit.login():
        # Perform Edit function
        edit.edit_emp()


