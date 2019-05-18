def sumPairs(A):
    """
    :param A:
    :return:
    """
    dict = {}
    for A1 in range(len(A)):
      for B1 in range(A1, len(A)):
          if A[A1] + A[B1]  in dict and len(dict[A[A1] + A[B1]]) == 1:
              dict[A[A1] + A[B1]].append((A1,B1))
          elif A[A1] + A[B1] not in dict :
              dict[A[A1] + A[B1]] = [(A1,B1)]



