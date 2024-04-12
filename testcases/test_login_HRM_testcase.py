import time
import allure
from allure_commons.types import AttachmentType

from pages.test_pages_orangehrm import Test_ohrm_login
from utilities.logger import LogGenerator
from utilities.ReadConfig import ReadConfig

class Test_OhrmProject():

    USERNAME = ReadConfig.getUserName()
    PASSWORD = ReadConfig.getPassword()

    log = LogGenerator.logger()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("TITLE OF THE TEST CASE")
    @allure.issue("THIS IS THE ISSUE #1")
    @allure.story("THIS IS STORY #1")

    def test_page_title_ohrm_001(self,setup):

        self.log.info("TEST_PAGE_TITLE_OHRM_001 IS STARTED")

        self.log.info("MAXIMIZE THE BROWSER")

        self.driver = setup

        self.obj = Test_ohrm_login(self.driver)

        self.log.info('NAVIGATING TO THE URL')
        self.obj.test_url('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        self.log.info('CHECKING THE TITLE OF THE PAGE')
        if (self.driver.title=='OrangeHRM'):

            self.log.info('TAKING THE SCREENSHOT')
            allure.attach(self.driver.get_screenshot_as_png(), name = "test_page_title_001_pass", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\pythonProject\\Orange HRM Project\\screenshots\\test_page_title_ohrm_pass.png")
            time.sleep(2)
            print('\n You are at correct page')

            self.log.info('CLOSING THE BROWSER')
            self.driver.close()

            assert True

        else:
            self.log.info('TAKING THE SCREENSHOT')
            allure.attach(self.driver.get_screenshot_as_png(), name = "test_page_title_001_fail", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\pythonProject\\Orange HRM Project\\screenshots\\test_page_title_fail.png")
            print('\n You Are At Wrong Page')

            self.log.info('CLOSING THE BROWSER')
            self.driver.close()
            assert False
        self.log.info('TEST_PAGE_TITLE_OHRM_OO1 IS STARTED ')

    def test_login_HRM_002(self,setup):

        self.log.info('TEST_LOGIN_HRM_002 IS STARTED')

        self.log.info('OPENING THE BROWSER')

        self.log.info('MAXIMIZE THE BROWSER')

        self.driver = setup

        self.obj = Test_ohrm_login(self.driver)
        
        self.log.info("NAVIGATING TO THE URL")
        self.obj.test_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        self.log.info("ENTER THE USERNAME")
        self.obj.test_enter_username('Admin')

        self.log.info("ENTER THE PASSWORD")
        self.obj.test_enter_password('admin123')

        self.log.info("CLICK ON LOGIN BUTTON")
        self.obj.test_click_login()

        self.log.info("CHECKING FOR THE LOGIN STATUS")
        self.obj.test_login_status()

        if(self.obj.test_login_status()==True):
            self.log.info("TAKING SCREENSHOT")
            allure.attach(self.driver.get_screenshot_as_png(), name = "test_login_002_pass", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\pythonProject\\Orange HRM Project\\screenshots\\test_login_status_pass.png")
            print('\n***Login Sucessfully***')

            self.log.info("CLICK ON MENU BUTTON")
            self.obj.test_click_menu_button()

            self.log.info("CLICK ON LOGOUT BUTTON")
            self.obj.test_click_logout()

            self.log.info("CLOSING THE BROWSER")
            self.driver.close()
            assert True

        else:
            self.log.info("TAKING SCREENSHOT")
            allure.attach(self.driver.get_screenshot_as_png(), name = "test_login_002_fail", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\pythonProject\\Orange HRM Project\\screenshots\\test_login_status_fail.png")

            print('\n***Login Unsucessful*** ')

            self.log.info("CLOSING THE BROWSER")
            self.driver.close()
            assert False
        self.log.info("TEST CASE LOGIN 002 IS COMPLETED")

