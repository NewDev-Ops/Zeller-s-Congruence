import math
from typing import final


class DateCalculator:
    def __init__(self, year, month, day):
        if month == 1 or month == 2:
            month += 12
            year -= 1
        self.year = year
        self.month = month
        self.day = day

##returns k
    def calculate_of_the_century(self):
        return self.year % 100

##returns j
    def zero_based_century(self):
        return self.year // 100

##final calculation
    def final_formula(self, calculate_of_the_century, zero_based_century):
        return (self.day + (13*(self.month + 1) / 5) + calculate_of_the_century + (calculate_of_the_century / 4) + (zero_based_century / 4) + 5*zero_based_century) % 7


test = DateCalculator(2022, 1, 1)

cen = test.calculate_of_the_century()
print(cen)

zero = test.zero_based_century()
print(zero)

final = test.final_formula(cen, zero)

days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

print(days[math.floor(final)])



