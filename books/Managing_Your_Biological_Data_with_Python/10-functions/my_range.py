def my_range(start=None, stop=None, step=1):
    if start and stop:
        start = start
        stop = stop
    if start and not stop:
        start = 0
        stop = start
    while start >= stop:
        print start
        start += step