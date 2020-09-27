def salary (hour, per_hour):
    if hour > 16:
        return "Error !!! Extera Time Work. You have to send your permission"
    else:
        pay = hour * per_hour
        return pay
h = int(input('Enter the hour: '))
ph = int(input('Enter amount per hour: '))
t = salary (h, ph)
print (t)