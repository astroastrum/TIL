num = 1234
new_num = 0
multiple_num = 1000

while multiple_num != 0:
    new_num += (num % 10)*multiple_num
    num //= 10
    multiple_num = int(multiple_num / 10)

print(new_num)