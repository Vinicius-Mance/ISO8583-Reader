def HexadecimalToAscii(ISOString):

    # string to storage ascii text to be returned by function
    asciiString = ""

    for i in range(0, len(ISOString), 2):

        # variable to storage a pair of characters to be analyzed
        pair = ISOString[i: i + 2]

        # conversion from base 16 to unicode characters
        asciiChar = chr(int(pair, 16))

        # final alteration on variable to be returned
        asciiString = asciiString + asciiChar

    return asciiString