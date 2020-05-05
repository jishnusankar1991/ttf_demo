# General imports
import requests
import time
import json
import unittest
import logging

# Logger specific configurations
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('test_vehicle_history_api-{time_stamp}.log'.format(time_stamp = time.strftime('%Y-%m-%d-%H%M%S')))
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

#stream_handler = logging.StreamHandler()
#stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
#logger.addHandler(stream_handler)


# URL Framing
url = 'https://api.tekion.xyz/api/integration/vehicleHistory/vehicleSpecs/vinLookup'

api_token = """eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6SXdOREF3UXpOQk0wRkVNelZFTmpNMU5UQXhSREEzUXpjM1FqVkZNalUxTVRrME1EbERSQSJ9.eyJuaWNrbmFtZSI6InJrb3RoYXBhbGxpIiwibmFtZSI6InJrb3RoYXBhbGxpQHRla2lvbi5jb20iLCJwaWN0dXJlIjoiaHR0cHM6Ly9zLmdyYXZhdGFyLmNvbS9hdmF0YXIvNDZhM2ZkYjkyODQzYWIzNzZlZTI5NjBkZmU2MThkZjc_cz00ODAmcj1wZyZkPWh0dHBzJTNBJTJGJTJGY2RuLmF1dGgwLmNvbSUyRmF2YXRhcnMlMkZyay5wbmciLCJ1cGRhdGVkX2F0IjoiMjAyMC0wNC0yMFQwODo1OTowNS45NzZaIiwiZW1haWwiOiJya290aGFwYWxsaUB0ZWtpb24uY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vdGVraW9uLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1OWYwY2U2YzJiNmYzODI1ZTAyMzU4NmYiLCJhdWQiOiJGNDd2UWRQanZpNFd4UlA0dTBKMkVnVHVsUTdRRXp4eSIsImlhdCI6MTU4NzM3MzE0NiwiZXhwIjoxNTg3NDA5MTQ2fQ.f37ePOFyQVi0vn7PNER-1L_4pNw2UhPEVnFQauhwkTg7ZX9duXZSjIiB9IBJxmoaG8WeJyD9R02xml-QgQPdXVIG-yOBq6CL6RsePw2iTeALTvnMCKURdNHbPfghJmoAGB5xqWk2DpPuhjfArMzI4M5YiBqGQjV5IaIOcmmgKsBHK5UiO90oYjTt3g73qbDDTwLsBxU2TdLmnNOTdBhhGWjxfpUCv1iRePDRp-bEXVyen5SDmbY5YWXBlcHCOt0NmP8vTkVT56tnUq4-Le8UxumWDw3IMwdg0fS4Vu_H-50M0FRPHfBIkGm-h_F0qEHiJnrXXrB-PXyqFW6APE8VWw"""

query = {'vin':'1G1ZD5ST0LF019724', 'includeRaw': 'true'}

headers = {'dealerid': '5', 'roleid': '5', 'tenantid': 'cacargroup', 'tenantname': 'cacargroup', 
'userid': '51', 'Content-Type': 'application/json', 'tekion-api-token' : api_token}

def fire_get_request(url, headers, params, timeout):
    start_time = time.time()
    response=requests.get(url, headers = headers, params = params, timeout=timeout)
    end_time=time.time() - start_time
    return {'responsetime':end_time,'response':response}


class VehicleHistoryApiCall(unittest.TestCase):

    def test_1234(self):
        """
        Test for HTTP level status code validation for Vehicle History API
        """
        logger.info("test_1234: Test for HTTP level status code validation for Vehicle History API")
        output = fire_get_request(url, headers, query, 30)
        http_response = output['response']
        
        logger.info("HTTP status code: {}".format(http_response.status_code))
        logger.debug("Response Body: {}".format(http_response.text))
        logger.debug("Response Time: {}".format(output['responsetime']))
    
        self.assertEqual(http_response.status_code, 200, "200 OK Status Code Validation Failed")

    def test_1235(self):
        """
        Test for VIN validation from the Vehicle History API
        """
        logger.info("test_1235: Test for VIN validation from the Vehicle History API")
        output = fire_get_request(url, headers, query, 30)
        json_response = output['response'].json()
        
        logger.info("HTTP status code: {}".format(output['response'].status_code))
        logger.debug("Response Body: {}".format(output['response'].text))
        logger.debug("Response Time: {}".format(output['responsetime']))
        
        vid_from_api = json_response["consolidated"]["VehicleSpecifications"]["VehicleSpecificationsLine"][0]["Vehicle"]["VehicleID"]

        self.assertEqual(vid_from_api, query['vin'], "VIN Validation Failed")
    
    def test_1236(self):
        """
        Test for Company/OEM validation from the Vehicle History API
        """
        logger.info("test_1236: Test for Company/OEM validation from the Vehicle History API")
        output = fire_get_request(url, headers, query, 30)
        json_response = output['response'].json()

        logger.info("HTTP status code: {}".format(output['response'].status_code))
        logger.debug("Response Body: {}".format(output['response'].text))
        logger.debug("Response Time: {}".format(output['responsetime']))

        company_name = json_response["consolidated"]["VehicleSpecifications"]["VehicleSpecificationsHeader"]["ManufacturerParty"]["SpecifiedOrganization"]["CompanyName"]
        oem = json_response["oem"]
        
        self.assertTrue(company_name is not None, "Null value in company name found")
        self.assertTrue(oem is not None, "Null value in OEM  found")

if __name__ == '__main__':
    unittest.main()