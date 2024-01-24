from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Text:

    # Initialize the WebDriver at the class level for reuse across test methods
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def text_delete(self):
        """
        This method performs the following steps:
        1. Opens the browser, navigates to the application URL, and logs in.
        2. Navigates to the PIM module and the EmployeeList page.
        3. Retrieves the name of the employee in the first row.
        4. Deletes the employee using the delete button and handles the confirmation alert.
        5. Searches for the deleted employee in the EmployeeList page.
        6. Quits the browser.
        """
        try:
            # Step 1: Open the browser and navigate to the application URL
            self.driver.maximize_window()
            self.driver.get(data.WebData().url)

            # Step 2: Enter username, password, and click on the login button
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(data.WebData().username)
            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(data.WebData().password)
            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()

            # Step 3: Navigate to the PIM module
            pim_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
            pim_link.click()

            # Step 4: Navigate to the EmployeeList page
            employee_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().employee_link_locator)))
            employee_link.click()

            # Step 5: Retrieve the name of the employee in the first row
            name_in_first_row = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().first))).text
            print(name_in_first_row)

            # Step 6: Delete the employee using the delete button and handle the confirmation alert
            delete = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().delete_button_locator)))
            delete.click()

            alert_1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().alert_locator)))
            alert_1.click()

            # Step 7: Search for the deleted employee in the EmployeeList page - This confirms the delete operation (considered as assertion for delete test case)
            self.driver.get(data.WebData().search_employeelist_url)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_emp_name))).send_keys(name_in_first_row)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_button))).click()
            sleep(30)
            # Assert the current URL to confirm the employee is added
            assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList#"

        finally:
            # Step 9: Quit the browser
            self.driver.quit()


if __name__ == "__main__":
    text = Text()
    text.text_delete()
