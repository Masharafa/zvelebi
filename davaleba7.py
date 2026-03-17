# # 1) გამრავლების ტაბულა

# n = int(input("შეიყვანე რიცხვი: "))

# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)

# # 2) FizzBuzz

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)



 # 3) სამკუთხედი (ვარსკვლავები)

n = int(input("შეიყვანე რიცხვი: "))

for i in range(n, 0, -1):
    print("*" * i)