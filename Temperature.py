x = input("Enter farinhait(1) or cantigrad(2)?")

farinhait = 1
cantigrad = 2

dama = int(input("Enter your number:"))

if x == '1':
    farinhait = ((dama * 1.8) + 32)
    print("F:", farinhait)

elif x == '2':
    cantigrad = ((dama - 32)/ 1.8)
    print("C:", cantigrad)
