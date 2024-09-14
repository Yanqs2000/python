class Car:
    """描述汽车的一些属性特征"""

    def __init__(self, brand, model):
        """初始化属性"""
        self.brand = brand
        self.model = model
        self.mileage = 0
        self.gas_tank = 92

        """定义方法"""

    def driving(self):
        print(f"{self.brand} {self.model} is driving")

    def stop(self):
        print(f"{self.brand} {self.model} is stop")

    def fill_gas_tank(self):
        print(f"{self.brand} {self.model} needs {self.gas_tank} gas")

    def read_mileage(self):
        print(f"{self.brand} {self.model} has driven {self.mileage} miles")

    def update_mileage(self, mileage):
        self.mileage += mileage


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
        print("Total Employee is", Employee.empCount)

    def displayEmployee(self):
        print("Name:", self.name, ",Salary:", self.salary)

    def get_private_attr(self):
        return self.__private_attr

    def set_private_attr(self, value):
        self.__private_attr = value


class ElectricCar(Car):
    """电动汽车的独特之处"""
    # 在子类的__init__()方法中，需要调用super()函数，让Python将新创建的实例传递给父类的__init__()方法
    # 若子类未写init方法，那么默认将继承父类的init方法，若子类写了init方法，那么必须调用super()函数来显式地表示继承关系
    # super()函数将父类的属性和方法都传递给了子类

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.battery = 1000

    # 子类可以定义自己的方法，也可以重写父类的方法
    def fill_gas_tank(self):
        print(f"{self.brand} {self.model} doesn't need gas tank")

    def fill_battery(self):
        print(f"{self.brand} {self.model} has a {self.battery} KWh battery")
