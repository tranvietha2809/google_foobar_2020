def buildBraille():
    orgS = "The quick brown fox jumps over the lazy dog"
    orgB = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    cleanorgB = ""
    cleanorgS = ""
    dictB = {}
    for i in range(0, len(orgB) - 5, 6):
        if orgB[i: i+6] == "000001" or orgB[i: i+6] == "000000":
            continue
        else:
            cleanorgB += orgB[i: i+6]
        #xu li orgS
        cleanorgS += orgS[int((i-6)/6)].lower()
        # dictB[orgS[int((i-6)/6)]] = string[i: i+6].lower()
    for i in range(0, len(cleanorgB) - 5, 6):
        dictB[cleanorgS[int((i)/6)]] = cleanorgB[i: i+6]
    dictB[' '] = "000000"
    return dictB

def solution(s):
    brailleTranslation = buildBraille()
    rs = ""
    for i in range(0, len(s)):
        if(s[i].isupper() == True):
            rs += "000001"
            l = s[i].lower()
            rs += brailleTranslation[l]
        else:
            rs += brailleTranslation[s[i]]
    return rs


