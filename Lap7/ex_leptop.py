"""
Name: {นางสาวสุกัญญา ขุนทนะ}
SID: {364211760026}
Group: {MIT221}
"""

class Laptop:
    def __init__(self,brand,model,cpu,ram,display,storage,price):
        self.__brand = brand
        self.__model = model
        self.__cpu = cpu
        self.__ram = ram
        self.__display = display
        self.__storage = storage
        self.__price = price

    def get_brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__brand = brand

    def get_model(self):
        return self.__model
    def set_model(self,model):
        self.__model = model

    def get_cpu(self):
        return self.__cpu
    def set_cpu(self,cpu):
        self.__cpu = cpu

    def get_ram(self):
        return self.__ram
    def set_ram(self,ram):
        self.__ram = ram

    def get_display(self):
        return self.__display
    def set_display(self,display):
        self.__display =display

    def gef_storage(self):
        return self.__storage
    def set_storage(self,storage):
        self.__storage = storage

    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price = price

    def __str__(self):
        print(f'Brand: {self.__brand} Model: {self.__model} CPU: {self.__cpu} RAM: {self.__ram} Display: {self.__display}'
              f'Price: {self.__price}')

s = Laptop("ASUS","Vivobook 15X","Inter Core i5-12500H","8","15.6","512","27,990")
s.__str__()

print(s.get_brand())
s.set_brand("Lenovo")
print(s.get_brand())

print(s.get_model())
s.set_model("IdeePadGaming3")
print(s.get_model())

print(s.get_cpu())
s.set_cpu("Intel Core i5-11320H")
print(s.get_cpu())