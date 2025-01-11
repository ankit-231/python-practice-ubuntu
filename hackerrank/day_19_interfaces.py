class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):

        # n = 1000 will fail cause it gives: RecursionError: maximum recursion depth exceeded in comparison
        def recursive(num):
            if num == 1:
                return 1
            else:
                if n % num == 0:
                    return num + recursive(num - 1)
                else:
                    # turns out returning the function itself is like `continue` in a loop:
                    return recursive(num - 1)

        def normal(num):
            divisors = []
            while num > 0:
                if n % num == 0:
                    divisors.append(num)
                num -= 1
            return sum(divisors)

        return normal(n)


# n = int(input())
n = 6
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
