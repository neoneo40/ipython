
# -*- coding: utf-8
class Stack:
    def __init__(self):
        self.storages = []
 
    def is_empty(self):
        return len(self.storages) == 0
 
    def push(self, value):
        self.storages.append(value)
 
    def pop(self):
        return self.storages.pop()
 
    def top(self):
        return self.storages[-1]
    
    def __str__(self):
        return str(self.storages)
 
 
def well_matched(string_):
    # 여는 괄호
    opening = ['(', '{', '[']
    # 닫는 괄호
    closing = [')', '}', ']']
    # 열린 괄호들을 순서대로 담는 스택
    open_stack = Stack()
    for ch in string_:
        # opening에 포함되는 문자가 있으면 stack에 넣는다.
        if ch in opening:
            open_stack.push(ch)
        else:
            # stack에 아무것도 없는데 닫는 괄호가 있다면 False
            if open_stack.is_empty():
                return 'NO'
            top = open_stack.top()
            # openingr과 closing의 index를 비교해서 같지 않으면 False
            if opening.index(top) != closing.index(ch):
                return 'NO'
            # stack에 들어있는걸 뺀다.
            open_stack.pop()
    # 모든 for문이 끝났을때 stack이 비어있으면 True
    if open_stack.is_empty():
        return 'YES'
    # 그게 아니면 False
    return 'NO'
 
 
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        string_  = raw_input()
        print well_matched(string_)