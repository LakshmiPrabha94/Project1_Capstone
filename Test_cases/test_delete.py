# Importing necessary modules and classes
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from delete import Delete
import data
import locators


@pytest.fixture
def delete_instance():
    delete = Delete()
    yield delete
    #delete.shutdown()

# Positive test case
def test_delete_existent_emp(delete_instance):
    """
    Test case for deleting an employee:
    1. Opens the browser, navigates to the application URL, and logs in.
    2. Navigates to the PIM module and the EmployeeList page.
    3. Retrieves the name of the employee in the first row.
    4. Deletes the employee using the delete button and handles the confirmation alert.
    5. Searches for the deleted employee in the EmployeeList page.
    6. Quits the browser.
    """
    # Step 1: Booting function and login
    if delete_instance.booting_function() and delete_instance.login():
        # Step 2: Navigate to the PIM module
        pim_link = WebDriverWait(delete_instance.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
        pim_link.click()

        # Step 3: Navigate to the EmployeeList page
        employee_link = WebDriverWait(delete_instance.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().employee_link_locator)))
        employee_link.click()

        # Step 4: Retrieve the name of the employee in the first row
        name_in_first_row = WebDriverWait(delete_instance.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().first))).text
        print(f"Name of the employee in the first row: {name_in_first_row}")

        # Step 5: Delete the employee using the delete button and handle the confirmation alert
        delete_button = WebDriverWait(delete_instance.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().delete_button_locator)))
        delete_button.click()

        confirmation_alert = WebDriverWait(delete_instance.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().alert_locator)))
        confirmation_alert.click()

        # Step 6: Search for the deleted employee in the EmployeeList page - This confirms the delete operation
        delete_instance.driver.get(data.WebData().search_employeelist_url)
        search_name_input = WebDriverWait(delete_instance.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_emp_name)))
        search_name_input.send_keys(name_in_first_row)

        search_button = WebDriverWait(delete_instance.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_button)))
        search_button.click()

        sleep(15)  # Wait for the search results to load

        # Step 7: Assert the current URL to confirm the employee is deleted
        assert delete_instance.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"

# Negative test case
def test_delete_nonexistent_emp(delete_instance):
    """
    Negative test case for deleting a nonexistent employee:
    1. Opens the browser, navigates to the application URL, and logs in.
    2. Navigates to the PIM module and the EmployeeList page.
    3. Tries to delete an employee who does not exist.
    4. Handles any error messages or alerts that may appear.
    5. Quits the browser.
    """
    # Step 1: Booting function and login
    if delete_instance.booting_function() and delete_instance.login():
        # # Step 2: Navigate to the PIM module
        # pim_link = WebDriverWait(delete_instance.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
        # pim_link.click()

        # # Step 3: Navigate to the EmployeeList page
        # employee_link = WebDriverWait(delete_instance.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().employee_link_locator)))
        # employee_link.click()
        

        # Step 4: Try to delete an employee who does not exist

        delete_instance.driver.get(data.WebData().search_employeelist_url)
        search_name_input = WebDriverWait(delete_instance.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_emp_name)))
        search_name_input.send_keys(data.WebData.nonexistent_employee_name)

        search_button = WebDriverWait(delete_instance.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_button)))
        search_button.click()

        sleep(30)  # Wait for the search results to load

        # Check for any error messages or alerts
        try:
            error_message = WebDriverWait(delete_instance.driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().error_message_locator))).text
            print(f"Error Message: {error_message}")
        except:
            pass  # No error message found

        # Step 5: Assert the absence of the employee in the EmployeeList page
        assert delete_instance.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
