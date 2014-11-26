from collections import deque

class linehistory:
    def __init__(self, lines):
        self.lines = lines
        self.history = deque(maxlen=3)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

with open('../04/creating_data_processing_pipelines/example.py') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, line in lines.history:
                print('{}:{}'.format(lineno, line), end='')
