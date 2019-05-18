from collections import deque
word, result = 'aaabccddd', deque()
for ch in word:
    if result and result[-1] == ch:
        print(ch)
        result.pop()
    else:
        result.append(ch)

if result:
    print('')
else:
    print (''.join(result))