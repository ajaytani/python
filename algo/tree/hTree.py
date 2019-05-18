def hTree(startLength, origin, depth):
    if depth == 0:
        return
    else:
        topLeft = [origin[0] - startLength / 2, origin[1] + startLength / 2]
        bottomLeft = [origin[0] - startLength / 2, origin[1] - startLength / 2]
        topRight = [origin[0] + startLength / 2, origin[1] + startLength / 2]
        bottomRight = [origin[0] + startLength / 2, origin[1] - startLength / 2]
        leftCenter = [origin[0] - startLength / 2, origin[1]]
        rightCenter = [origin[0] + startLength / 2, origin[1]]

        drawLine(topLeft, bottomLeft)
        drawLine(topRight, bottomRight)
        drawLine(leftCenter, rightCenter)

        hTree(startLength / sqrt(2), topLeft, depth - 1)
        hTree(startLength / sqrt(2), topRight, depth - 1)
        hTree(startLength / sqrt(2), bottomRight, depth - 1)
        hTree(startLength / sqrt(2), bottomLeft, depth - 1)


def main():
    hTree(5, [0, 0], 3)