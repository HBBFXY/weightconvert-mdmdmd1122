weight_str = input()
unit = weight_str[-2:]
value = float(weight_str[:-2])

if unit == "kg":
    pounds = value * 2.2046
    print(f"对应的英制重量为{pounds:.3f}磅")
elif unit == "pd":
    kilograms = value * 0.4535
    print(f"对应的公制重量为{kilograms:.3f}公斤")
else:
    print("输入格式错误")
