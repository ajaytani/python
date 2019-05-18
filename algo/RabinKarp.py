class RabinKarp(object):
    def __init__(self):
        self.prime = 3
    def recalculatehash(self,S,oldIndex,newIndex,patternLength,oldHash):
        newHash = oldHash - ord(S[oldIndex])
        newHash = newHash/self.prime
        newHash += ord(S[newIndex])*pow(self.prime,patternLength-1)
        return newHash

    def createHash(self,S,endIndex):
        hashvalue = 0
        for i in range(endIndex+1):
            hashvalue +=ord(S[i])*pow(self.prime,i)

        return hashvalue

    def patternSearch(self,text, pattern):
        m = pattern.length
        n = text.length
        patternHash = self.createHash(pattern, m - 1)
        textHash = self.createHash(text, m - 1)
        for i  in n - m + 1:
            if patternHash == textHash and self.checkEqual(text, i - 1, i + m - 2, pattern, 0, m - 1):
                return i - 1

            if i < n - m + 1:
                textHash = self.recalculateHash(text, i - 1, i + m - 1, textHash, m)
        return -1

    def checkEqual(self):
        pass
    


