# 定义集合
my_set = {"传智教育", "itheima", "etoake", "黑马程序员", "传智教育", "itheima", "etoake", "黑马程序员"}
my_set_empty = set()
print(f"my_set的内容是:{my_set}，类型是: {type(my_set)}")
print(f"my_set_empty的内容是:{my_set_empty}，类型是: {type(my_set_empty)}")


# 添加新元素
my_set.add("kami")
print(f"加入kami后my_set的内容是:{my_set}，类型是: {type(my_set)}")
# 移除元素
my_set.remove("黑马程序员")
print(f"移除黑马程序员后my_set的内容是:{my_set}，类型是: {type(my_set)}")
# 随机取出一个元素
element = my_set.pop()
print(f"随机取出的元素是:{my_set}，取出元素后：{my_set}")
# 清空元素
my_set.clear()
print(f"集合清空，：{my_set}")

# 取差集
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.difference(set2)
print(f"取出差集的结果是：{set3}")
print(f"原集合set1：{set1}")
print(f"原集合set2：{set2}")

# 消除两个集合的差集
set1.difference_update(set2)
print(f"消除差集后set1：{set1}")
print(f"消除差集后set2：{set2}")

# 集合合并
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.union(set2)
print(f"合并结果set3：{set3}")
print(f"原集合set1：{set1}")
print(f"原集合set2：{set2}")


# 作业
my_list = ["黑马程序员", "传智播客", "黑马程序员", "传智播客", "itheima", "itcast", "itheima", "itcast", "best"]
test_set = set()
for e in my_list:
    test_set.add(e)
print(f"结果：{test_set}")
