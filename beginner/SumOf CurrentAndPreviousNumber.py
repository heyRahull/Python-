# Question 2: Given a range of first 10 numbers,
# Iterate from start number to the end number and
# print the sum of the current number and previous

print("Printing current and previous number sum in a given range(10)")
previousNumber = 0
for x in range(10):
    sum1 = x + previousNumber
    print("Current Number is : ", x, "previous number is : ", x-1, "The sum is : ", sum1)
    previousNumber = x
