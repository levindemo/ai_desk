import logging
import os


# create method to create logger in this project
# so we can use it in other modules and configure the log to standard output and IO and logger format

def create_logger():
    logger = logging.getLogger(__name__)
    # set default as info or env var AIDESK_LOG_LEVEL
    logger.setLevel(os.environ.get('AIDESK_LOG_LEVEL', 'INFO'))
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # if console log enable in env
    if os.environ.get('AIDESK_CONSOLE_LOG') == 'TRUE':
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    # if log to filesystem enable in env
    if os.environ.get('AIDESK_FILE_LOG') == 'TRUE':
        # if log file path not set, use default
        log_file_path = os.environ.get('AIDESK_LOG_FILE_PATH', 'aidesk.log')
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    # if log to remote server log disable in env
    if os.environ.get('AIDESK_REMOTE_LOG') == 'TRUE':
        # if log server url not set, use default
        # log_server_url = os.environ.get('AIDESK_LOG_SERVER_URL', 'http://localhost:8000/log')
        # create http handler
        # http_handler = logging.handlers.HTTPHandler(log_server_url, '/log')
        # http_handler.setFormatter(formatter)
        # logger.addHandler(http_handler)
        # not implemented
        raise NotImplementedError('remote log handler not implemented')
    return logger


# sample code to use logger
if __name__ == '__main__':
    logger = create_logger()
    logger.info('this is a info log')
    logger.error('this is a error log')
    logger.debug('this is a debug log')
    logger.exception('this is a exception log')
