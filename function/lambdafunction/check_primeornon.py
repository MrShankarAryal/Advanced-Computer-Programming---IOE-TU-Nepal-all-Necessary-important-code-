is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
number = int(input("Enter a number: "))
print(f"The number {number} is {'prime' if is_prime(number) else 'not prime'}.")