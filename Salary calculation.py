# Salary calculation
hour = float(input('Enter Your Work Time (h): '))
if 0<=hour<=140:
    if hour<100:
        salary = hour * 9
        pay = salary - ((salary * 35) / 100)
        pay_toman = pay * 27500
        pay_euro = pay * 0.85
        print(pay,'$',pay_euro,'€',pay_toman,'Toman')
    if 100<=hour<115:
        s_h_middle = (hour - 100) * 10
        salay = ((s_h_middle + 891))
        tax = (salay * 35) / 100
        pay = salay - tax
        pay_toman = pay * 27500
        pay_euro = pay * 0.85
        print(pay,'$',pay_euro,'€',pay_toman,'Toman')
    if 115<=hour<=140:
        h_max = hour - 115
        salay = h_max + 1041
        tax = (salay * 35) / 100
        pay = salay - tax
        pay_toman = pay * 27500
        pay_euro = pay * 0.85
        print(pay,'$',pay_euro,'€',pay_toman,'Toman')
else:
    print("Talk to your boss because your work time is not in the valid range")