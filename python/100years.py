from datetime import datetime

name = input("Name : ")
age = int(input("Age : "))

this_year = datetime.now().year

def year () :
    year_to_100 = (100 - age) + this_year
    if age < 100:
        print("You will have 100 years old in", year_to_100, "! \U0001F973\U0001F389\U0001F389\U0001F389")
    else:
        print("Happy 100 !", name)

year()