def example3():
    try:
        int('N/A')
    except ValueError:
        raise RuntimeError('A parsing error occurred') from None
        
example3()