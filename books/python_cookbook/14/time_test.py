def add(a, b):
    return a + b

def main(MAX):
    total = 0
    for i in range(MAX):
        total += add(i, i)
        
main(10000000)