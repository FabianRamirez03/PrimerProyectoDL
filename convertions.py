def validateBinary(numberEntry):
    binary = False
    for i in str(numberEntry):
        if len(str(numberEntry)) == 12:
            if i in '10':  # If digit is 1 or 0
                binary = True
            else:
                binary = False
                break
        else:
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


def Hamming(binary, parity):
    return setHammingNumber(binary, parity)


def setHammingNumber(binary, parity):
    result = [
        ['Palabras de datos (sin paridad)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['P1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['P2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['P3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['P4', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['P5', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['Palabras de datos (con paridad)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    ]
    cont = 0
    while cont < 7:
        result[cont] = setRow(binary, cont, result[cont], parity, result)
        cont = cont + 1
    return result


def setRow(binary, rowNumber, row, parity, wholeResult):
    parityPositions = [1, 2, 4, 8, 16]
    binaryPos = 0
    column = 1
    columnLimit = len(row)
    if rowNumber == 0:
        while column < columnLimit:
            if column in parityPositions:
                column = column + 1
                continue
            else:
                row[column] = binary[binaryPos]
                column = column + 1
                binaryPos = binaryPos + 1
        result = row
    elif rowNumber == 6:
        result = finalResult(wholeResult)
    else:
        result = checkParity(parity, binary, rowNumber, row)
    return result


def checkParity(parity, binary, rowNumber, row):
    sumChecker = True
    sum = 0
    parityPositionsInNumber = [0, 0, 1, 4, 11]
    parityPositions = [1, 2, 4, 8, 16]
    firstColumn = [0, 3, 3, 5, 9, 17]
    numberAdded = 0
    binaryLen = len(binary)
    column = firstColumn[rowNumber]
    binaryPosition = parityPositionsInNumber[rowNumber - 1]
    while binaryPosition < binaryLen:
        if sumChecker:
            sum = sum + int(binary[binaryPosition])
            numberAdded = numberAdded + 1
            if numberAdded == rowNumber:
                numberAdded = 0
                sumChecker = False
            if column in parityPositions:
                column = column + 1
            if column not in parityPositions:
                row[column] = binary[binaryPosition]
                column = column + 1
            binaryPosition = binaryPosition + 1
        else:
            if column in parityPositions:
                column = column + 1
            binaryPosition = binaryPosition + 1
            numberAdded = numberAdded + 1
            column = column + 1
            if numberAdded == rowNumber:
                numberAdded = 0
                sumChecker = True

    result = sum % 2
    if parity:
        result = not result
    row[parityPositions[rowNumber - 1]] = int(result)
    return row


def finalResult(wholeResult):
    result = wholeResult[6]
    result[1] = wholeResult[1][1]
    result[2] = wholeResult[2][2]
    result[3] = wholeResult[2][3]
    result[4] = wholeResult[3][4]
    result[5] = wholeResult[3][5]
    result[6] = wholeResult[3][6]
    result[7] = wholeResult[3][7]
    result[8] = wholeResult[4][8]
    result[9] = wholeResult[4][9]
    result[10] = wholeResult[4][10]
    result[11] = wholeResult[4][11]
    result[12] = wholeResult[4][12]
    result[13] = wholeResult[3][13]
    result[14] = wholeResult[3][14]
    result[15] = wholeResult[1][15]
    result[16] = wholeResult[5][16]
    result[17] = wholeResult[5][17]
    return result
