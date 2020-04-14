array = []


def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    array.append(num % 2)


call = decimalToBinary(int(input()))
# print(array)

countOfOne = 0
maxCount = 0
for elements in array:
    if elements == 1:
        countOfOne += 1
        if maxCount < countOfOne:
            maxCount = countOfOne
        # print("1s")
        # print(countOfOne)
    else:
        if maxCount < countOfOne:
            maxCount = countOfOne
       # print(countOfOne)
        countOfOne = 0
print(maxCount)
