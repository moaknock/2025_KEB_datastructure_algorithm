class Stack:
    def __init__(self):
        self.items = list()

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0  # 스택이 비어 있는지 확인


s1 = Stack()
s1.push(-9)
s1.push(11)
s1.push(977)

print(s1.pop())  # 977
print(s1.peek()) # 11
print(s1.peek()) # 11 (peek()은 값 제거 없이 확인만 함)
