"""
编写类时，并非总要从头开始，可以通过继承来直接获得另一个类的所有属性和方法。
被继承的类称为父类，而产生的新类称为子类。
子类在继承父类的属性和方法的同时，还可以定义自己的属性和方法，即可扩展性。
"""
# 创建子类时，父类必须包含在当前文件中，且位于子类前面

# 父类
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

# 子类
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


mycar = ElectricCar('Tesla', 'Model-X')
mycar.driving()
mycar.update_mileage(100)
mycar.stop()
mycar.read_mileage()
mycar.driving()
mycar.update_mileage(200)
mycar.stop()
mycar.read_mileage()
mycar.fill_gas_tank()
mycar.fill_battery()