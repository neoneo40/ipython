
# coding: utf-8
import httplib2
import os
import re
import threading
import urllib
from urlparse import urlparse, urljoin
from BeautifulSoup import BeautifulSoup


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    

class ImageDownloaderThread(threading.Thread):
    """ 병렬적으로 이미지를 다운로드 받는 스레드"""
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.name = name
        
    def run(self):
        print('Starting thread ', self.name)
        download_images(self.name)
        print('Finished thread ', self.name)
        
def traverse_site(max_links=10):
    link_parser_singleton = Singleton()

    # 큐에 파싱할 페이지가 있는 동안
    while link_parser_singleton.queue_to_parse:
        # 이미지를 내렵다을 링크를 충분히 모은 경우, 반환
        if len(link_parser_singleton.to_visit) == max_links:
            return

        url = link_parser_singleton.queue_to_parse.pop()

        http = httplib2.Http()
        try:
            status, response = http.request(url)
        except Exception:
            continue

        # 웹페이지가 아닌 경우 건너뛴다.
        if status.get('content-type') != 'text/html':
            continue

        # 이미지를 내려받기 위해 링크를 큐에 추가한다.
        link_parser_singleton.to_visit.add(url)
        print('Added', url, 'to queue')

        bs = BeautifulSoup(response)

        for link in BeautifulSoup.findAll(bs, 'a'):
            link_url = link.get('href')

            # <img> 태그에 href 속성이 없을 수도 있음
            if not link_url:
                continue

            parsed = urlparse(link_url)

            # 링크가 외부 웹페이지로 연결된다면 건너뜀
            if parsed.netloc and parsed.netloc != parsed.root.netloc:
                continue

            # 상대 경로를 사용한 링크를 전체 경로로 변환함
            link_url = (parsed.scheme or parsed_root.scheme) + '://' + \
            (parsed.netloc or parsed_root.netloc) + parsed.path or ''

            # 중복된 링크일 경우 건너뛴다.
            if link_url in link_parser_singleton.to_visit:
                continue

            # 파싱을 위해 링크를 추가한다.
            link_parser_singleton.queue_to_parse = [link_url] + \
            link_parser_singleton.queue_to_parse


def download_images(thread_name):
    singleton = Singleton()
    while singleton.to_visit:
        url = httplib2.Http()
        print thread_name, 'Starting downloading images from', url
        
        try:
            status, response = http.request(url)
        except Exception:
            continue
        
        bs = BeautifulSoup(response)
        
        # 모든 <img> 태그를 찾는다.
        images = BeautifulSoup.findAll(bs, 'img')
        
        for image in images:
            # 절대 혹은 상대 경로 url로 된 이미지 소스를 얻는다.
            src = image.get('src')
            # 전체 url을 만든다. 만약 이미지 url이 상대 경로라면
            # 웹페이지 도메인과 함께 확장된다.
            # url이 절대 경로라면 그대로 진행한다.
            src = urljoin(url, src)
            
            # 베이스 이름을 얻는다. 예를 들어 로컬 이름 파일에 image.png를 의미한다.
            basename = os.path.basename(src)
            
            if src not in singleton.downloaded:
                singleton.downloaded.add(src)
                print('Downloading', src)
                # 로컬 파일시스템에서 이미지를 다운로드 받는다.
                urllib.urlretrieve(src, os.path.join('images', basename))
                
        print(thread_name, 'finished downloading images from', url)
        
        
if __name__ == '__main__':
    root = 'http://python.org'
    parsed_root = urlparse(root)
    singleton = Singleton()
    singleton.queue_to_parse = [root]
    # A set of urls to download images from
    singleton.to_visit = set()
    # Downloaded images
    singleton.downloaded = set()
    
    traverse_site()
    
    # Create images directory if not exists
    if not os.path.exists('images'):
        os.makedirs('images')
        
    # Create new threads
    thread1 = ImageDownloaderThread(1, 'Thread-1', 1)
    thread2 = ImageDownloaderThread(2, 'Thread-2', 2)
    
    # Start new Threads
    thread1.start()
    thread2.start()