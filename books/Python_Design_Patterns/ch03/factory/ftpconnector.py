from books.Python_Design_Patterns.ch03.factory.connector import Connector


class FTPConnector(Connector):
    '''FTP 커넥터를 생성하고 모든 속성을 실행 시간에 설정하는 실제 생성자'''
    def protocol_factory_method(self):
        return 'ftp'

    def port_factory_method(self):
        return FTPPort()

    def parse(self, content):
        lines = content.split('\n')
        filenames = []
        for line in lines:
            # 일반적으로 FTP 포맷은 열을 8개 가지고 있음. 이것을 나누어 주자
            splitted_line = line.split(None, 8)
            if len(splitted_line) == 9:
                filenames.append(splitted_line[-1])
        return '\n'.join(filenames)