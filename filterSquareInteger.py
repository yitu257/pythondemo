#过滤出1~100中平方根是整数的数：
import math
def is_sqr(x):
    return math.sqrt(x)%1==0

templist=filter(is_sqr,range(1,101))
newlist=list(templist)
print(newlist)

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

print(globals())

#a=input("input:")
#print(a)

v=memoryview(bytearray("abcdef",'utf-8'))
print(v[1])
print(v[-1])
print(v[-2])
print(v[1:4])
print(v[1:4].tobytes())
print(v)

lst_t=("a",77,"bbcc",("user1","name","sex","age"))
print(lst_t[:2])
print(lst_t[:-3:-1])
print(lst_t[:3:2])
print(lst_t[::2])
print(lst_t[::-2])

dict = "abcd efgh";
print(dict)
print(repr(dict))
print(str(dict))

RANGE_NUM = 100
for i in (math.pow(x,2) for x in range(RANGE_NUM)): # 第一种方法：对列表进行迭代
     # do sth for example
    print(i)
