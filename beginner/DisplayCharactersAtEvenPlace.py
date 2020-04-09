# Question 3: Accept string from a user and 
# display only those characters which are present at an even index number.

# For example str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

str1 = input("Enter a String")
print("THe original string is :", str1)

print("The output is :")
for x in range(0, len(str1), 2):
    print("index[", x, "]", str1[x])


