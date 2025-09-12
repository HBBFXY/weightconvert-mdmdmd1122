def weight_converter():
    # 获取用户输入
    s = input().strip()
    
    # 检查输入长度
    if len(s) < 2:
        print("输入格式错误")
        return
    
    # 提取单位（最后2个字符）
    unit = s[-2:]
    # 提取数字部分（除了最后2个字符的所有字符）
    num_str = s[:-2]
    
    # 检查数字部分是否有效
    if not num_str:
        print("输入格式错误")
        return
    
    try:
        num = float(num_str)
    except ValueError:
        print("输入格式错误")
        return
    
    # 进行转换
    if unit == "kg":
        pounds = num * 2.2046
        print("对应的英制重量为{:.3f}磅".format(pounds))
    elif unit == "pd":
        kilograms = num / 2.2046
        print("对应的公制重量为{:.3f}公斤".format(kilograms))
    else:
        print("单位错误，请输入kg或pd")

# 调用函数
weight_converter()
