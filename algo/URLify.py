def urlify(S,length):
    cA = list(S)
    j = len(cA)-1
    #verse backwards from the last letter (not space) of your 'array'.
    # Whenever you hit a letter, move it to the last space in the array.
    # If a space is found, there will now be enough space to add "%20."
    # Do it one character at a time, and continue the loop until you reach index 0.
    for i in range(length-1,-1,-1):
        if cA[i] != ' ':
            cA[j] = cA[i]
            j -= 1
        else:
            cA[j] = "0"
            cA[j-1] = '2'
            cA[j-2] = '%'
            j -= 3
    return ''.join(cA)
print(urlify('Mr John Smith    ',13))
