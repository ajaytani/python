def ransom_note(magazine, ransom):
    mag = dict.fromkeys(magazine, 0)
    for i in magazine:
        if i in mag:
            mag[i] += 1
    for j in ransom:
        if j not in mag:
            return 'No'
        elif j in mag and mag[j] > 0:
            mag[j] -= 1
        else:
            return 'No'

    return 'Yes'

answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")