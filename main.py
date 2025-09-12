s = input().strip()

if s.endswith('kg'):
    try:
        kg = float(s[:-2])
        pounds = kg * 2.2046
        print("对应的英制重量为{:.3f}磅".format(pounds))
    except:
        print("输入格式错误")
        
elif s.endswith('pd'):
    try:
        pd = float(s[:-2])
        kg = pd / 2.2046
        print("对应的公制重量为{:.3f}公斤".format(kg))
    except:
        print("输入格式错误")
else:
    print("输入格式错误")
