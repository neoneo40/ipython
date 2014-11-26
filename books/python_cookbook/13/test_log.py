
import logging

def main():
    # 로그 시스템 환경 설정
    logging.basicConfig(filename='app.log',
                        level=logging.ERROR)
    
    # 변수(작업을 따르는 호출을 하기 위해서)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'
    
    # 예제 로그 호출(프로그램에 삽입)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')
    
if __name__ == '__main__':
    main()