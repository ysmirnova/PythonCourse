def generatefibonacci(length):
    if length == 0:
        return 0
    else:
        a, b = 0, 1
        for i in range(2, length + 1):
            a, b = b, a + b
    return b


if __name__ == "__main__":
    print("Input number for number in Fibonacci sequence: ")
    n = int(input())
    print(generatefibonacci(n))
