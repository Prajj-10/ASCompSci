# Step 1

Symbol = input("Enter a symbol : ")
MaxNumOfSymbol = 2  # Initializing a value that does not give 1 as a remainder.
MaxNumOfSymbol = int(input("Enter max number of symbols : "))

# Step 2
while MaxNumOfSymbol % 2 != 1: # keeps on repeating until user enters an odd number.
    print("Enter an odd number !!")
    MaxNumOfSymbol = int(input("Enter max number of symbols : "))
NumberOfSpaces = (MaxNumOfSymbol-1)/2
NumberOfSpaces = int(NumberOfSpaces)
NumberOfSymbols = 1

# Step 3
while NumberOfSymbols <= MaxNumOfSymbol:
    for i in range(1, NumberOfSpaces+1):
        print(" ", end="")

    # Step 4
    for j in range(1, NumberOfSymbols + 1):
        print(Symbol, end="")
    print()

    # Step 5

    NumberOfSpaces = NumberOfSpaces - 1
    NumberOfSymbols = NumberOfSymbols + 2


'''
a = int(input("enter number of column : "))
for i in range(1,a+1):
for j in range(0,(i+(i-1))):
print(b, end="")
print(" ")
'''