stu_score = {
    "王力宏": {
        "语文": 77,
        "数学": 66,
        "英语": 33,
    },
    "周杰伦": {
        "语文": 88,
        "数学": 86,
        "英语": 55,
    },
    "林俊杰": {
        "语文": 99,
        "数学": 96,
        "英语": 66,
    }
}
print(f"周杰伦的语文信息是{stu_score['周杰伦']['语文']}")

# 新增元素
stu_score["张信哲"] = {
    "语文": 98,
    "数学": 92,
    "英语": 91,
}
print(f"字典新增元素后结果：{stu_score}")

# 更新元素
stu_score["周杰伦"]["英语"] = 63
print(f"字典更新元素后结果：{stu_score}")

# 获取全部key
result = stu_score.keys()
print(f"字典所有的key为：{result}")

# 遍历
for k in stu_score.keys():
    print(f"当前key为：{k}，当前值为：{stu_score[k]}")
    for key in stu_score[k].keys():
        print(f"当前key为：{key}，当前值为：{stu_score[k][key]}")
    print("----------------")
# 直接循环得到的也是key
for e in stu_score:
    print(f"当前e为：{e}")

print(f"当前元素数量为：{len(stu_score)}")
