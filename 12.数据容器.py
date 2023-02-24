# 列表特性： 多元素，不同类型， 有序存储（下标）， 允许重复，允许修改




test_list = ["itheima", "黑马", "程序员"]

# 查询元素下标
index = test_list.index("itheima")
print(f"itheima在列表的索引为：{index}")

# 修改指定下标索引的值
test_list[0] = "华电"
print(test_list)

# 在指定下标插入值
test_list.insert(1, "国际")
print(test_list)

# 在末尾追加单个元素
test_list.append("鲁能软件")
print(test_list)

# 在末尾追加一批元素
test_list.extend(["国家", "电网"])
print(test_list)

# 删除指定下标的元素
del test_list[2]
print(test_list)
# 取出指定下标元素
element = test_list.pop(2)
print(element)
print(test_list)

# 删除某元素在列表中的第一个匹配项
test_list = [1, 2, 2, 3]
test_list.remove(2)
print(test_list)

# 清空列表
test_list.clear()
print(test_list)

# 统计某元素的数量
test_list = [1, 2, 2, 3, 4, 4, 4]
print(test_list.count(4))

# 计算长度
print(len(test_list))

