# The given code was taken from AI chatbot


# Contributor: Yunisha
# Contribution: A utility to calculate factorial for math/DSA practice


def calculate_factorial(n):
    """Calculate factorial iteratively."""
    if n < 0:
        return "Factorial does not exist for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    test_num = 5
    print(
        f"The factorial of {test_num} is: {calculate_factorial(test_num)}"
    )