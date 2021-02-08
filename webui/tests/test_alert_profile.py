import unittest
from webui.tests.test_base import TestBase
from webui.pages.base_page import BasePage


class TestAlertProfile(TestBase):
    def test_create_web_path_alert_profile(self):
        base_page = BasePage(self.driver)
        manage_alert_profile_page = base_page.navigate_to_manage_alert_profile_page()
        manage_alert_profile_page.create_alert_profile_with_conditions_by_path_type("Web Path", self._testMethodName,
                                                                                    "Apdex Score", 2, 3, 3)
        assert manage_alert_profile_page.is_alert_profile_exists_by_path_type("Web Path", self._testMethodName)
        assert "Apdex Score" in manage_alert_profile_page.get_alert_profile_conditions("Web Path", self._testMethodName)
        manage_alert_profile_page.delete_alert_profile_by_path_type("Web Path", self._testMethodName)

    def test_update_web_path_alert_profile_name(self):
        base_page = BasePage(self.driver)
        manage_alert_profile_page = base_page.navigate_to_manage_alert_profile_page()
        assert True

    def test_delete_web_path_alert_profile(self):
        base_page = BasePage(self.driver)
        manage_alert_profile_page = base_page.navigate_to_manage_alert_profile_page()
        manage_alert_profile_page.create_alert_profile_with_conditions_by_path_type("Web Path", self._testMethodName,
                                                                                    "Apdex Score", 2, 3, 3)
        if manage_alert_profile_page.is_alert_profile_exists_by_path_type("Web Path", self._testMethodName):
            manage_alert_profile_page.delete_alert_profile_by_path_type("Web Path", self._testMethodName)
        else:
            assert False
        if manage_alert_profile_page.is_alert_profile_exists_by_path_type("Web Path", self._testMethodName):
            assert False
        else:
            assert True


if __name__ == '__main__':
    unittest.main()
