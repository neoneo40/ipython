def do_case(n, ok):
    a = range(2, n+1)
    la = len(a)
    k = 0
    while la > 2:
        k = (k + ok - 1) % la
        a.pop(k)
        la -= 1
    return a


if __name__ == "__main__":
    c = int(raw_input())
    for i in range(c):
        n, k = [int(v) for v in raw_input().split()]
        f, s = do_case(n, k)
        print f, s