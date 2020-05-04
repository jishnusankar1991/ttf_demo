import requests
import time
import json
import unittest

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

        output = fire_get_request(url, headers, query, 30)
        http_response = output['response']
    
        self.assertEqual(http_response.status_code, 200, "200 OK Status Code Validation Failed")

    def test_1235(self):
        """
        Test for VIN validation from the Vehicle History API"
        """

        output = fire_get_request(url, headers, query, 30)
        json_response = output['response'].text
        json_op = json.loads(json_response)
        vid_from_api = json_op["consolidated"]["VehicleSpecifications"]["VehicleSpecificationsLine"][0]["Vehicle"]["VehicleID"]

        self.assertEqual(vid_from_api, query['vin'], "VIN Validation Failed")
    
    def test_1236(self):
        """
        Test for Company/OEM validation from the Vehicle History API"
        """

        output = fire_get_request(url, headers, query, 30)
        json_response = output['response'].text
        json_op = json.loads(json_response)
        company_name = json_op["consolidated"]["VehicleSpecifications"]["VehicleSpecificationsHeader"]["ManufacturerParty"]["SpecifiedOrganization"]["CompanyName"]
        oem_name = json_op["oem"]
        self.assertTrue(company_name is not None, "Null value in company name found")
        self.assertTrue(oem_name is not None, "Null value in OEM name found")

if __name__ == '__main__':
    unittest.main()