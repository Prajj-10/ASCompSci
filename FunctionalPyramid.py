def set_values(Symbol, MaxNumOfSymbol, NumberOfSpaces, NumberOfSymbols):
    Symbol = input("Enter a symbol : ")
    MaxNumOfSymbol = validated_max_number_of_symbols()
    NumberOfSpaces = (MaxNumOfSymbol - 1) / 2
    NumberOfSpaces = int(NumberOfSpaces)
    NumberOfSymbols = 1


def validated_max_number_of_symbols():
    MaxNumOfSymbol = 2
    MaxNumOfSymbol = int(input("Enter max number of symbols : "))
    while MaxNumOfSymbol % 2 != 1:  # keeps on repeating until user enters an odd number.
        print("Enter an odd number !!")
        MaxNumOfSymbol = int(input("Enter max number of symbols : "))
    return MaxNumOfSymbol


def output_spaces(NumberOfSpaces):
    for i in range(1, NumberOfSpaces + 1):
        print(" ", end="")


def output_symbols(NumberOfSymbols, Symbol):
    for j in range(1, NumberOfSymbols + 1):
        print(Symbol, end="")
    print()


def adjusted_number_of_spaces(NumberOfSpaces):
    NumberOfSpaces = NumberOfSpaces - 1
    return NumberOfSpaces


def adjusted_number_of_symbols(NumberOfSymbols):
    NumberOfSymbols = NumberOfSymbols + 2
    return NumberOfSymbols


NumberOfSymbols = 1
MaxNumOfSymbol = 0
set_values(Symbol="", MaxNumOfSymbol=0, NumberOfSpaces=0, NumberOfSymbols=1)
while NumberOfSymbols <= MaxNumOfSymbol:
    output_spaces()
    output_symbols()
