# 发工资
import random

# count = 10000
# for i in range(1, 21):
#     n = random.randint(1, 10)
#     if n < 5:
#         print(f"员工{i}的绩效为{n}， 低于5，不发工资")
#         continue
#     count -= 1000
#     print(f"员工{i}绩效为{n}，向员工{i}发放工资1000元，账户余额还剩{count}元")
#     if count == 0:
#         print("工资发完啦！")
#         break

money = 10000
for i in range(1, 21):
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}的绩效为{score}， 低于5，不发工资")
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i}绩效为{score}，向员工{i}发放工资1000元，账户余额还剩{money}元")
    else:
        print(f"余额不足，当前余额{money}元，不足以发放工资，下个月再来")
        break
