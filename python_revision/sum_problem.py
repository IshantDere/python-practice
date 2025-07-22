class EvenNumberSummer:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum_nums(self):
        total = 0
        for i in self.numbers:
            if i%2 == 0:
                total += i

        return total


# testcase 1
nums = [1, 2, 3, 4, 5, 6]
summer = EvenNumberSummer(nums)
print(summer.sum_nums())
