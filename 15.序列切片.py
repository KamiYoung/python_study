# 切片操作，列表，元组，字符串，均支持进行切片操作
# 切片： 从一个序列中，取出一个子序列
# 语法： 序列【起始下标：结束下标：步长】
my_list = [0, 1, 2, 3, 4, 5, 6]

# 对lisit切片，1开始，4结束，步长1
result = my_list[1:4]
print(f"结果1：{result}")

# 对tuple切片， 从头开始，步长1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]
print(f"结果2：{result2}")

# 对str进行切片，从头开始，到最后结束，步长2
my_str = "01234567"
result3 = my_str[::2]
print(f"结果3：{result3}")

# 对str进行切片，从头开始到最后结束，步长-1
result4 = my_str[::-1]
print(f"结果4：{result4}")

# 对列表进行切片，从3开始，到1结束，步长-1
result5 = my_list[3:1:-1]
print(f"结果5：{result5}")


# 对元组进行切片，从头开始，到尾结束，步长-2
result6 = my_tuple[::-2]
print(f"结果6：{result6}")
