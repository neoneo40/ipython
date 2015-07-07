import sys
 
 
def fx(qq, loop_cnt, k):
    idx = 0
    max_cnt = len(qq)
 
    for i in xrange(loop_cnt):
        qq.pop(idx)
        max_cnt -= 1
        idx = idx + k - 1
 
        if idx >= max_cnt:
            idx = idx % (max_cnt)
 
    print qq[0], qq[1]
 
 
def main():
    test_count = sys.stdin.readline()
    test_count = int(test_count)
 
    test_param = []
 
    for i in xrange(test_count):
        hap_sig = sys.stdin.readline()
        a, b = hap_sig[:-1].split()
        test_param.append( ( int(a), int(b) ))
 
    for n, k in test_param:
        loop_cnt = n - 2    # loop_cnt == killed persons count
        saram = [ x for x in xrange(1,n+1)]
        fx(saram, loop_cnt, k)
 
 
if __name__ == '__main__':
    main()