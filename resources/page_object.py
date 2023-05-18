from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data_elements.element_mapper import *


class HomePageObject:
    """
        This helps to resolve all actions carried out on the home page
    """

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def launch_page(self):
        """
        This method launches the page
        :return: a launched web page
        """
        self.driver.get(HomePage.url)
        self.driver.maximize_window()

    def mouse_over_element(self, element):
        ele = self.driver.find_element(By.CSS_SELECTOR, element)
        self.action.move_to_element(ele).perform()

    def click_element(self, element):
        self.wait_for_presence(element)
        self.driver.find_element(By.CSS_SELECTOR, element).click()

    def wait_for_presence(self, element):
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, element)))

    def wait_for_selection(self, element):
        self.wait.until(ec.element_located_to_be_selected((By.CSS_SELECTOR, element)))

    def wait_for_text_presence(self, element, text):
        self.wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, element), text))

    def verify_text(self, element, message):
        self.wait_for_presence(element)
        expect_text = self.driver.find_element(By.CSS_SELECTOR, element).text
        assert expect_text == message

    def select_value(self, element, value):
        self.wait_for_presence(element)
        ele = self.driver.find_element(By.CSS_SELECTOR, element)
        select = Select(ele)
        select.select_by_value(value)

    def fill_details(self, field, text):
        self.wait_for_presence(field)
        self.driver.find_element(By.CSS_SELECTOR, field).send_keys(text)

    def execute_click_action(self, element):
        self.wait_for_presence(element)
        ele = self.driver.find_element(By.CSS_SELECTOR, element)
        self.driver.execute_script("arguments[0].click();", ele)

