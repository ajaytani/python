def reverse(w):
    x =len(w)
    if len(w) <= 1:
        return w
    else:
        print (w)
        return [w[-1]] + (reverse(w[:-1]))


def sentencereversal(S):
    words = []
    i = 0
    l =len(S)
    if l <=1:
        return S
    else:
        while i < l:
            if S[i] !=' ':
                word_start = i
                while i < l and S[i] != ' ':
                    i +=1
                words.append(S[word_start:i+1])
            i +=1
    return ' '.join(reverse(words))




print(sentencereversal('a nice shirt is presented'))
