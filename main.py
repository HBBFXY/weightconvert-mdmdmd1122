# 获取用户输入
input_str = input()
# 提取数值部分和单位部分
num = float(input_str[:-2])
unit = input_str[-2:]
# 根据单位进行转换
if unit == 'kg':
    # 千克转磅
    result = num * 2.2046
    print(f"对应的英制重量为{result:.3f}磅")
elif unit == 'pd':
    # 磅转千克
    result = num / 2.2046
    print(f"对应的公制重量为{result:.3f}公斤")
