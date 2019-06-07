"""
Even Fibonacci Numbers.

# Question
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""


class FibonacciOperations:
    """Calculate Fibonacci numbers."""

    def __init__(self, start_number=1, max_number=100):
        """Initialize variables."""
        self.start = start_number
        self.max = max_number

    def generate_fibonacci_list(self):
        """Generate fibonacci numbers for given range."""
        number_list = [self.start]

        for index, number in enumerate(number_list):
            previous_number = number_list[index - 1]
            if number == self.start:
                next_number = number + 1
            else:
                next_number = previous_number + number

            if next_number > self.max:
                break

            number_list.append(next_number)

        print(number_list)
        return number_list

    def calculate_sum(self, number_list):
        """Calculate sum of generated fibonacci list."""
        sum = 0
        for number in number_list:
            if number % 2 == 0:
                sum += number

        return sum


fibo = FibonacciOperations(1, 4000000)
answer = fibo.calculate_sum(fibo.generate_fibonacci_list())
print(answer)