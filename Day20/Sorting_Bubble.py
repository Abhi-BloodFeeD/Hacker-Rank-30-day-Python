
#     ____ RECHECK _______SOME ERRORS OCCURED
##########INCOMPLETE#############

import sys
def BubbleSort(S, i, temporarySwap):
    if S[i - 1] > S[i]:
        temp = S[i]
        S[i] = S[i - 1]
        S[i - 1] = temp
        temporarySwap += 1


def main():
    totalSwap = 0
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    # Write Your Code Heres)
    for x in range(n):
        temporarySwap = 0
        for y in range(n - x):
            BubbleSort(a, x, temporarySwap)
        if temporarySwap == 0:
            break
        totalSwap += temporarySwap
    print("Aray is sorted in {} swaps".format())


if __name__ == "__main__":
    main()
