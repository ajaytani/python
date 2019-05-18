def rotate(array, nelts):
    k = nelts % len(array)
    return array[k:] + array[:k]