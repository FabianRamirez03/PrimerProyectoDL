from pprint import pprint


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
    # (yValues)
    # print(xValues)
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
    row[parityPositions[rowNumber - 1]] = str(int(result))
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


# Retorna el valor sin los bits de paridad y los bits de paridad en una lista
def cleanNumber(binary, parity):
    parityPositions = [1, 2, 4, 8, 16]
    cont = 1
    new = ''
    parityBits = []
    while cont <= len(binary):
        if cont not in parityPositions:
            new += binary[cont-1]
        else:
            parityBits.append(str(binary[cont-1]))
        cont+=1
    return [new, parityBits]


# Retorna la posicion donde se encuentra el error
def compararParidades(paridadVieja, paridadRuidosa):
    cont = len(paridadVieja) -1
    result = ''
    resultCheckList = []
    while cont >= 0:
       if (paridadRuidosa[cont] != paridadVieja[cont]):
           result += '1'
           resultCheckList.append('1')
       else:
           result += '0'
           resultCheckList.append('0')
       cont-=1
    result = convertDecimal(result)
    return [result, resultCheckList]


def buildFinalTable(tableToBuild, extraData):
    tableToBuild[0].append('1')
    tableToBuild[0].append('')
    cont = 0
    while cont<len(extraData):
        if (extraData[cont] == 0):
            tableToBuild[cont + 1].append('Correcto')
        else:
            tableToBuild[cont + 1].append('Error')
        tableToBuild[cont + 1].append(extraData[cont])
        cont += 1
    return tableToBuild


def detectError(noisedNumber):
    # Recibimos un numero sucio pero con la paridad como si fuera limpio

    # Separamos ese numero en los valores de paridad y los valores de data
    cleaning = cleanNumber(noisedNumber, '0')
    # print('numero viejo: ', cleaning)

    # Recalcular Hamming para el numero 12 bits de data sucia
    noisedHamming = Hamming(cleaning[0], '0')

    # Obtener los valores de paridad de esa tabla
    noisedHammingNumberCalculated = cleanNumber(noisedHamming[-1][1:], '0')

    # print(noisedHamming[-1][1:])
    # print('numero nuevo:', noisedHammingNumberCalculated)

    # Comparar los valores de paridad viejos con los nuevos
    posicionError = compararParidades(cleaning[1], noisedHammingNumberCalculated[1])

    # Construir la tabla final
    finalTable = buildFinalTable(noisedHamming, noisedHammingNumberCalculated[1][:5])

    # Retornamos la posicion de error con la tabla
    return [posicionError[0], finalTable]


result = detectError('01101011101010111')
print(result[1])
