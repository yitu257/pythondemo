def h():
    print('start')
    m = yield 5
    print(m)
    n = yield 100
    print(m)
    print(n)
    m = yield 200
    print(m)
    print(n)

c=h()
value1 = c.__next__()# c.__next__() 相当于 c.send(None)
print("这是表达式 yield   5 对应存储的值：" + str(value1) + "\n")
value2 = c.send('aaa')
print("这是表达式 yield 100 对应存储的值：" + str(value2) + "\n")
value3 = c.send(999999)
print("这是表达式 yield 200 对应存储的值：" + str(value3) + "\n")

c.send('最后一个yield值修改但是找不到结束的"yield标签')