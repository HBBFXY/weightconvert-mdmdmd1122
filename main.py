s = input().strip()

# 精确匹配格式
if len(s) >= 3 and s[-2:] == "kg" and s[:-2].isdigit():
    kg = float(s[:-2])
    pounds = kg * 2.2046
    print("对应的英制重量为{:.3f}磅".format(pounds))
    
elif len(s) >= 3 and s[-2:] == "pd" and s[:-2].isdigit():
    pd = float(s[:-2])
    kg = pd / 2.2046
    print("对应的公制重量为{:.3f}公斤".format(kg))
    
else:
    print("输入格式错误")
