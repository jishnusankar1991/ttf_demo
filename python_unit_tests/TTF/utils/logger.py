import logging
import time

try:
    NullHandler = logging.NullHandler

except AttributeError:
    class NullHandler(logging.Handler):
        '''This handler does nothing'''
        def emit(self, record):
            '''do nothing'''


def ttf_logger(name):
    '''Creates a logger that is a child of the current root logger

    @param name usually the __name__ module variable

    @retval instance of a logger suitable for a module
    '''

    #logname = 'testcase.%s' % (name)
    logger = logging.getLogger(name)
    #logger.addHandler(NullHandler())
    

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

    file_handler = logging.FileHandler('C:\\Users\\jishn\\TTF\\test_results\\test_vehicle_history_api-{time_stamp}.log'.format(time_stamp = time.strftime('%Y-%m-%d-%H%M%S')))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    #stream_handler = logging.StreamHandler()
    #stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    #logger.addHandler(stream_handler)

    return logger