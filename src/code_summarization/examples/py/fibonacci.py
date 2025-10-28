import json


def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def main(n: int):
    """
    Calculate the n-th Fibonacci number.
    """
    result = fibonacci(n)
    output = {
        "input": n,
        "fibonacci_number": result
    }
    print(json.dumps(output, indent=4))


if __name__ == "__main__":
    n = 10
    main(n)
