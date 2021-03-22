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


def HammingWithNoise(hammingTable, noiseCombobox):
    list = hammingTable[6][1:]

    print(noiseCombobox)
    if noiseCombobox == '1':
        list[2] = int(not int(list[2]))
        print("caca" + str(list))
    if noiseCombobox == '2':
        list[4] = int(not int(list[4]))
        print("caca" + str(list))
    if noiseCombobox == '3':
        list[5] = int(not int(list[5]))
        print("caca" + str(list))
    if noiseCombobox == '4':
        list[6] = int(not int(list[6]))
        print("caca" + str(list))
    if noiseCombobox == '5':
        list[8] = int(not int(list[8]))
        print("caca" + str(list))
    if noiseCombobox == '6':
        list[9] = int(not int(list[9]))
        print("caca" + str(list))
    if noiseCombobox == '7':
        list[10] = int(not int(list[10]))
        print("caca" + str(list))
    if noiseCombobox == '8':
        list[11] = int(not int(list[11]))
        print("caca" + str(list))
    if noiseCombobox == '9':
        list[12] = int(not int(list[12]))
        print("caca" + str(list))
    if noiseCombobox == '10':
        list[13] = int(not int(list[13]))
        print("caca" + str(list))
    if noiseCombobox == '11':
        list[14] = int(not int(list[14]))
        print("caca" + str(list))
    if noiseCombobox == '12':
        list[16] = int(not int(list[16]))
        print("caca" + str(list))
    strings = [str(integer) for integer in list]
    a_string = "".join(strings)
    result = int(a_string)

    print(result)

    return str(result)


### Retorna el valor sin los bits de paridad y los bits de paridad en una lista
def cleanNumber(binary):
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

### Retorna la posicion donde se encuentra el error
def compararParidades(paridadVieja, paridadRuidosa):
    cont = len(paridadVieja) -1
    print(paridadVieja)
    print(paridadRuidosa)
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

def buildFinalTable(tableToBuild, extraData, parity):
    tableToBuild[0].append('1')
    tableToBuild[0].append('')
    cont = 0
    while cont<len(extraData):
        if (extraData[cont] == '0'):
            tableToBuild[cont +1].append('Correcto')
        else:
            tableToBuild[cont +1].append('Error')
        tableToBuild[cont +1].append(parity[cont])
        cont+=1

    return tableToBuild



def detectError(noisedNumber, parity):
    # Recibimos un numero sucio pero con la paridad como si fuera limpio

    # Separamos ese numero en los valores de paridad y los valores de data
    cleaning = cleanNumber(noisedNumber)

    # Recalcular Hamming para el numero 12 bits de data sucia
    print('cdssfd', cleaning[0])
    noisedHamming = Hamming(cleaning[0], parity)

    # Obtener los valores de paridad de esa tabla
    noisedHammingNumberCalculated = cleanNumber(noisedHamming[-1][1:])

    # print(noisedHamming[-1][1:])

    # Comparar los valores de paridad viejos con los nuevos
    posicionError = compararParidades(cleaning[1], noisedHammingNumberCalculated[1])

    # Construir la tabla final
    #finalTable = buildFinalTable(noisedHamming, noisedHammingNumberCalculated[1])[:5]
    finalTable = buildFinalTable(noisedHamming, posicionError[1], cleaning[1])[:6]

    # Retornamos la posicion de error con la tabla
    return [posicionError[0], finalTable]


#result = detectError('001111010110', '0')
#print(result[0])

print(Hamming('001111010110', '0'))


#pprint(Hamming(cleaning[0], '0'))


#Result should be 110110101011