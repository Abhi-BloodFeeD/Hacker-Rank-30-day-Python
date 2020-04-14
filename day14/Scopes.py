class Difference:
    def __init__(self, array):
        self.__elements = array

        # Add your code here
    def computeDifference(self):
        maxValue = max(self.__elements)
        minValue = min(self.__elements)
        self.maximumDifference = maxValue - minValue

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
