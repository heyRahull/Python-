# Astrologer's star (pattern printing)
# Taken a number as input from user and print the star pattern according to that input.
# Take a boolean value and print any one pattern accordingly

n = int(input("Enter a Number : "))
print(n)
bool1 = int(input("Enter 1 or 0 : "))
if (bool1 == 1):
    bool1 = True
elif (bool1 == 0):
    bool1 = False

if (bool1):
    print("\nPattern for True(1)")
    for x in range(0, n):
        print("\n")
        for y in range(0, x + 1):
            print("*", end="")
else:
    print("\nPattern for False(0)")
    for x in range(0, n):
        print("\n")
        for y in range(x, n):
            print("*", end="")
