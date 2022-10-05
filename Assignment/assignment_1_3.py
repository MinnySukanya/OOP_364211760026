"""
Name: {นางสาวสุกัญญา ขุนทนะ}
SID: {364211760026}
Group: {MIT221}
"""

"""
เขียนโปรแกรมไพธอนเพื่อนำเลขบัตรประชาชนมาบวกกันเพื่อทำนายดวงชะตาดังนี้
• สร้างฟังก์ชันเพื่อหาผลรวมของเลขบัตรประชาชน โดยใช้ชื่อฟังก์ชั่นว่า sumPID()
• สร้างฟังชั่นชื่อ getFortune() เพื่อทำนายดวงชะตา ถ้าเป็นเลขคู่ให้ทำนายว่า your fortune is good
• ถ้าเป็นเลขคี่ ให้ทำนายว่า your fortune is very good

ใช้ฟังก์ชั่น split()
ใช้ฟังก์ชั่น spl
"""
def getPTD():
    pid = input('Enter your pid ') #str
    lpid = [int(x) for x in pid]
    return lpid #list

def getFortune(var):
        if var % 2 == 0:
            print('Your fortune is good')
        else:
            print('Your fortune is very good')

PID = getPTD()
print(f'The data from user: {sum(PID)}')
print(f'The prediction result is: {getFortune(sum(PID))}')

print("Hello, MIT221")
