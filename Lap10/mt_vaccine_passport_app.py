"""
Name: Sukanya Khunthana
TD: SID: {364211760026}
Group: {MIT221}
"""

from model import Person,Studet,Vaccine,Vaccine_Passport

p1 = Person("Sukanta",21,50,155)

v1 = Vaccine("Astrazeneca")
d1 = "10/7/2565"

vp1 = Vaccine_Passport(p1)

vp1.vaccine_passport_info()

vp1.add_vaccine(v1)
vp1.add_date(d1)

vp1.vaccine_passport_info()

v2 = Vaccine("Pfizer")
d2 = "10/8/2565"

vp1.add_vaccine(v2)
vp1.add_date(d2)

vp1.vaccine_passport_info()

# Student
s1 = Studet("Phornprasert",38,75,165,"MIT")

v3 = Vaccine("Sinovac")
d3 = "11/8/2565"

vp2 = Vaccine_Passport(s1)
vp2.add_vaccine(v3)
vp2.add_date(d3)

vp2.vaccine_passport_info()