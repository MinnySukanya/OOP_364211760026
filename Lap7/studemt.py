"""
Name: Sukanya Khunthana
TD: SID: {364211760026}
Group: {MIT221}
"""

class Student:
    def __inif__(self,name,id):
        # attributer
        self .name = name # public member
        self.__id    = id # private member
    def __str__(self):
        print(f'name: {self.name} ID: {self.__id}')

std = Student("Purwiat","001")
# direct access
#print(std.name, std.id)

std.__str__()

std.name = "Nattapong" # change data attribute
std.__str__()

std.__id = "002"
std.__str__()

# name mangling
print(std._Student__id)

std._Student__id = "002"
std.__str__()