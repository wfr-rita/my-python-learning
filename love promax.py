"""用python设计第一个游戏"""
import random
counts = 3
answer = random.randint(1,5)
while counts > 0:
    temp = input("不妨猜一猜我今天爱你有几分")
    guess = int(temp)

    if guess == answer:
        print("我也爱你，今天爱你，明天爱你，所有的明天，一如既往地爱你")
        print("哈哈，我会爱你一辈子！")
    else:
        if guess < answer:
        
            print("我爱你，宝贝，无论你是什么样的，我知道你不爱我，无论你身处哪里，我会爱你，更加爱你")

        else:
            print("谢谢有你爱我，我们彼此相爱，直至沧海断裂，直至世界毁灭。")
            break
        counts = counts - 1
            
    
print("这是你第一次打代码，希望你将来不缺钱，不缺爱，潇潇洒洒，风风火火")    
     
    
    

