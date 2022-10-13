#Author: @syedalizain033 (Twitter, Linkedin, Facebook, Instagram)

def leapYearFinder(year):
    year=int(year)
    if (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 !=0 ):
        return True
    return False

year=str(input("Enter year: "))
if year.isnumeric() and len(year)==4:
    if leapYearFinder(year):
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')
else:
    print('Enter a valid year.')