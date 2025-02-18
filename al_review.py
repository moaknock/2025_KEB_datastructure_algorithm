# numbers = [1,2,3,4,5]
# for i in numbers:
#     for j in numbers:
#         for h in numbers:
#             x = i + j + h
#             print(x)

pin = 931
# n = len(pin)
n =  len(str(pin))
for i in range(10**n):
    if i == pin:
        print(i)