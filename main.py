# 在这个文件下编写代码，题目具体要求见README.md文件
#weightConvert.py
weightStr=input("请输入带有符号的重量值：")
if weightStr[-2:]in['kg']:
  pd=eval(weightStr[0:-2])*2.2046
  print("转换后的英制重量是{:.3f}pd".format(pd))
elif weightStr[-2:]in['pd']:
  kg=eval(weightStr[0:-2])/2.2026
  print("转换后的公制重量是{:.3f}kg".format(kg))
else:
  print("输入格式错误")
