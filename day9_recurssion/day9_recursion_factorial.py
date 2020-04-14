def recurssion(number):
    if number==1:
        return 1
    else:
        return number*recurssion(number-1)

solution = recurssion(int(input()))
print(solution)
