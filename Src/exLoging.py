import logging

# create logger
logging.basicConfig(filename='example2.log',level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)


# 'application' code
logger.debug('debug message')
logger.info('')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
logger.error('error message')