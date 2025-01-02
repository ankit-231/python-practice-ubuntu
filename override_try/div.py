class CustomNumber:
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        if isinstance(other, CustomNumber):
            print(
                "Dividing two CustomNumbers",
                self.value,
                other.value,
                self.value / other.value,
            )
            return CustomNumber(self.value / other.value)
        return NotImplemented

    def __repr__(self):
        return f"CustomNumber({self.value})"


# Usage
a = CustomNumber(10)
b = CustomNumber(2)

result = a / b
print(result)  # Output: CustomNumber(5.0)
