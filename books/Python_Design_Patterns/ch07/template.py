# -*- coding: utf-8
import urllib2
from xml.dom import minidom


class AbstractNewsParser(object):
    def __init__(self):
        # 클래스 인스턴스 생성 방지
        if self.__class__ is AbstractNewsParser:
            raise TypeError('abstract class cannot be instantiated')

    def print_top_news(self):
        '''템플릿 메소드. 모든 웹사이트에서 3개의 최신 뉴스를 반환한다.'''
        url = self.get_url()
        raw_content = self.get_raw_content(url)
        content = self.parse_content(raw_content)

        cropped = self.crop(content)

        for item in cropped:
            print 'Title: ', item['title']
            print 'Content: ', item['content']
            print 'Link: ', item['link']
            print 'Published: ', item['published']
            print 'Id: ', item['id']

    def get_url(self):
        raise NotImplementedError()

    def get_raw_content(self, url):
        return urllib2.urlopen(url).read()

    def parse_content(self, content):
        raise NotImplementedError()

    def crop(self, parsed_content, max_items=3):
        return parsed_content[:max_items]


class YahooParser(AbstractNewsParser):
    def get_url(self):
        return 'http://news.yahoo.com/rss/'

    def parse_content(self, raw_content):
        parsed_content = []

        dom = minidom.parseString(raw_content)
        for node in dom.getElementsByTagName('item'):
            parsed_item = {}
            try:
                parsed_item['title'] = node.getElementsByTagName('title')[0].\
                childNodes[0].nodeValue
            except IndexError:
                parsed_item['title'] = None

            try:
                parsed_item['content'] = \
                    node.getElementsByTagName('description')[0].\
                        childNodes[0].nodeValue
            except IndexError:
                parsed_item['content'] = None

            try:
                parsed_item['link'] = \
                node.getElementsByTagName('link')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['id'] = None

            try:
                parsed_item['published'] = \
                node.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['published'] = None

            parsed_content.append(parsed_item)
        return parsed_content


class GoogleParser(AbstractNewsParser):
    def get_url(self):
        return 'https://news.google.com/news/feeds?output=atom'

    def parse_content(self, raw_content):
        parsed_content = []
        dom = minidom.parseString(raw_content)
        for node in dom.getElementsByTagName('entry'):
            parsed_item = {}
            try:
                parsed_item['title'] = \
                    node.getElementsByTagName('title')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['title'] = None

            try:
                parsed_item['content'] = \
                node.getElementsByTagName('content')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['content'] = None

            try:
                parsed_item['link'] = \
                node.getElementsByTagName('link')[0].getAttribute('href')
            except IndexError:
                parsed_item['link'] = None

            try:
                parsed_item['id'] = \
                node.getElementsByTagName('id')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['id'] = None

            try:
                parsed_item['published'] = \
                node.getElementsByTagName('updated')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['published'] = None

            parsed_content.append(parsed_item)

        return parsed_content


if __name__ == '__main__':
    google = GoogleParser()
    yahoo = YahooParser()

    print 'Google: \n', google.print_top_news()
    print 'Yahoo: \n', yahoo.print_top_news()