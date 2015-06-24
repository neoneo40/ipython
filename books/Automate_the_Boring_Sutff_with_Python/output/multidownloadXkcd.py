import requests
import os
import bs4
import threading
import re
import urlparse

if not os.path.exists('xkcd'):
    os.makedirs('xkcd')
    
def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page http://xkcd.com/{}...'.format(urlNumber))
        res = requests.get('http://xkcd.com/{}'.format(urlNumber))
        res.raise_for_status()
        
        soup = bs4.BeautifulSoup(res.text)
        
        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
        if comicUrl.startswith('/') or not 'http' in comicUrl:
            comicUrl = urlparse.urljoin('http://xkcd.com', comicUrl)
            
        # TODO: Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    
        # TODO: Save the image to ./xkcd.
        with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as imageFile:
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
                
def main():
    # TODO: Create and start the Thread objects.
    downloadThreads = [] # a list of all the Thread objects
    for i in range(0, 1600, 100): # loops 14 times, creates 14 threads
        # i+100 is correct. not i+99
        downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+100))
        downloadThreads.append(downloadThread)
        downloadThread.start()
    # TODO: Wait for all threads to end.
    for downloadThread in downloadThreads:
        downloadThread.join()
    print('Done.')
    
if __name__ == '__main__':
    main()