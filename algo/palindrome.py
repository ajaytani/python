def palindromeCheck(S1):
    n =  len(S1)
    if n <=1:
        return True
    if n == 2:
        return S1[0] ==S1[1]

    if n > 2:
        start = 0
        end = n-1
        while start < n and end >= 0:
            if S1[start].isalnum() and S1[end].isalnum():
                if (S1[end].lower() == S1[start].lower() and S1[start].isalnum() and S1[end].isalnum()) or (S1[start].isdigit() and S1[end] == S1[start]) :
                    start +=1
                    end -=1
                else:
                    return False
            elif not S1[start].isalnum():
                start +=1
            elif not S1[end].isalnum():
                end -=1
        return True

print(palindromeCheck('A man, a plan, a canal, Panama!'))



