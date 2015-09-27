# -*- coding: utf-8

import abc
import urllib2
from BeautifulSoup import BeautifulStoneSoup


class Connector(object):
    '''원격 서버에 연결하기 위한 추상 클래스'''
    __metaclass__ = abc.ABCMeta

    def __init__(self, is_secure):
        self.is_secure = is_secure
        self.port = self.port_factory_method()
        self.protocol = self.protocol_factory_method()

    @abc.abstractmethod
    def parse(self):
        '''웹 콘텐츠를 파싱한다.
        이 메소드는 실행 시간에 재정의해야만 한다.'''
        pass

    def read(self, host, path):
        '''모든 클래스에 대한 일반 메소드로, 웹 콘텐츠를 읽는다.'''
        url = self.protocol + '://' + host + ':' + str(self.port) + path
        print 'Connecting to ', url
        return urllib2.urlopen(url, timeout=2).read()

    @abc.abstractmethod
    def protocol_factory_method(self):
        '''서브 클래스에서 반드시 재정의해야 하는 팩토리 메소드'''
        pass

    @abc.abstractmethod
    def port_factory_method(self):
        '''서브 클래스에서 반드시 재정의해야 하는 또 다른 팩토리 메소드'''
        return FTPPort()


class HTTPConnector(Connector):
    '''HTTP 커넥터를 생성하고 모든 속성을 실행 시간에 설정하는 실제 생성자'''
    def protocol_factory_method(self):
        if self.is_secure:
            return 'https'
        return 'http'

    def port_factory_method(self):
        '''HTTPPort와 HTTPSecurePort는 실제 객체로, 팩토리 메소드에서 생성한 것이다.'''
        if self.is_secure:
            return HTTPSecurePort()
        return HTTPPort()

    def parse(self, content):
        '''웹 콘텐츠 파싱'''
        filenames = []
        soup = BeautifulStoneSoup(content)
        links = soup.table.findAll('a')
        for link in links:
            filenames.append(link['href'])
        return '\n'.join(filenames)


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


class Port(object):
    __metaclass__ = abc.ABCMeta
    '''추상 생성물. 이 중 하나의 서브클래스는 팩토리 메소드에서 생성된다.'''

    @abc.abstractmethod
    def __str__(self):
        pass


class HTTPPort(Port):
    '''http 포트를 나타내는 실제 생성물'''
    def __str__(self):
        return '80'


class HTTPSecurePort(Port):
    '''https 포트를 나타내는 실제 생성물'''
    def __str__(self):
        return '443'


class FTPPort(Port):
    '''ftp 포트를 나타내는 실제 생성물'''
    def __str__(self):
        return '21'


if __name__ == '__main__':
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'

    protocol = input('Connecting to {}. Which Protocol to use? '
    '(0-http, 1-ftp): '.format(domain))

    if protocol == 0:
        is_secure = bool(input('Use secure connection? (1-yes, 0-no): '))
        connector = HTTPConnector(is_secure)
    else:
        is_secure = False
        connector = FTPConnector(is_secure)

    try:
        content = connector.read(domain, path)
    except urllib2.URLError, e:
        print 'Can not access resouce with this method'
    else:
        print connector.parse(content)