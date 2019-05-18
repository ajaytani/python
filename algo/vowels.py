def vowels(InputString):

    vowelSet = set(['a','e','i','o','u', 'A','E','I','O','U'])

    output = set()
    for i in InputString:
        if i in vowelSet:
            output.add(i)

    print(output)


vowels('AlphaBetaGamaInput given %t234qw')

def timesTable(n):

    for i in range(1,n+1):
        print i,
        for j in range(1,n+1):
            print i * j,
        print('\n')

print(timesTable(12))


def palindrome(inputString):
    n = len(inputString)
    start = 0
    end = n-1
    if n > 2:
        while start < end:
            if inputString[start].isalnum() and inputString[end].isalnum():
                if (inputString[end].lower() == inputString[start].lower() and inputString[start].isalpha() and inputString[end].isalpha()) or (inputString[start].isdigit() and inputString[end] == inputString[start]):
                    start +=1
                    end -=1
                else:
                    return False
            else:
                if not inputString[start].isalphanum():
                    start +=1
                if not inputString[end].isalphanum():
                    end -=1

        return True