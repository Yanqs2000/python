class Car():
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


# 创建 Car 类的实例
my_car = Car("Toyota", "Camry")

# 调用对象方法
my_car.drive(50)
my_car.display_info()

# 再次调用对象方法
my_car.drive(30)
my_car.display_info()
