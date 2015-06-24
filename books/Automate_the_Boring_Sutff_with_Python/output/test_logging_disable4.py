import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.critical('Critical error! Critical error!')
logging.disable(logging.ERROR)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')