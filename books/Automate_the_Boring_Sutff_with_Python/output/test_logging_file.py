import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.critical('Critical error! Critical error!')
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
logging.debug('Debug!')
logging.info('Info!')