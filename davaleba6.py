# pirveli

nuli = 0

while True:
    num = int(input("შეიყვანე რიცხვი: "))

    if num == 0:
        break
    if num > 0:
        nuli += num

print("ჯამი არის:", nuli)


# meore



num = int(input("შეიყვანე რიცხვი: "))

if num < 0:
    num = -num

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10
        count += 1

print("ციფრების რაოდენობაა:", count)




#mesame 

N = int(input("შეიყვანე რიცხვი N: "))

kenti = 0
luwi = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        luwi += 1
    else:
        kenti += 1

print("კენტი რიცხვების რაოდენობა:", kenti)
print("ლუწი რიცხვების რაოდენობა:", luwi)