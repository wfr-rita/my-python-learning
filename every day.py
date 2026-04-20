day = 1
while day <= 7:
    answer = input("今天内心有想我吗？")
    if answer != "有":
        break
    day += 1
else:
    print("我也爱你，每一天")
