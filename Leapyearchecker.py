#Leap Year Checker
#Ava Mendoza
# 11-6-24

#Initialize
#Functions
#If a year is divisible byb 4, it is a leap year.
#However, if that year is a;sp divisible by 100, it is not a leap year
#If it is divisible by 400. In that case, it is a leap year.

def is_leap_year(year):
    #Code goes here
    if year % 400 == 0:
        print("It is a leap year")
    elif year % 100 == 0:
        print("It is not a leap year")
    elif year % 4 == 0:
        print("It is a leap year")


#Main
is_leap_year(2024) #True
is_leap_year(1900) #False
is_leap_year(1600) #True
