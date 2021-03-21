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


def Hamming(binary):
    strBinary = str(binary)
    m = len(strBinary)
    r = calcRedundantBits(m)
    arr = posRedundantBits(strBinary, r)
    arr = calcParityBits(arr, r)
    return setHammingNumber(binary)


def calcRedundantBits(m):
    # Use the formula 2 ^ r >= m + r + 1
    # to calculate the no of redundant bits.
    # Iterate over 0 .. m and return the value
    # that satisfies the equation

    for i in range(m):
        if 2 ** i >= m + i + 1:
            return i


def posRedundantBits(data, r):
    # Redundancy bits are placed at the positions
    # which correspond to the power of 2.
    j = 0
    k = 1
    m = len(data)
    res = ''

    # If position is power of 2 then insert '0'
    # Else append the data
    for i in range(1, m + r + 1):
        if i == 2 ** j:
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1

    # The result is reversed since positions are
    # counted backwards. (m + r+1 ... 1)
    return res[::-1]


def calcParityBits(arr, r):
    n = len(arr)

    # For finding rth parity bit, iterate over
    # 0 to r - 1
    for i in range(r):
        val = 0
        for j in range(1, n + 1):

            # If position has 1 in ith significant
            # position then Bitwise OR the array value
            # to find parity bit value.
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-1 * j])
            # -1 * j is given since array is reversed

        # String Concatenation
        # (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr


def setHammingNumber(binary):
    parityPositions = [1, 2, 4, 8, 16]
    result = [
        ['Palabras de datos (sin paridad)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['P1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['P2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['P3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['P4', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['P5', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['Palabras de datos (con paridad)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    ]
    row = 0
    rowLimit = len(result)
    columnLimit = len(result[0])
    cont = 0
    while cont < 7:
        result[cont] = setRow(binary, cont, result[cont], True, result)
        cont = cont + 1
    print(result)
    return result


def setRow(binary, rowNumber, row, parity, wholeResult):
    parityPositions = [1, 2, 4, 8, 16]
    binaryPos = 0
    column = 1
    columnLimit = len(row)
    result = []
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
    row[parityPositions[rowNumber-1]] = int(result)
    print(row)
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

