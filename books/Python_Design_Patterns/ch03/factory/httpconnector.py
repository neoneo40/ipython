from books.Python_Design_Patterns.ch03.factory.connector import Connector


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