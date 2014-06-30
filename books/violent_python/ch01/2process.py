from multiprocessing import Process, Queue

def do_work(start, end, result):
    sum = 0
    for i in range(start, end):
        sum += i
    result.put(sum)
    return

if __name__ == '__main__':
    START, END = 0, 20000000
    result = Queue()
    pr1 = Process(target=do_work, args=(START, END/2, result))
    pr2 = Process(target=do_work, args=(END/2, END, result))
    pr1.start()
    pr2.start()
    pr1.join()
    pr2.join()
    result.put('STOP')
    sum = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            sum += tmp
print 'Result : ', sum