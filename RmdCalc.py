# today's date
from MonthDictionary import month_def
from datetime import date
today = date.today()
today_date = today.strftime("%m/%d/%Y")


DOB_Input = input("Enter your Date of Birth __/__/____: ")
dates = DOB_Input.split('/')
month = dates[0]
day = int(dates[1])
year = int(dates[2])

tdates = today_date.split('/')
tmonth = tdates[0]
tday = int(tdates[1])
tyear = int(tdates[2])


class Class(object):
    def __init__(self, m, d):
        self.total_days = month_def.get(m) + d

    def giveDecimal(self):
        decimal_days = self.total_days/365
        return decimal_days


bday_as_decimal = Class(month, day)
today_as_decimal = Class(tmonth, tday)

age = (tyear + today_as_decimal.giveDecimal()) - (year + bday_as_decimal.giveDecimal())
print(f"your age is {age}")

# calculate when the first RMD will be
new_first_rmd = 73 + year
old_first_rmd = 71 + year

if year > 1949:
    print(f"Your first RMD is due by April 1st, {new_first_rmd}")
elif year == 1949 and int(month) >= 7:
    print(f"Your first RMD is due by April 1st, {new_first_rmd}")
elif year == 1949 and int(month) < 7:
    print(f"Your first RMD was due by April 1st, {old_first_rmd}")
elif year < 1949 and int(month) < 7:
    print(f"Your first RMD was due by April 1st, {old_first_rmd}")
else:
    print(f"Your first RMD was due by April 1st, {72 + year}")
