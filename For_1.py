number_1 = float(input('Enter Your Number: '))
count = 0
found = 0
while number_1 != -1:
    count += 1
    found = found + number_1
    number_1 = float(input('Enter a new Number: '))
if number_1 == -1:
    average = found / count
    print ('Count: ',count)
    print ('Average: ',average)