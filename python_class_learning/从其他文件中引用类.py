from module import Car, Employee, ElectricCar

mycar = Car("Tesla", "Model-X")

mycar.driving()
mycar.update_mileage(100)
mycar.read_mileage()

class Employee():
    "所有员工的基类"
    empCount = 0  # 类属性(类里面、函数外面定义)，从类内部或类外部以Employee.empCount的形式进行访问
    empCount1 = 1

    def __init__(self, name, salary):
        "对象属性是对象特征的描述,如name,salary"
        self.name = name
        self.salary = salary
        "私有属性是指类内部定义的属性，外部无法直接访问，只能通过类内部的方法进行访问"
        self.__private_attr = 10  # 前面加__(双下划线)表示它是私有属性，解释器会作出限制（通过重写属性名称的办法）
        self._private_attr = 11  # 前面加_(单下划线)只是约定它是私有属性，解释器并不会作出限制
employee = Employee("Tom", 10000)
print(employee.__dict__)  # 查看对象属性
print(employee.name)
print(employee.salary)
print(employee._private_attr) # 前面加_(单下划线)只是约定它是私有属性，解释器并不会作出限制 