class PrimeRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_primes(self):
        for num in range(self.start, self.end + 1):
            if num > 1:
                for i in range(2, int(num**0.5) + 1):
                    if num % i == 0:
                        break
                else:
                    print(num)

start = (int(input("Enter start: ")))
end = (int(input("Enter end: ")))
obj = PrimeRange(start, end)
obj.print_primes()