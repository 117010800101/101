Money=input("请输入带有符号金钱数目")
if Money[-1] in ['Y','y']:
     c=(eval(Money[0:-1]) 
     print("兑换后的金钱是{:.2f}c".format(M))
elif Money[-1] in['d','p']:
    f=1.8*eval(Money[0:-1])/6
    print("兑换后金钱是{:.2f}F",format(F))
else:
    print("输入格式错误")
