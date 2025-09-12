# 获取用户输入
input_str = input().strip()
# 提取数值和单位
num = float(input_str[:-2])
unit = input_str[-2:].lower()  # 统一转为小写，避免大小写问题

if unit == 'kg':
    # 千克转磅，1 千克 = 2.2046 磅
    pounds = num * 2.2046
    print(f"对应的英制重量为{pounds:.3f}磅")
elif unit == 'pd':
    # 磅转千克，1 磅 = 1/2.2046 千克
    kilograms = num / 2.2046
    print(f"对应的公制重量为{kilograms:.3f}公斤")
else:
    print("输入单位错误，请输入'kg'（千克）或'pd'（磅）")
