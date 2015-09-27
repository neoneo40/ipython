class SimpleFactory(object):
    # 이 데코레이터는 메소드가 클래스 인스턴스 없이 실행할 수 있게 함
    # SimpleFactory.build_connect
    @staticmethod
    def build_connection(protocol):
        if protocol == 'http':
            return HTTPConnection()
        elif protocol == 'ftp':
            return FTPConnection()
        else:
            raise RuntimeError('Unknown protocol')


if __name__ == '__main__':
    protocol = raw_input('Which Protocol to use? (http or ftp): ')
    protocol = SimpleFactory.build_connection(protocol)
    protocol.connect()
    print protocol.get_response()