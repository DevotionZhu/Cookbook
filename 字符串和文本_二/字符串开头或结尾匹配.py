import os

filename = 'spam.txt'
print(filename.endswith('.txt'))  # True
print(filename.startswith('file.'))  # False


filenames = os.listdir('.')
print(filenames)
# [name for name in filenames if name.endswith(('.c', '.h')) ]