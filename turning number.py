number = int (input('Enter a three digit number: '))
n1 = number // 100
n2_1 = number % 100
n2 = n2_1 // 10
n3 = number % 10
number_reverse = (n3*100)+(n2*10)+(n1)
print (number_reverse)
print (number_reverse*2)