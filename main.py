def weight_converter():
    # 获取用户输入
    s = input().strip()
    
    # 提取数字部分和单位部分
    # 单位在最后两个字符，其余部分是数字
    if len(s) < 2:
        print("输入格式错误")
        return
    
    # 获取最后两个字符作为单位
    unit = s[-2:]
    num_str = s[:-2]
    
    # 将数字部分转换为浮点数
    try:
        num = float(num_str)
    except:
        print("输入格式错误")
        return
    
    if unit == "kg":
        # 千克转磅
        result = num * 2.2046
        print("对应的英制重量为{:.3f}磅".format(result))
    elif unit == "pd":
        # 磅转千克
        result = num / 2.2046
        print("对应的公制重量为{:.3f}公斤".format(result))
    else:
        print("单位错误，请输入kg或pd")

# 调用函数
weight_converter()
