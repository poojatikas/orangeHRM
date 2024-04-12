from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class Test_search_emp():
    empid_tf_xp = (By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]')
    search_button_xp = (
    By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')
    search_result_xp = (By.XPATH, "//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']")

    def __init__(self,driver):
        self.driver = driver

    def test_enter_search_emp(self,empid):
        self.driver.find_element(*Test_search_emp.empid_tf_xp).send_keys(empid)

    def test_click_search_button(self):
        self.driver.find_element(*Test_search_emp.search_button_xp).click()


    def test_search_results(self):
        try:
            firstmiddlename=self.driver.find_element(*Test_search_emp.search_result_xp).text
            print('\n', firstmiddlename)
            return True

        except NoSuchElementException:
            return False





