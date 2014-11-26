def example2():
    try:
        int('N/A')
    except ValueError as e:
        print("Couldn't parse:", err)
        
example2()