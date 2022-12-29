print ("Nikhil's Expenditure For First Semester")
income=int(input('Enter the Monthly income :'))
rent=float(input('Enter the weekly rent :'))
mr=rent*4
b=float(input('Enter the bills on Food and Electricity :'))
mx=mr+b
m=int(input ('Enter the number of months in First semester :'))
t=(income)-mr+b
s=(m*income)-m*mx
print(f"Monthly expenses of Nikhil : {mx:1.2f}".format(mx))
print(f"Monthly savings of Nikhil : {t:1.2f}".format(t))
print(f"Nikhil's expense in a day : {mx/30:1.2f}".format(mx/30))
print(f"Nikhil's savings in first semester : {s:1.2f}".format(s))


