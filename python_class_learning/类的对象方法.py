class Car:
    "__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建类的实例时，会自动调用该方法,self表示对象本身，不可缺少"
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.mileage = 0
    def drive(self, distance):
        print(f"Driving the {self.brand} {self.model}")
        self.mileage += distance

    def display_info(self):
        print(f"{self.brand} {self.model}, Mileage: {self.mileage} miles")
    "私有方法，只能在类的内部调用，不能在类的外部调用"
    def __description(self):
        return f"Finally, this car is a {self.brand} {self.model} with {self.mileage} miles on it."
    # 通过内部的公有方法调用私有方法来间接输出
    def final_description(self):
        return self.__description()


# 创建 Car 类的实例
my_car = Car("Toyota", "Camry")

# 调用对象方法
my_car.drive(50)
my_car.display_info()

# 再次调用对象方法
my_car.drive(30)
my_car.display_info()

print(my_car.final_description())

# 内置类方法，需要通过重写来改变其默认行为
"""
__dir__()	    输出本类和父类所有属性和方法名
__str__	        返回对象的字符串表示。
__repr__	    显示对象的一些必要信息
__len__()	    返回对象的长度。
__getitem__()	允许通过索引访问元素。
__getattr__	    获取属性的值
__delatr__	    删除某属性
__setattr__	    设置属性的值
__call__	    使实例对象可以像函数一样被调用。
__eq__()	    定义对象之间的相等比较。
__hash__()	    返回对象的哈希值。
"""
print(my_car.__hash__())
