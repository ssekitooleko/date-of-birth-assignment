import calendar
age=input("Please input your age: \n")
int_age=int(age)
year= 2017-int_age
print("You were born in ",year)
month=input("In which month were you born? Please submit a month number: \n")
int_month=int(month)
actual_month=calendar.month_name[int_month]
print("You were born in ",actual_month)
date=input("Please input your date of day of birth: \n")
int_date=int(date)
birthday=calendar.day_name[calendar.weekday(year,int_month,int_date)]
print("You were born on ",birthday,int_date,actual_month,year)
input("Thank you very much Please type Maiso to end the program: \n")







