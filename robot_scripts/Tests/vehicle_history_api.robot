*** Settings ***
Library  RequestsLibrary
Library  Collections
Library  JSONLibrary


*** Variable ***
${base_url}=    https://api.tekion.xyz/api/integration
${api_token}=    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6SXdOREF3UXpOQk0wRkVNelZFTmpNMU5UQXhSREEzUXpjM1FqVkZNalUxTVRrME1EbERSQSJ9.eyJuaWNrbmFtZSI6InJrb3RoYXBhbGxpIiwibmFtZSI6InJrb3RoYXBhbGxpQHRla2lvbi5jb20iLCJwaWN0dXJlIjoiaHR0cHM6Ly9zLmdyYXZhdGFyLmNvbS9hdmF0YXIvNDZhM2ZkYjkyODQzYWIzNzZlZTI5NjBkZmU2MThkZjc_cz00ODAmcj1wZyZkPWh0dHBzJTNBJTJGJTJGY2RuLmF1dGgwLmNvbSUyRmF2YXRhcnMlMkZyay5wbmciLCJ1cGRhdGVkX2F0IjoiMjAyMC0wNC0yMFQwODo1OTowNS45NzZaIiwiZW1haWwiOiJya290aGFwYWxsaUB0ZWtpb24uY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vdGVraW9uLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1OWYwY2U2YzJiNmYzODI1ZTAyMzU4NmYiLCJhdWQiOiJGNDd2UWRQanZpNFd4UlA0dTBKMkVnVHVsUTdRRXp4eSIsImlhdCI6MTU4NzM3MzE0NiwiZXhwIjoxNTg3NDA5MTQ2fQ.f37ePOFyQVi0vn7PNER-1L_4pNw2UhPEVnFQauhwkTg7ZX9duXZSjIiB9IBJxmoaG8WeJyD9R02xml-QgQPdXVIG-yOBq6CL6RsePw2iTeALTvnMCKURdNHbPfghJmoAGB5xqWk2DpPuhjfArMzI4M5YiBqGQjV5IaIOcmmgKsBHK5UiO90oYjTt3g73qbDDTwLsBxU2TdLmnNOTdBhhGWjxfpUCv1iRePDRp-bEXVyen5SDmbY5YWXBlcHCOt0NmP8vTkVT56tnUq4-Le8UxumWDw3IMwdg0fS4Vu_H-50M0FRPHfBIkGm-h_F0qEHiJnrXXrB-PXyqFW6APE8VWw
${vin}=    1G1ZD5ST0LF019724

*** Test Cases ***
TC_001: Test for HTTP level status code validation for Vehicle History API
    [Tags]    Sanity
    ${Headers}=    Create Dictionary    dealerid=5    roleid=5    tenantid=cacargroup    tenantname=cacargroup    userid=51    Content-Type=application/json    tekion-api-token=${api_token}
    ${query_params}=    Create Dictionary    vin=${vin}    includeRaw=true
    Create Session    VehicleHistoryApi    ${base_url}
    ${Response}=    Get Request    VehicleHistoryApi    /vehicleHistory/vehicleSpecs/vinLookup    headers=${Headers}    params=${query_params}
    Log    ${Response.status_code}
    Log    ${Response.content}
    Should Be Equal As Strings    ${Response.status_code}    200

TC_002: Test for VIN validation from the Vehicle History API
    [Tags]    Regression
    ${Headers}=    Create Dictionary    dealerid=5    roleid=5    tenantid=cacargroup    tenantname=cacargroup    userid=51    Content-Type=application/json    tekion-api-token=${api_token}
    ${query_params}=    Create Dictionary    vin=${vin}    includeRaw=true
    Create Session    VehicleHistoryApi    ${base_url}
    ${Response}=    Get Request    VehicleHistoryApi    /vehicleHistory/vehicleSpecs/vinLookup    headers=${Headers}    params=${query_params}
    ${json_object}=    To Json    ${Response.content}  
    ${response_vin}=    Get Value From Json    ${json_object}    $.consolidated.VehicleSpecifications.VehicleSpecificationsLine[0].Vehicle.VehicleID
    Log    ${response_vin[0]}
    Should Be Equal As Strings    ${vin}    ${response_vin[0]}

TC_003: Test for Company/OEM validation from the Vehicle History API
    [Tags]    Regression1
    ${Headers}=    Create Dictionary    dealerid=5    roleid=5    tenantid=cacargroup    tenantname=cacargroup    userid=51    Content-Type=application/json    tekion-api-token=${api_token}
    ${query_params}=    Create Dictionary    vin=${vin}    includeRaw=true
    Create Session    VehicleHistoryApi    ${base_url}
    ${Response}=    Get Request    VehicleHistoryApi    /vehicleHistory/vehicleSpecs/vinLookup    headers=${Headers}    params=${query_params}
    ${json_object}=    To Json    ${Response.content}  
    ${response_vin}=    Get Value From Json    ${json_object}    $.consolidated.VehicleSpecifications.VehicleSpecificationsHeader.ManufacturerParty.SpecifiedOrganization.CompanyName
    Log    ${response_vin[0]}
    Should Not Be Equal    ${response_vin[0]}    ${EMPTY}