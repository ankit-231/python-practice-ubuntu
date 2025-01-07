class Difference:
    def __init__(self, a: list[int]):
        self.__elements = a
        # I think you can initialize maximumDifference as 0 cause min absolute diff is 0.
        # But still I'm keeping it as None.
        self.maximumDifference = None

    # Normal Method
    def computeDifference(self):
        # for i in range(len(self.__elements)):
        #     difference = self.__elements[i] - self.__elements[i + 1]
        temp_elements = self.__elements
        diff_arr = []
        while len(temp_elements) > 1:
            for i in range(len(temp_elements) - 1):
                difference = temp_elements[0] - temp_elements[i + 1]
                abs_diff = abs(difference)
                diff_arr.append(abs_diff)
            temp_elements.pop(0)

        if self.maximumDifference is None:
            self.maximumDifference = max(diff_arr)

    # Recursive Method: I could not figure out
    # def rComputeDifference(self):
    #     def max_diff_recursive(arr: list[int]):
    #         max_diff = None
    #         if len(arr) == 1:
    #             if max_diff is None or max_diff > 0:
    #                 max_diff = 0
    #             return max_diff
    #         else:
    #             diff_arr = []
    #             for i in range(len(arr) - 1):
    #                 difference = arr[0] - arr[i + 1]
    #                 abs_diff = abs(difference)
    #                 diff_arr.append(abs_diff)

    #             return max(abs_diff) or max_diff_recursive(arr.pop(0))


# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(" ")]
# a = [int(e) for e in "1 2 5".split(" ")]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
