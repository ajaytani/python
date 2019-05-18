def balancedParen(A):
    lst = [('(',')'),('{','}'),('[',']')]

    closed = {']':'[', ')':'(' ,'}':'{' }
    stack = []
    for i in A:
        if i in closed:
            if (stack.pop(),i) in lst:
                continue
            else:
                return False
        else:
            stack.append(i)
    if len(stack) != 0:
        return False
    return True

print(balancedParen('[({})]'))

