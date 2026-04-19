timu_one = input("3 + 5 = ?")
timu_two = input("10 % 3 = ?")
timu_three = input("5 > 3 的结果是 True 还是 False?")
timu_one = int(timu_one)
timu_two = int(timu_two)
if timu_two == 8:
    print("正确")
    else:
        print("错误")
if timu_two == 1:
    print("正确")
    else:
        print("错误")
if timu_three == "True":
    print("正确")
    else:
        print("错误")
if timu_one == 8 and timu_two == 1 and timu_three == "True":
    print("3/3")
else:
    print("不及格")
