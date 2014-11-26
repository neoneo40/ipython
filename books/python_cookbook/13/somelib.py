
import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

# 예제 함수(테스팅)
def func():
    log.critical('A critical Error!')
    log.debug('A debug message')