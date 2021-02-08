from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.settings_menu_locator = (By.CLASS_NAME, "appneta_usermenu_usermenu_configMenu")
        self.manage_alert_profiles_option_locator = (By.PARTIAL_LINK_TEXT, "Manage Alert Profiles")

    def is_element_present(self, by=By.ID, value=None):
        try:
            self.driver.find_element(by=by, value=value)
        except NoSuchElementException:
            return False
        return True

    def navigate_to_manage_alert_profile_page(self):
        from webui.pages.manage_alert_profile_page import ManageAlertProfilePage
        action_chain = ActionChains(self.driver)
        action_chain.move_to_element(self.driver.find_element(*self.settings_menu_locator)).perform()
        action_chain.click(self.driver.find_element(*self.manage_alert_profiles_option_locator)).perform()
        return ManageAlertProfilePage(self.driver)


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.user_name_text_box = driver.find_element(by=By.ID, value='username-input')
        self.user_id_text_box = driver.find_element(by=By.XPATH, value='//*[@id="username-input"]')
        self.password_text_box = driver.find_element(by=By.NAME, value='j_password')
        self.login_button = driver.find_element(by=By.ID, value='login-button')
        self.continue_button_locator = (By.XPATH, "//button[text()='Continue >>']")

    def set_user_name(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.user_name_text_box))
        self.user_name_text_box.send_keys(username)

    def set_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.password_text_box))
        self.password_text_box.send_keys(password)

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.user_name_text_box))
        self.set_user_name(username)
        self.set_password(password)
        self.login_button.click()
        if self.is_element_present(*self.continue_button_locator):
            self.driver.find_element(*self.continue_button).click()
