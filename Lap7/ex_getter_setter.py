"""
Name: {นางสาวสุกัญญา ขุนทนะ}
SID: {364211760026}
Group: {MIT221}
"""

class Student:
    def __inif__(self,name,id):
        # attributer
        self.__name = name # private member
        self.__id    = id # private member
    # getter and setter
    def get_name(self):
        return  self.__name
    def set_name(self,name):
        self.__name = name
        
    def get_id(self):
        return self.__id

    def __str__(self):
        print(f'Name: {self.__name} ID: {self.__id}')


s = Student("Sam","001")
s.__str__()

print(s.get_name())
s.set_name("Net")

print(s.get_name())
