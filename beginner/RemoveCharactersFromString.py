# Question 4: Given a string and an integer number n,
# remove characters from a string starting from zero up to n and return a new string
# For example, removeChars("pynative", 4) so output must be tive.
# Note: n must be less than the length of the string.


str1 =input("Enter a string")
num1 = int(input("Enter a number"))

if num1 > len(str1):
    print("The number shold be less than the length of the string")
else:
    for x in range(num1, len(str1)):
        print(str1[x])