# binary-converter program
'''
logic: base 10 to base 2
either remainder (easier)
or split into powers of 2

base 2 to base 10
??
'''

print("welcome.")
num = int(input("what is your num?"))
bnum = []
while True:
    bnum.insert(0, num%2)
    num = num//2
    if num <= 0:
        print(bnum)
        break
    else:
        continue

