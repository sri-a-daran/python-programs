month=int(input("Enter the required month "))
year=int(input("Enter the required year "))
if month in (1,3,5,7,8,10,12):
    print("31 days")
elif month in (4,6,9,11):
    print("30 days")
elif month==2:
    if year%4==0:
        print("29 days")
    else:
        print("28 days")
else:
    print("Invalid month")
