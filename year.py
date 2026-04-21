year = int(input("请输入具体年份："))
month = int(input("请输入具体月份："))
if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year,"年2月有29天。")
    else:
        print(year,"年2月有28天。")
elif month in {1,3,5,7,,8,10,12}:
    print(year,"年",month,"月有31天。")
elif month in {4,6,9,11}:
    print(year,"年",month,"月有30天。")
