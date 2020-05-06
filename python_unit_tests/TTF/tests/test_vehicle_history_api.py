# General imports
import time
import json
import unittest
import xlrd
from libs.common_functions import fire_get_request, fire_post_request
from config import settings
from utils.logger import ttf_logger

logger = ttf_logger(__name__)

class VehicleHistoryApiCall(unittest.TestCase):
    
    def test_1234(self):
        """
        Test for HTTP level status code validation - Vehicle History API - GET
        """
        logger.info("test_1234: Test for HTTP level status code validation - Vehicle History API - GET")
        output = fire_get_request(settings.get_url, settings.get_headers, settings.get_query, 30)
        http_response = output['response']
        logger.info("HTTP status code: {}".format(http_response.status_code))
    
        self.assertEqual(http_response.status_code, 200, "200 OK Status Code Validation Failed")
    

    def test_1235(self):
        """
        Test for VIN validation - Vehicle History API - GET
        """
        logger.info("test_1235: Test for VIN validation - Vehicle History API - GET")
        output = fire_get_request(settings.get_url, settings.get_headers, settings.get_query, 30)
        json_response = output['response'].json()
        logger.info("HTTP status code: {}".format(output['response'].status_code))
        vid_from_api = json_response["consolidated"]["VehicleSpecifications"]["VehicleSpecificationsLine"][0]["Vehicle"]["VehicleID"]
        logger.info("VIN: {}".format(vid_from_api))

        self.assertEqual(vid_from_api, settings.get_query['vin'], "VIN Validation Failed")
    

    def test_1236(self):
        """
        Test for Company/OEM validation - Vehicle History API - GET
        """
        logger.info("test_1236: Test for Company/OEM validation - Vehicle History API - GET")
        output = fire_get_request(settings.get_url, settings.get_headers, settings.get_query, 30)
        json_response = output['response'].json()
        logger.info("HTTP status code: {}".format(output['response'].status_code))

        company_name = json_response["consolidated"]["VehicleSpecifications"]["VehicleSpecificationsHeader"]["ManufacturerParty"]["SpecifiedOrganization"]["CompanyName"]
        oem = json_response["oem"]
        logger.info("Company Name: {}".format(company_name))
        logger.info("OEM Body: {}".format(oem))
        
        self.assertTrue(company_name is not None, "Null value in company name found")
        self.assertTrue(oem is not None, "Null value in OEM  found")
    
    
    def test_1237(self):
        """
        Test for HTTP level status code validation - Vehicle History API - POST
        """
        logger.info("test_1237: Test for HTTP level status code validation - Vehicle History API - POST")
        output = fire_post_request(settings.post_url, settings.post_headers, settings.post_data, 30)
        http_response = output['response']
        logger.info("HTTP status code: {}".format(http_response.status_code))
    
        self.assertEqual(http_response.status_code, 200, "200 OK Status Code Validation Failed")
    

if __name__ == '__main__':
        unittest.main()