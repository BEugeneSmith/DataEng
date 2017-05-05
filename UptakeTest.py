from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

class test_uptake(unittest.TestCase):
    def setUp(self):
        self.success = True
        self.homepage = "https://uptake.com/"
        self.driver = Chrome('chromedriver.exe')
        self.driver.implicitly_wait(60)

    def test_homepage(self):
        driver = self.driver
        driver.get(self.homepage)
        driver.maximize_window()

        # get the contact page
        driver.find_element_by_xpath("//div[@class='social-links']//button[.='Contact']").click()

        # enter test data
        driver.find_element_by_id("firstname-c391fd6c-db94-4e29-9166-598f28f48702").click()
        driver.find_element_by_id("firstname-c391fd6c-db94-4e29-9166-598f28f48702").clear()
        driver.find_element_by_id("firstname-c391fd6c-db94-4e29-9166-598f28f48702").send_keys("test")
        driver.find_element_by_id("lastname-c391fd6c-db94-4e29-9166-598f28f48702").click()
        driver.find_element_by_id("lastname-c391fd6c-db94-4e29-9166-598f28f48702").clear()
        driver.find_element_by_id("lastname-c391fd6c-db94-4e29-9166-598f28f48702").send_keys("human")
        driver.find_element_by_id("company-c391fd6c-db94-4e29-9166-598f28f48702").click()
        driver.find_element_by_id("company-c391fd6c-db94-4e29-9166-598f28f48702").clear()
        driver.find_element_by_id("company-c391fd6c-db94-4e29-9166-598f28f48702").send_keys("test")
        driver.find_element_by_id("email-c391fd6c-db94-4e29-9166-598f28f48702").click()
        driver.find_element_by_id("email-c391fd6c-db94-4e29-9166-598f28f48702").clear()
        driver.find_element_by_id("email-c391fd6c-db94-4e29-9166-598f28f48702").send_keys("testhuman@loremipsum.org")
        driver.find_element_by_id("phone-c391fd6c-db94-4e29-9166-598f28f48702").click()
        driver.find_element_by_id("phone-c391fd6c-db94-4e29-9166-598f28f48702").clear()
        driver.find_element_by_id("phone-c391fd6c-db94-4e29-9166-598f28f48702").send_keys("123-456-7890")
        if not driver.find_element_by_xpath("//select[@id='potential_interest_picklist-c391fd6c-db94-4e29-9166-598f28f48702']//option[4]").is_selected():
            driver.find_element_by_xpath("//select[@id='potential_interest_picklist-c391fd6c-db94-4e29-9166-598f28f48702']//option[4]").click()
        driver.find_element_by_id("lead_description__c-c391fd6c-db94-4e29-9166-598f28f48702").click()
        driver.find_element_by_id("lead_description__c-c391fd6c-db94-4e29-9166-598f28f48702").clear()
        driver.find_element_by_id("lead_description__c-c391fd6c-db94-4e29-9166-598f28f48702").send_keys("ignore this message")

        # submit
        # driver.find_element_by_xpath("//div[@class='actions']/input").click()

        self.assertTrue(self.success)

    def test_products(self):
        driver = self.driver
        driver.get(self.homepage)
        driver.maximize_window()
        driver.find_element_by_link_text("INDUSTRIES").click()
        driver.find_element_by_link_text("Retail").click()
        driver.find_element_by_xpath("//div/div/button").click()
        driver.find_element_by_xpath("//div[@class='social-links']//button[.='Contact']").click()
        self.assertTrue(self.success)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
