import requests
import time
from utils.logger import ttf_logger

logger = ttf_logger(__name__)


def fire_get_request(url, headers, params, timeout):
    start_time = time.time()
    response=requests.get(url, headers = headers, params = params, timeout=timeout)
    end_time=time.time() - start_time

    logger.debug("Response Body: {}".format(response.text))
    logger.debug("Response Time: {}".format(end_time))

    return {'responsetime':end_time,'response':response}

def fire_post_request(url, headers, data, timeout):
    start_time = time.time()
    response=requests.post(url, headers = headers, json = data, timeout=timeout)
    end_time=time.time() - start_time

    logger.debug("Response Body: {}".format(response.text))
    logger.debug("Response Time: {}".format(end_time))

    return {'responsetime':end_time,'response':response}