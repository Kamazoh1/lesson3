import datetime

today = datetime.date.today()
print('Today = ', today)

yesterday = today - datetime.timedelta(days = 1)
print("Yesterday = ", yesterday)
# d = datetime.date.today(-1)
try:
    month_ago = today.replace(month=today.month - 1)
except:
    month_ago = today - datetime.timedelta(days = 30)

print("Month ago = ", month_ago)

str_dt = '01/01/17 12:10:03.234567'

dt = datetime.datetime.strptime(str_dt, '%d/%m/%y %H:%M:%S.%f')

print(dt)
    # t = datetime.date(2019, 3, 30).replace(month=datetime.date.today().month-1)


# print("Hello world")
