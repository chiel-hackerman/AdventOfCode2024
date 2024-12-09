file = open('input.txt')

leftList = []
rightList = []

while True:
	content=file.readline()
	if not content:
		break
	x = content.split()
	leftList.append(int(x[0]))
	rightList.append(int(x[1]))

leftList = sorted(leftList)
rightList = sorted(rightList)

difference = []
length = len(leftList)

for n in range(length):
	if leftList[n] > rightList[n]:
		dif = leftList[n]-rightList[n]
	elif rightList[n] > leftList[n]:
		dif = rightList[n] - leftList[n]
	else:
		dif = 0
	difference.append(dif)

print(sum(difference))

similarityScore = []

for n in range(length):
	mul = rightList.count(leftList[n])
	result = leftList[n]*mul
	similarityScore.append(result)

print(sum(similarityScore))