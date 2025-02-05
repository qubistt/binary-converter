# binary-converter program
'''
logic: base 10 to base 2
either remainder (easier)
or split into powers of 2

base 2 to base 10
??
'''
'''
todo
1. make it output int instead of list
2. make it run inf until user asks it to stop
3. add bnum to num functionality
'''
print("welcome.")
def num2bnum():
    bnum = []
    num = int(input("what is num? "))
    while True:
        bnum.insert(0, num%2)
        num = num//2
        if num <= 0:
            print(bnum)
            break
        else:
            continue

def num2bnum(bnum):
   for i in bnum

while True:
    choice = input("n2b, b2n or exit")
    if choice.lower() == 'n2b':
        num2bnum()
    elif choice.lower() == 'b2n':
        bnum2num()
    elif choice.lower() == 'exit':
        exit()
