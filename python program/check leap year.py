#CHECK LEAP YEAR
def is_leap_year(year):
    if(year%4==0and year%100!=0)or(year%400==0):
        return True
    return False
year=int(input("Enter a year:"))
if is_leap_year(year):
    print("Leap year")
else:
    print("Not a Leap year")
