
class MyClass(object):
    def __call__(self,num):
        print("in_call_:%s",num)

    def __init__(self,num):
        self.num=num

    def __str__(self):
        #print("in_str_")
        return "test"

    def __repr__(self):
        print("in_repr__")
        return "test2"

if __name__ == '__main__':
    a=MyClass(4)
    print(a)
    b=a(75)
    print(a(75))
    #print(c)
