TempStr=input("请输入带有符号温度值")
if TempStr[-1] in ['F','f']:
     c=(eval(TempStr[0:-1]) -32)/1.8
     print("转换后的温度是{:.2f}c".format(c))
elif TemSptr[-1] in['c','c']:
    f=1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2f}F",format(F))
else:
    print("输入格式错误")
