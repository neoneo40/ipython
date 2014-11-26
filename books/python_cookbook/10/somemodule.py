def spam():
    print('spam method')

def grok():
    print('grok method')

blah = 42

# 'spam'과 'grok'만 내보낸다.
__all__ = ['spam', 'grok', 'blah']