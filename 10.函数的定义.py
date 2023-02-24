import random


def welcome(n):
    print("欢迎来到黑马程序员！")
    print("请出示您的健康码及72小时核酸证明！")
    if n <= 37.5:
        print(f"您的体温是{n}， 正常进入")
    else:
        print(f"您的体温是{n},需要隔离")


welcome(random.randint(36, 42))


def add(n, m):
    result = n + m
    print(f"{n} + {m}的结果是{result}")


add(1343452, 3464575468)
