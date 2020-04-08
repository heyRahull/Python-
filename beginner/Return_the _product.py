# Question 1: Accept two integer numbers from a user and return their product and
# if the product is greater than 1000, then return their sum

num1 = int(input("Enter the First integer : "))
num2 = int(input("Enter the First integer : "))
product = num1*num2
print("The product of the two numbers is : ", product)
if product > 1000:
    print("The sum of two numbers is : ", num1+num2)