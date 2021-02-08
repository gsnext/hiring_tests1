import json
import unittest
from config import TestConfig
from utils import hit_endpoint, alert_profile_template


class TestAlertProfileAPI(unittest.TestCase):
    def test_create_alert_profile(self):
        alert_profile = alert_profile_template()
        alert_profile["name"] = self._testMethodName
        alert_profile["attribs"][0]["param"] = "Connectivity"
        alert_profile["attribs"][0]["scope"] = "Overall"
        response_post = hit_endpoint('post', TestConfig.url + "/api/v3/alertProfile?api_key=v3", json=alert_profile)
        response = hit_endpoint('get', TestConfig.url + "/api/v3/alertProfile/{}?api_key=v3".format(json.loads(response_post.text)["id"]), json=alert_profile)
        response_json = json.loads(response.text)
        assert response_json["name"] == self._testMethodName
        assert response_json["attribs"][0]["param"] == alert_profile["attribs"][0]["param"]
        assert response_json["attribs"][0]["scope"] == alert_profile["attribs"][0]["scope"]
        hit_endpoint('delete', TestConfig.url + "/api/v3/alertProfile/{}?api_key=v3".format(response_json["id"]))

    def test_update_alert_profile_name(self):
        alert_profile = alert_profile_template()
        alert_profile["name"] = self._testMethodName
        alert_profile["attribs"][0]["param"] = "Connectivity"
        alert_profile["attribs"][0]["scope"] = "Overall"
        alert_profile["attribs"][0]["value"] = 7
        response_post = hit_endpoint('post', TestConfig.url + "/api/v3/alertProfile?api_key=v3", json=alert_profile)
        alert_profile["name"] = "test"
        alert_profile["attribs"][0]["param"] = "Availability"
        response_put = hit_endpoint('put', TestConfig.url + "/api/v3/alertProfile?api_key=v3", json=alert_profile)
        response = hit_endpoint('get', TestConfig.url + "/api/v3/alertProfile/{}?api_key=v3".format(json.loads(response_put.text)["id"]), json=alert_profile)
        response_json = json.loads(response.text)
        assert response_json["attribs"][0]["param"] == alert_profile["attribs"][0]["param"]
        assert response_json["attribs"][0]["scope"] == alert_profile["attribs"][0]["scope"]

    def test_delete_alert_profile(self):
        alert_profile = alert_profile_template()
        alert_profile["name"] = self._testMethodName
        alert_profile["attribs"][0]["param"] = "Connectivity"
        alert_profile["attribs"][0]["scope"] = "Overall"
        response_post = hit_endpoint('post', TestConfig.url + "/api/v3/alertProfile?api_key=v3", json=alert_profile)
        response = hit_endpoint('get', TestConfig.url + "/api/v3/alertProfile/{}?api_key=v3".
                                format(json.loads(response_post.text)["id"]), json=alert_profile)
        response_json = json.loads(response.text)
        hit_endpoint('delete', TestConfig.url + "/api/v3/alertProfile/{}?api_key=v3")
        response = hit_endpoint('get', TestConfig.url + "/api/v3/alertProfile/{}?api_key=v3".
                                format(json.loads(response_post.text)["id"]), json=alert_profile)
        response_json = json.loads(response.text)

        if (response_json["name"] == self._testMethodName) or (response_json["attribs"][0]["param"] == alert_profile["attribs"][0]["param"]) or (response_json["attribs"][0]["scope"] == alert_profile["attribs"][0]["scope"]):
            assert False
        else:
            assert True

if __name__ == '__main__':
    unittest.main()
