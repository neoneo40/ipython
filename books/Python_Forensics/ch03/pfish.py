
# coding: utf-8
import logging
import time
import sys
import _pfish


if __name__ == '__main__':
    PFISH_VERSION = '1.0'

    # 로깅을 설정한다.
    logging.basicConfig(filename='pFishLog.log',
                        level=logging.DEBUG,
                        format='%(asctime)s %(message)s')

    # 명령줄 인수 처리
    _pfish.ParseCommandLine()

    # 시작하는 시간 기록
    startTime = time.time()

    # 환영 메시지 기록
    logging.info('')
    logging.info('Welcome to p-fish version {} ... New Scan Started'.format(
            PFISH_VERSION))
    logging.info('')
    _pfish.DisplayMessage('Welcome to p-fish ... version'.format(PFISH_VERSION))

    # 시스템과 관련한 일부 정보 기록
    logging.info('System: {}'.format(sys.platform))
    logging.info('Version: {}'.format(sys.version))

    # 파일 시스템 디렉토리 및 해시 파일을 횡단함
    fileProcessed = _pfish.WalkPath()

    # 종료 시간을 기록하고 기간을 계산
    endTime = time.time()
    duration = endTime - startTime
    logging.info('Files Processed:' + str(fileProcessed))
    logging.info('Elapsed Time: ' + str(duration) + 'seconds')
    logging.info('')
    logging.info('Program Terminated Normally')
    logging.info('')

    _pfish.DisplayMessage('Program End')