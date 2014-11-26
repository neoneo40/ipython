def example():
    try:
        int('N/A')
    except ValueError:
        print("Didn't work")
        raise
        
example()