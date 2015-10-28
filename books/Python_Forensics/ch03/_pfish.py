
# coding: utf-8
import os
import stat
import time
import hashlib
import argparse
import csv
import logging

log = logging.getLogger('main._pfish')


def ParseCommandLine():
    parser = argparse.ArgumentParser('Python file system hashing... p-fish')

    parser.add_argument('-v',
                        '--verbose',
                        help='allows progress messages to be displayed',
                        action='store_true')

    # 상호 베타적인 선택이 필요한 그룹 설정
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--md5',
                       help='specifies MD5 algorithm',
                       action='store_true')
    group.add_argument('--sha256',
                       help='specifies SHA256 algorithm',
                       action='store_true')
    group.add_argument('--sha512',
                       help='specifies SHA512 algorithm',
                       action='store_true')

    parser.add_argument('-d',
                        '--rootPath',
                        type=ValidateDirectory,
                        required=True,
                        help='specify the root path for hashing')
    parser.add_argument('-r',
                        '--reportPath',
                        type=ValidateDirectoryWritable,
                        required=True,
                        help='specify the path for reports and logs will be written')

    # 검증된 인수를 보유한 전역 객체를 생성
    # 이 객체는 _pfish.py 모듈 내의 모든 함수에서 사용 가능

    global gl_args
    global gl_hashType

    gl_args = parser.parse_args()

    if gl_args.md5:
        gl_hashType = 'MD5'
    elif gl_args.sha256:
        gl_hashType = 'SHA256'
    elif gl_args.sha512:
        gl_hashType = 'SHA512'
    else:
        gl_hashType = 'UnKnown'
        logging.error('Unknown Hash Type Specified')

    DisplayMessage('Command line processed: Successfully')
    return


def WalkPath():
    processCount = 0
    errorCount = 0

    oCVS = _CSVWriter(os.path.join(gl_args.reportPath, 'fileSystemReport.csv'),
                      gl_hashType)

    # rootPath에서 시작하는 모든 파일을 처리하는 반복문을 만들고,
    # 모든 하위 디렉토리도 처리된다.

    log.info('Root Path: ' + gl_args.rootPath)

    for root, dirs, files in os.walk(gl_args.rootPath):
        # for문은 각 파일에 대한 파일 이름을 획득하고 HashFile 함수를 호출한다.
        for file in files:
            fname = os.path.join(root, file)
            result = HashFile(fname, file, oCVS)

            # 해시 연산이 성공한 경우, ProcessCount가 증가한다.
            if result is True:
                processCount += 1
            # 성공하지 못한 경우, ErrorCount가 증가한다.
            else:
                errorCount += 1

    oCVS.writerClose()
    return(processCount)


def HashFile(theFile, simpleName, o_result):
    """
    Must Refactoring.
    """
    # 경로가 유효한지 확인한다.
    if os.path.exists(theFile):
        # 경로가 심볼 링크가 아닌지 확인한다.
        if not os.path.islink(theFile):
            # 파일이 실재하는지 확인
            if os.path.isfile(theFile):
                try:
                    # 파일 열기 시도
                    f = open(theFile, 'rb')
                except IOError:
                    # 열기에 실패하는 경우, 오류를 보고
                    log.warning('Open Failed: ' + theFile)
                    return
                else:
                    try:
                        # 파일 읽기 시도
                        rd = f.read()
                    except IOError:
                        # 읽기에 실패하는 경우, 파일을 닫고 오류 보고
                        f.close()
                        log.warning('Read Failed: ' + theFile)
                        return
                    else:
                        # 파일 열기가 성공하면 이 파일로부터 읽을 수 있음
                        # 파일의 상태를 조회

                        theFileStats = os.stat(theFile)
                        (mode, ino, dev, nlink, uid, gid, size,
                         atime, mtime, ctime) = os.stat(theFile)

                        # 단순한 파일 이름을 인쇄
                        DisplayMessage('Processing File: ' + theFile)

                        # 파일의 바이트(Byte) 크기를 인쇄
                        fileSize = str(size)

                        # 수정/접근/속성변경 시간을 인쇄
                        modifiedTime = time.ctime(mtime)
                        accessTime = time.ctime(atime)
                        createdTime = time.ctime(ctime)

                        ownerID = str(uid)
                        groupID = str(gid)
                        fileMode = bin(mode)

                        # 파일 해시를 처리

                        if gl_args.md5:
                            # MD5 계산 및 인쇄
                            hashValue = hashlib.md5(rd).hexdigest()
                        elif gl_args.sha256:
                            hashValue = hashlib.sha256(rd).hexdigest()
                        elif gl_args.sha512:
                            hashValue = hashlib.sha512(rd).hexdigest()
                        else:
                            log.error('Hash not Selected')

                            # 파일 처리가 완료되면
                            # 활성 상태의 파일을 닫는다.
                            print('=' * 20)
                            f.close()

                        # 출력 파일에 한 행을 기록함
                        o_result.writeCSVRow(simpleName, theFile, fileSize,
                                             modifiedTime, accessTime, createdTime,
                                             hashValue, ownerID, groupID, mode)
                        return True
            else:
                log.warning('[{} Skipped NOT a File]'.format(repr(simpleName)))
                return False
        else:
            log.warning('[{} Skipped NOT a File]'.format(repr(simpleName)))
            return False
    else:
        log.warning('[{} Path does NOT a exist]'.format(repr(simpleName)))
        return False


def ValidateDirectory(theDir):
    # 디렉토리 경로의 유효성을 검사
    if not os.path.isdir(theDir):
        raise argparse.ArgumentTypeError('Directory does not exist')

    # 경로가 읽기 가능한지 검사
    if os.access(theDir, os.R_OK):
        return theDir
    else:
        raise argparse.ArgumentTypeError('Directory is not readable')


def ValidateDirectoryWritable(theDir):
    # 디렉토리 경로의 유효성 검사
    if not os.path.isdir(theDir):
        raise argparse.ArgumentTypeError('Directory does not exist')

    # 경로가 쓰기 가능한지 검사
    if os.access(theDir, os.W_OK):
        return theDir
    else:
        raise argparse.ArgumentTypeError('Directory is not writable')


def DisplayMessage(msg):
    if gl_args.verbose:
        print(msg)
    return


class _CSVWriter(object):
    def __init__(self, fileName, hashType):
        try:
            # writer 객체를 생성하고 머리글 행을 기록
            self.csvFile = open(fileName, 'wb')
            self.writer = csv.writer(self.csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            self.writer.writerow(('File', 'Path', 'Size', 'Modified Time', 'Access Time',
            'Created Time', hashType, 'Owner', 'Group', 'Mode'))
        except:
            log.error('CSV File Failure')

    def writeCSVRow(self, fileName, filePath, fileSize, mTime, aTime,
                    cTime, hashVal, own, grp, mod):
        self.writer.writerow((fileName, filePath, fileSize, mTime,
        aTime, cTime, hashVal, own, grp, mod))

    def writerClose(self):
        self.csvFile.close()