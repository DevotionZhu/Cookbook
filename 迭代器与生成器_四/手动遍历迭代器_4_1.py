# def manual_iter():
with open('E:\python\passwd') as f:
     try:
         while True:

             line = next(f)
             print(line, end='')
     except StopIteration:
             pass