class A(object):
    def funcA(self):
        print("funcA")
    i_temp=100
    @classmethod
    def funcB(cls):
        print(cls.i_temp)
        print(cls().funcA())
A.funcB()