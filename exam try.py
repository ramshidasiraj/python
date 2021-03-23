year = int(input("enter a year :"))
if(year%400 == 0)or(year%4 and year% 1001==0):
    print("the given year is leap year")
else:
    print("the given year is not a leap year")
