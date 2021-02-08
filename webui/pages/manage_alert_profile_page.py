from webui.pages.base_page import BasePage
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ManageAlertProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.delete_button = driver.find_element(by=By.ID, value='deleteSQDButton')
        self.edit_button = driver.find_element(by=By.ID, value='editSQDButton')
        self.copy_button = driver.find_element(by=By.ID, value='copySQDButton')
        self.new_button = driver.find_element(by=By.ID, value='addSQDButton')
        self.custom_alert_profile_options_locator = (By.ID, "sqdTemplateList")
        self.condition_labels_locator = (By.XPATH, "//tr[@class='table-row']//td[contains(@id, 'Label')]")

    def click_path_type(self, path_type):
        self.driver.find_element(by=By.XPATH, value="//button[text()='{}']".format(path_type)).click()

    def click_alert_profile(self, alert_profile_name):
        for option in self.driver.find_elements(*self.custom_alert_profile_options_locator):
            if option.text == alert_profile_name:
                option.click()
                break

    def get_conditions(self):
        conditions = []
        for label in self.driver.find_elements(*self.condition_labels_locator):
            conditions.append(label.text)
        return conditions

    def create_alert_profile_with_conditions_by_path_type(self, path_type, alert_name, condition, violates_minutes,
                                                          clear_minutes, violates_value):
        self.click_path_type(path_type)
        self.create_alert_profile(alert_name, condition, violates_minutes, clear_minutes, violates_value)

    def go_to_new_alert_profile_page(self):
        self.new_button.click()
        return NewAlertProfilePage(self.driver)

    def create_alert_profile(self, alert_name, condition, violates_minutes, clear_minutes, violates_value):
        new_alert_profile_page = self.go_to_new_alert_profile_page()
        new_alert_profile_page.fill_alert_profile_details(alert_name, condition, violates_minutes, clear_minutes,
                                                          violates_value)
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located((By.XPATH, "//button[@title='Create']")))

    def is_alert_profile_exists_by_path_type(self, path_type, alert_profile_name):
        self.click_path_type(path_type)
        return self.check_alert_profile_exists(alert_profile_name)

    def get_alert_profile_conditions(self, path_type, alert_profile_name):
        self.click_path_type(path_type)
        self.click_alert_profile(alert_profile_name)
        return self.get_conditions()

    def check_alert_profile_exists(self, alert_profile_name):
        for option in self.driver.find_elements(*self.custom_alert_profile_options_locator):
            if option.text == alert_profile_name:
                return True
        return False

    def delete_alert_profile(self, alert_profile_name):
        for option in self.driver.find_elements(*self.custom_alert_profile_options_locator):
            if alert_profile_name in option.text:
                option.click()
                self.delete_button.click()
                if self.is_element_present('confirm_deletion_dialog'):
                    self.confirm_deletion_button.click()

    def delete_alert_profile_by_path_type(self, path_type, alert_profile_name):
        self.click_path_type(path_type)
        try:
            self.delete_alert_profile(alert_profile_name)
        except StaleElementReferenceException:
            # Sometimes selenium driver will throw exceptions on this page
            # the root cause is unknown, however this doesn't effect the
            # delete operation
            pass

class NewAlertProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.alert_name_input = driver.find_element(by=By.NAME, value='alertName')
        self.condition_select = driver.find_element(by=By.ID, value='select-condition-input')
        self.create_alert_profile_button = driver.find_element(by=By.XPATH, value="//button[text()='Create']")
        self.add_condition_button = driver.find_element(by=By.XPATH,
                                                value="//button[contains(@class,'ui-button')][contains(text(), 'Add')]")

        self.condition_minutes_inputs_locator = (By.XPATH, "//div[text()='minutes']/preceding-sibling::input[1]")
        self.condition_minutes_inputs_connectivity_locator = (By.XPATH,
                                            "//div[text()='minutes']/preceding-sibling::span[1]//input[not(@disabled)]")
        self.condition_percentage_inputs_locator = (By.XPATH, "//div[text()='%']/preceding-sibling::input[1]")
        self.condition_mbps_inputs_locator = (By.XPATH, "//div[text()='Mbps']/preceding-sibling::input[1]")
        self.condition_ms_inputs_locator = (By.XPATH, "//div[text()='ms']/preceding-sibling::input[1]")
        self.condition_tests_inputs_locator = (By.XPATH, "//div[text()='tests']/preceding-sibling::input[1]")

    def set_alert_name(self, alert_name):
        self.alert_name_input.clear()
        self.alert_name_input.send_keys(alert_name)

    def select_condition(self, condition):
        condition_select = Select(self.condition_select)
        condition_select.select_by_visible_text(condition)

    def set_violates_minutes_input_value(self, value):
        condition_minutes_inputs_connectivity = self.driver.\
            find_elements(*self.condition_minutes_inputs_connectivity_locator)
        condition_minutes_inputs = self.driver.find_elements(*self.condition_minutes_inputs_locator)
        condition_tests_inputs = self.driver.find_elements(*self.condition_tests_inputs_locator)
        if len(condition_minutes_inputs_connectivity) > 0:
            condition_minutes_inputs_connectivity.clear()
            condition_minutes_inputs_connectivity.send_keys(value)
        elif len(condition_minutes_inputs) > 0:
            condition_minutes_inputs[0].clear()
            condition_minutes_inputs[0].send_keys(value)
        elif len(condition_tests_inputs) > 0:
            condition_tests_inputs[0].clear()
            condition_tests_inputs[0].send_keys(value)

    def set_clears_minutes_input_value(self, value):
        condition_minutes_inputs_connectivity = self.driver.\
            find_elements(*self.condition_minutes_inputs_connectivity_locator)
        condition_minutes_inputs = self.driver.find_elements(*self.condition_minutes_inputs_locator)
        condition_tests_inputs = self.driver.find_elements(*self.condition_tests_inputs_locator)
        if len(condition_minutes_inputs_connectivity) > 0:
            condition_minutes_inputs_connectivity[1].clear()
            condition_minutes_inputs_connectivity[1].send_keys(value)
        elif len(condition_minutes_inputs) > 0:
            condition_minutes_inputs[1].clear()
            condition_minutes_inputs[1].send_keys(value)
        elif len(condition_tests_inputs) > 0:
            condition_tests_inputs[1].clear()
            condition_tests_inputs[1].send_keys(value)

    def fill_condition_details(self, condition, violates_minutes, clear_minutes, violates_value=0):
        self.select_condition(condition)
        condition_ms_inputs = self.driver.find_elements(*self.condition_ms_inputs_locator)
        condition_percentage_inputs = self.driver.find_elements(*self.condition_percentage_inputs_locator)
        condition_mbps_inputs = self.driver.find_elements(*self.condition_mbps_inputs_locator)
        if not (condition in ['DHCP Errors', 'Wireless Interface Errors', 'QoS Change']):
            if condition in ['Latency', 'RTT', 'Data Jitter', 'Voice Jitter']:
                condition_ms_inputs[0].send_keys(str(violates_value))
            elif condition in ['Data Loss', 'Available Capacity (%)', 'Utilized Capacity (%)',
                               'Total Capacity Symmerty (%)', \
                               'Voice Loss']:
                condition_percentage_inputs[0].send_keys(str(violates_value))
            elif condition in ['Total Capacity (Mbps)', 'Available Capacity (Mbps)', 'Utilized Capacity (Mbps)', \
                               'Total Capacity Symmerty (Mbps)']:
                condition_mbps_inputs[0].send_keys(str(violates_value))
            self.set_violates_minutes_input_value(violates_minutes)
            self.set_clears_minutes_input_value(clear_minutes)
        self.add_condition_button.click()

    def fill_alert_profile_details(self, alert_name, condition, violates_minutes, clear_minutes, violates_value=0):
        self.set_alert_name(alert_name)
        self.fill_condition_details(condition, violates_minutes, clear_minutes, violates_value)
        self.create_alert_profile_button.click()
