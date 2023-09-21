NumberOfSpaces = 0
Symbol = ""
NumberOfSymbols = 1
MaxNumOfSymbol = 0



# Procedure SetValues
def set_values():
    Symbol = input("Enter a symbol : ")
    MaxNum = input_max_number_of_symbols()
    NumberOfSpaces = (MaxNum - 1) / 2
    NumberOfSpaces = int(NumberOfSpaces)
    NumberOfSymbols = 1


# call MaxNumOfSymbol Function

def input_max_number_of_symbols():
    MaxNumOfSymbol = 2
    MaxNumOfSymbol = int(input("Enter max number of symbols : "))
    while MaxNumOfSymbol % 2 != 1:  # keeps on repeating until user enters an odd number.
        print("Enter an odd number !!")
        MaxNumOfSymbol = int(input("Enter max number of symbols : "))
    return MaxNumOfSymbol


def output_spaces():
    for i in range(1, NumberOfSpaces + 1):
        print(" ", end="")


def output_symbols():
    for j in range(1, NumberOfSymbols + 1):
        print(Symbol, end="")
    print()


set_values()
while NumberOfSymbols <= MaxNumOfSymbol:
    output_spaces()
    output_symbols()
    NumberOfSpaces = NumberOfSpaces - 1
    NumberOfSymbols = NumberOfSymbols + 2
