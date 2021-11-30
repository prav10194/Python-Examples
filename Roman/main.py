def convertA2R(arabic, roman, inputNumber):
    index = len(arabic) - 1
    romanString = ""
    while(inputNumber > 0):
        if(inputNumber >= arabic[index]):
            romanString += roman[index]
            inputNumber -= arabic[index]
        else:
            index -= 1
    return romanString
