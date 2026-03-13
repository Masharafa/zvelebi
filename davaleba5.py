total = 0

while True:
    price = float(input("შეიყვანეთ პროდუქტის ფასი (0 - დასრულება): "))

    if price == 0:
        break

    if price < 0:
        print("შეცდომა! ფასი უარყოფითი არ შეიძლება")
    else:
        total += price

print("საერთო ჯამი:", total)

if total > 100:
    discount = total * 0.10
    new_total = total - discount
    print("თქვენ მიიღეთ 10% ფასდაკლება!")
    print("ახალი ჯამი:", new_total)




    count = 0

for i in range(1, 1001):
    if i % 10 == 0:
        print(i)
        count += 1

print("რაოდენობა:", count)




num = int(input("შეიყვანეთ დადებითი რიცხვი: "))

if num < 0:
    print("შეცდომა! უარყოფითი რიცხვი არ შეიძლება")
else:
    count = 0

    for i in range(1, num + 1):
        if i % 5 == 0:
            print(i)
            count += 1

    print("რაოდენობა:", count)