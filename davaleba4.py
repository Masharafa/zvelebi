number = int(input("enter number:"))
if number >0:
    print("რიცხვი მეტია ნულზე")
elif number <0:
    print("რიცხვი ნაკლებია ნულზე")
else:
    print("რიცხვი ნულია")





temp = float(input("შეიყვანეთ ტემპერატურა: "))

if temp > 30:
    print("ძალიან ცხელა")
elif 20 <= temp <= 30:
    print("თბილა")
elif 10 <= temp < 20:
    print("გრილია")
else:
    print("ცივა")




num = int(input("შეიყვანეთ რიცხვი: "))

if num % 2 == 0:
    print("ლუწია")
else:
    print("კენტია")




age = int(input("შეიყვანეთ ასაკი: "))

if age < 5:
    print("ბილეთი უფასოა")
elif 5 <= age <= 12:
    print("ბილეთის ფასი: 5 ლარი")
elif 13 <= age <= 17:
    print("ბილეთის ფასი: 8 ლარი")
elif 18 <= age < 65:
    print("ბილეთის ფასი: 12 ლარი")
else:
    print("ბილეთის ფასი: 6 ლარი")