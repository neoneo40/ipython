
# -*- coding: utf-8
def josephus(N, K):
    # list를 준비한다. range 특성상 마지막은 +1을 해줘야 됨
    lst = range(1, N+1)
    i = 0
    # list에서 skip할 index
    skip = K - 1
    # list의 값 계산을 한 번만 하기 위해서
    max_ = len(lst)
    # 2명이 남을 때까지 계속 loop
    while 2 < max_:
        # index가 max_의 값을 넘게 되면 새로운 index를 설정해 줌
        # 이 부분이 가장 중요하다. 새로운 index를 설정해줘야 logic이 정상 동작함
        # i = 28, max_ = 26 일시 28 - 26 = 2, i를 2로 설정
        while i >= max_:
            i = i - max_
        # index의 값을 kill
        lst.pop(i)
        # list의 값 계산을 한 번만 계산하기 위해서
        max_ = len(lst)
        # i에 계속 skip할 index를 더한다.
        i += skip
    return lst

def main():
    n = int(raw_input())
    params = []
    for i in range(n):
        string_ = raw_input()
        N, K = (int(n) for n in string_.split())
        params.append([N, K])
    for N, K in params:
        result = josephus(N, K)
        print result[0], result[1]

if __name__ == '__main__':
    main()