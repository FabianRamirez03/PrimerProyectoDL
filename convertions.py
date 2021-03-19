def validateBinary(numberEntry):
    binary = False
    for i in str(numberEntry):
        if i in '10':  # If digit is 1 or 0
            binary = True
        else:
            binary = False
            break
    return binary


def convertDecimal(binaryNum):
    decimalRepresentation = int(binaryNum, 2)
    return decimalRepresentation


def convertOctal(binaryNum):
    decimalRepresentation = int(binaryNum, 2)
    octalString = oct(decimalRepresentation)
    return octalString


def convertHexadecimal(binaryNum):
    decimalRepresentation = int(binaryNum, 2)
    hexadecimalString = hex(decimalRepresentation)
    return hexadecimalString

def convertNZRI(binaryNum):
    yValues = [False]
    xValues = [0]
    number = [0]
    cont = 1
    for num in binaryNum:
        if (num == "1"):
            yValues.append(not yValues[-1])
        else:
            yValues.append(yValues[-1])
        number.append(num)
        xValues.append(cont)
        cont += 1
    print(yValues)
    print(xValues)
    return [xValues, yValues, number]