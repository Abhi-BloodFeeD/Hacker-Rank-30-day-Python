
import sys


def main():
    totalSwap = 0

    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    # Write Your Code Heres)

    totalSwap = 0
    for x in range(0, n):
        elementalSwap = 0
        for i in range(1, n - x):
            if a[i - 1] > a[i]:
                temp = a[i]
                a[i] = a[i - 1]
                a[i - 1] = temp

                elementalSwap += 1
        totalSwap += elementalSwap
    if elementalSwap == 0:

        pass

    print("Aray is sorted in {} swaps".format(totalSwap))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[n - 1]))


main()
