array_final = []
arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

for cc in range(0, 4):
    for rr in range(0, 4):
        try:
            a = arr[rr][cc]
            #print("a" + str(a))

            b = arr[rr][cc + 1]
            #print("b" + str(b))

            c = arr[rr][cc + 2]
            #print("c" + str(c))
            d = arr[rr + 1][cc + 1]
            #print("d" + str(d))
            e = arr[rr + 2][cc]
            #print("e" + str(e))
            f = arr[rr + 2][cc + 1]
            #print("f" + str(f))
            g = arr[rr + 2][cc + 2]
            #print("g" + str(g))

            sum = (a + b + c + d + e + f + g)

            # print(sum)
            array_final.append(sum)
        except IndexError:
            continue

print(max(array_final))
