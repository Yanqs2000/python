class Employee():
    "所有员工的基类"
    empCount = 0  # 类属性(类里面、函数外面定义)，从类内部或类外部以Employee.empCount的形式进行访问
    def __init__(self, name, salary):
        "对象属性是对象特征的描述,如name,salary"
        self.name = name
        self.salary = salary
        "私有属性是指类内部定义的属性，外部无法直接访问，只能通过类内部的方法进行访问"
        self.__private_attr = 10

        Employee.empCount += 1
    def displaycount(self):
        print("Total Employee is",Employee.empCount)
    def displayEmployee(self):
        print("Name:",self.name,",Salary:",self.salary)

    def get_private_attr(self):
        return self.__private_attr
    def set_private_attr(self, value):
        self.__private_attr = value

# 类的内置类属性        
print("doc属性", Employee.__doc__) # 类的文档字符串
print("name属性", Employee.__name__) # 类名
print("module属性", Employee.__module__) # 类定义所在的模块
print("bases", Employee.__bases__)  # 类的所有父类构成元素（存在的父类）
print("dict属性", Employee.__dict__) # 类的属性

# 创建Employee类的实例
obj = Employee("Tom", 10000)
print(obj.name)
print(obj.salary)
# 私有属性，不能够直接用obj.__private_attr访问，会报错，可以使用方法（函数）调用
print(obj.get_private_attr())
obj.set_private_attr(20)
print(obj.get_private_attr())