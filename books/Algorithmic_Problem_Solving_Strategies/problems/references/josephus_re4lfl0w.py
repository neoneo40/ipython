# -*- coding: utf-8
def josephus(N, K):
    # list를 준비한다.
    lst = range(1, N+1)
    i = 0
    # list에서 skip할 index
    skip = K - 1
    # 2명이 남을 때까지 계속 loop
    # list의 값 계산을 한 번만 하기 위해서
    max_ = len(lst)
    while 2 < max_:
        # index가 max_의 값을 넘게 되면 새로운 index를 설정해 줌
        # 이 부분이 가장 중요하다. 새로운 index를 설정해줘야 logic이 정상 동작함
        while i >= max_:
            i = i - max_
        # index의 값을 kill
        lst.pop(i)
        # list의 값 계산을 한 번만 하기 위해서
        max_ = len(lst)
        # i에 계속 skip할 index를 더한다.
        i += skip
    return lst

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        string_ = raw_input()
        N, K = (int(n) for n in string_.split())
        result = josephus(N, K)
        print result[0], result[1]