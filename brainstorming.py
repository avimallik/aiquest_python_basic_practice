# practice - 1
# def inputNums(a, b):
#     if a > b:
#         print(a)
#     elif a < b:
#         print(b)
#     elif a == b:
#         print(a)
# inputNums(5, 6)

# practice - 2
# def oneToN(a):
#     for i in range(1, a+1):
#         print(i)
# oneToN(5)

# practice - 3
# def negativeNumberChecker(a):
#     if a < 0:
#         print("The number is Negative")
# negativeNumberChecker(-3)

# practice - 4
# def sumOfDigit(a):
#     sum = 0
#     for i in str(a):
#         sum = sum + int(i)
#     return sum
# print(sumOfDigit(123))

# a = 5
# mul = 1
# for i in range(a, 0, -1):
#     mul = mul*i
# print(mul)

# practice - 5
# def factorial(a):
#     multiplyFactNum = 1
#     for i in range(a, 0, -1):
#         multiplyFactNum = multiplyFactNum * i
#     return multiplyFactNum
# print(factorial(5))

# practice - 6
# def occuranceOfDigit(a):
#     alist = []
#     countList = []
#     for i in str(a):
#         alist.append(int(i))
#     for j in range(len(alist)):
#         countList.append(alist.count(alist[j]))
#     maxCount = countList.index(max(countList))
#     return alist[maxCount]

# print(occuranceOfDigit(1323122))

# practice - 8
# a = "aiquest"
# s = a[::-1]
# print(s)

#practice - 9
# def armStrongNumber(a):
#     bl = []
#     sum = 0
#     message = ""

#     for i in str(a):
#         bl.append(int(i))
#     for j in bl:
#         sum = sum + j**3
#     if sum == a:
#         message = f"{a} is an Armstrong Number"
#     else:
#         message = ""
#     return message

# print(armStrongNumber(153))






