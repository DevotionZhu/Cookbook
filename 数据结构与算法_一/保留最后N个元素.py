from collections import deque


def search(lines, pattern, history = 5):
    previous_lines = deque(maxlen= history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines

            self.get_urlself.get_urll