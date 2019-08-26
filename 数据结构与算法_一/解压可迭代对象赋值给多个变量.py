record = ('Dave','wangmm@ipharmcare.net','1234','5678')
name, mail, *numbers = record
print(numbers)  # 返回的是个列表
print(numbers[0:2])