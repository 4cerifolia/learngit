fa = type("foo", (object,),{"v1": 123, "func": lambda self: 666})

obj = fa()
print(obj)
print(obj.func())

# 类默认由type创建
# 元类：指定类由谁来创建

class base:
    def f1(self):
        print(self.age)


class son(base):
    def f2(self):
        print(self.name)


obj = son()
obj.name = "移动"
obj.age = 100


obj.f2()
obj.f1()# 不论父类子类，self等于对象本身，如果对象已经有age内存了，直接取用，无所谓在哪里

