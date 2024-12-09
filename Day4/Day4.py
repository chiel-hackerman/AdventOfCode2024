file = open("example.txt")

matrix = []

while True:
    content=file.readline()
    if not content:
        break
    content = list(content)
    content.pop()
    matrix.append(content)
def addPadding(m):
    newMatrix = []
    for x in m:
        x = ['O', 'O', 'O'] + x + ['O', 'O', 'O']
        newMatrix.append(x)

    padding = []
    length = len(newMatrix[0])
    for o in range(length):
        padding.append('O')

    newMatrix.append(padding)
    newMatrix.append(padding)
    newMatrix.append(padding)
    newMatrix.insert(0, padding)
    newMatrix.insert(0, padding)
    newMatrix.insert(0, padding)

    return newMatrix

matrix = addPadding(matrix)

for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        print(matrix[y][x])


print(matrix)

