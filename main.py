# 在这个文件下编写代码，题目具体要求见README.md文件
# WeightConvert.py
weight_str = input()
kg_to_pd = 2.2046
if weight_str[-2:] == 'kg':
    kg = float(weight_str[:-2])
    pd = kg * kg_to_pd
    print(f"对应的英制重量为{pd:.3f}磅")
elif weight_str[-2:] == 'pd':
    pd = float(weight_str[:-2])
    kg = pd / kg_to_pd
    print(f"对应的公制重量为{kg:.3f}公斤")
else:
    print("输入格式错误")
