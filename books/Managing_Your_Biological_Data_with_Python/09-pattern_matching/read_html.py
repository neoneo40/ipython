'''
Parse abstracts from PubMed HTML pages.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 9.4.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

import urllib2
import re

pmid = '18235848'
url = 'http://www.ncbi.nlm.nih.gov/pubmed?term=%s' % pmid
handler = urllib2.urlopen(url)
html = handler.read()

title_regexp = re.compile('<h1>.{5,400}</h1>')
title_text = title_regexp.search(html)
abstract_regexp = re.compile('<h3>Abstract</h3><p>.{20,3000}</p></div>')
abstract_text = abstract_regexp.search(html)

print 'TITLE:', title_text.group() 
print 'ABSTRACT:', abstract_text.group()
