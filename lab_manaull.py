#Write a function factorial(n) that calculates the factorial of a non-negative integer n (n!).
def factorial(n):
    if n == 0:
        return
    else:
        return n*factorial(n-1)

print(factorial(67))
    
#Write a function is_palindrome(n) that checks if a number reads the same forwards and backwards.
def is_palindrome(n):
    s=str(n)
    return s == s[ : : -1]

print(is_palindrome(88))

#Write a function mean_of_digits(n) that returns the average of all digits in a number.
def mean_of_digits(n):
    digits=[int(d) for d in str(n)]
    mean = sum(digits)/len(digits)
    return mean

print(mean_of_digits(34))

#Write a function digital_root(n) that repeatedly sums the digits of a number until a single digit is obtained.
def digital_root(n):
    while n>=10:
        n=sum(int(digit) for digit in str(n))
    return n

print(digital_root(90))

#Write a function is_abundant(n) that returns True if the sum of proper divisors of n is greater than n.
def is_abundant(n):
    if n <= 0:
        return False
    proper_divisor_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            proper_divisor_sum += i

print(is_abundant(34))

#Write a function is_deficient(n) that returns True if the sum of proper divisors of n is less than n.
def is_deficiebt(n):
    sum_divisors = 0
    for i in range(1,n):
        if n%i==0:
            sum_divisors+=i
    return sum_divisors < n

print(is_deficiebt(10))

#Write a function for harshad number is_harshad(n) that checks if a number is divisible by the sum of its digits.
def is_harshad(n):
    sum_digits = 0
    temp = n
    while temp>0:
        digit = temp%10
        sum_digits+=digit
        temp//=10
    return n%sum_digits==0

print(is_harshad(20))

#Write a function is_automorphic(n) that checks if a number's square ends with the number itself.
def is_automorphic(n):
    square = n*n
    return str(square).endswith(str(n))

print(is_automorphic(25))

#Write a function is_pronic(n) that checks if a number is the product of two consecutive integers.
def is_pronic(n):
    i = 0
    while i*(i+1)<=n:
        if i*(i+1)==n:
            return True
        i+=1
    return False

print(is_pronic(19))
            
#Write a function count_distinct_prime_factors(n) that returns how many unique prime factors a number has.
def count_distinct_prime_factors(n):
    count = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        count += 1
    return count

print(count_distinct_prime_factors(11))

#Write a function is_prime_power(n) that checks if a number can be expressed as pk where p is prime and k ≥ 1.

def is_prime_power(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime(p):
            k = 1
            power = p
            while power <= n:
                if power == n:
                    return True
                k += 1
                power = p ** k
    return False

print(is_prime_power(12))

#Write a function is_mersenne_prime(p) that checks if 2p - 1 is a prime number (given that p is prime).

def is_mersenne_prime(p):
     # Helper function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if not is_prime(p):
        return False
    mersenne_number = 2 ** p - 1
    return is_prime(mersenne_number)

print(is_mersenne_prime(11))

#Write a function twin_primes(limit) that generates all twin prime pairs up to a given limit.
def is_prime(n):
    #Check if a number is prime.
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(45))
def twin_primes(limit):
    #Generate all twin prime pairs up to a given limit.
    twins = []
    for i in range(2, limit - 1):
        if is_prime(i) and is_prime(i + 2):
            twins.append((i, i + 2))
    return twins

print(twin_primes(100))


#Write a function Number of Divisors (d(n)) count_divisors(n) that returns how many positive divisors a number has.
def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i == n // i:
                count += 1  
            else:
                count += 2
    return count

print(count_divisors(12))       

#Write a function aliquot_sum(n) that returns the sum of all proper divisors of n (divisors less than n).
def aliquot_sum(n):
    if n <= 1:
        return 0  
    
    total = 1  
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:   
                total += n // i
        i += 1
    
    return total

print(aliquot_sum(23))

#Write a function are_amicable(a, b) that checks if two numbers are amicable (sum of proper divisors of a equals b and vice versa).
def aliquot_sum(n):
    if n <= 1:
        return 0
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total

def are_amicable(a, b):
    return aliquot_sum(a) == b and aliquot_sum(b) == a

print(are_amicable(220, 284)) 

#Write a function multiplicative_persistence(n) that countshow many steps until a number's digits multiply to a single digit.
def multiplicative_persistence(n):
    count = 0
    
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        
        n = product
        count += 1
    
    return count

print(multiplicative_persistence(39))

#Write a function is_highly_composite(n) that checks if a number has more divisors than any smaller number.
def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2  # i and n/i
    if int(n*0.5)*2 == n:
        count -= 1  # perfect square correction
    return count


def is_highly_composite(n):
    d_n = count_divisors(n)
    
    # Compare with all smaller numbers
    for k in range(1, n):
        if count_divisors(k) >= d_n:
            return False
    return True

print(is_highly_composite(89))

#Write a function for Modular Exponentiation mod_exp(base, exponent, modulus) that efficiently calculates (baseexponent) % modulus.
def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus  

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2

    return result

print(mod_exp(2, 10, 1000))

#Write a function Modular Multiplicative Inverse mod_inverse(a, m) that finds the number x such that (a * x) ≡ 1 mod m.
def mod_inverse(a, m):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  

    return x % m     

print(mod_inverse(3, 11))

#Write a function chinese Remainder Theorem Solver crt(remainders, moduli) that solves a system of congruences x ≡ ri mod mi.
def crt(remainders, moduli):
    from functools import reduce
    
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        else:
            g, x, y = extended_gcd(b, a % b)
            return g, y, x - (a // b) * y

    M = reduce(lambda a, b: a * b, moduli)
    x = 0
    for ri, mi in zip(remainders, moduli):
        Mi = M // mi
        _, inverse, _ = extended_gcd(Mi, mi)
        inverse = inverse % mi
        x += ri * Mi * inverse
    return x % M, M

remainders = [2, 3, 2]
moduli = [3, 5, 7]
solution, modulus = crt(remainders, moduli)
print(f"x ≡ {solution} mod {modulus}") # Output: x ≡ 23 mod 105

#Write a function Quadratic Residue Check is_quadratic_residue(a, p) that checks if x2 ≡ a mod p has a solution.
def is_quadratic_residue(a, p):
    if a % p == 0:
        return True  
    return pow(a, (p - 1) // 2, p) == 1

print(is_quadratic_residue(4,3))

#Write a function order_mod(a, n) that finds the smallest positive integer k such that ak ≡ 1 mod n.
def order_mod(a, n):
    if gcd(a, n) != 1:
        return -1  
    
    k = 1
    current = a % n
    while current != 1:
        current = (current * a) % n
        k += 1
    
    return k

from math import gcd

print(order_mod(5,9))

#Write a function Fibonacci Prime Check is_fibonacci_prime(n) that checks if a number is both Fibonacci and prime.
import math

# Function to check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if number is Fibonacci
def is_fibonacci(n):
    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4
    return int(math.sqrt(x1))*2 == x1 or int(math.sqrt(x2))*2 == x2

# Main function: Fibonacci Prime Check
def is_fibonacci_prime(n):
    return is_prime(n) and is_fibonacci(n)

print(is_fibonacci_prime(5))

#Write a function Lucas Numbers Generator lucas_sequence(n) that generates the first n Lucas numbers (similar to Fibonacci but starts with 2,1).
def lucas_sequence(n):
    # Handle small values
    if n <= 0:
        return []
    if n == 1:
        return [2]
    if n == 2:
        return [2, 1]

    # Start with first two Lucas numbers
    lucas = [2, 1]

    # Generate remaining terms
    for i in range(2, n):
        next_value = lucas[i-1] + lucas[i-2]
        lucas.append(next_value)

    return lucas

print(lucas_sequence(5))

#Write a function for Perfect Powers Check is_perfect_power(n) that checks if a number can beexpressed as ab where a > 0 and b > 1.
import math

def is_perfect_power(n):
    if n <= 1:
        return False   # 0 and 1 are usually not considered perfect powers
    
    # maximum possible exponent is log2(n)
    max_b = int(math.log2(n))

    for b in range(2, max_b + 1):
        # compute the b-th root of n
        a = round(n ** (1 / b))

        # check if a^b equals n
        if a > 1 and a ** b == n:
            return True

    return False

print(is_perfect_power(90))

#Write a function Collatz Sequence Length collatz_length(n) that returns the number of steps for n to reach 1 in the Collatz conjecture.
def collatz_length(n):
    steps = 0
    
    while n != 1:
        if n % 2 == 0:       # even
            n = n // 2
        else:               # odd
            n = 3 * n + 1
        steps += 1
    
    return steps

print(collatz_length(6))

#Write a function Polygonal Numbers polygonal_number(s, n) that returns the n-th s-gonal number.
def polygonal_number(s, n):
    """
    Returns the n-th s-gonal number.
    s = number of sides (3 = triangular, 4 = square, 5 = pentagonal, ...)
    n = term index
    """
    return ((s - 2) * n * n - (s - 4) * n) // 2

print(polygonal_number(3, 5))  

#Implement the probabilistic Miller-Rabin test is_prime_miller_rabin(n, k) with k rounds.
import random

def is_prime_miller_rabin(n: int, k: int = 5) -> bool:

    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    def try_composite(a: int) -> bool:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return False
        return True  
    for _ in range(k):
        a = random.randrange(2, n - 1)
        if try_composite(a):
            return False

    return True  

print(is_prime_miller_rabin(561, k=8))


#Implement pollard_rho(n) for integer factorization using Pollard's rho algorithm.
def pollard_rho(n):
    if n % 2 == 0:
        return 2  
    def f(x, c):
        return (x*x + c) % n
    for _ in range(5):
        x = random.randint(2, n-1)
        y = x
        c = random.randint(1, n-1)
        d = 1
        while d == 1:
            x = f(x, c)           
            y = f(f(y, c), c)     
            d = math.gcd(abs(x - y), n)

        if d != n:  
            return d

    return None  

n = 8051
factor = pollard_rho(n)
print(f"One factor of {n} is: {factor}")

#Write a function zeta_approx(s, terms) that approximates the Riemann zeta function ζ(s) using the first 'terms' of the series.
def zeta_approx(s, terms):
    total = 0.0 + 0.0j 
    for n in range(1, terms + 1):
        total += 1 / (n ** s)
    return total

print(zeta_approx(8,9))

#Write a function Partition Function p(n) partition_function(n) that calculates the number of distinct ways to write n as a sum of positive integers.
def partition_function(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i range (1, n+1):
        for j in range(i, n+1):
            dp[j]+=dp[j-1]
    return dp[n]

print(partition_function(89))

#Write a function Carmichael Number Check is_carmichael(n) that checks if a composite number
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def is_carmichael(n):
    if n < 3 or is_prime(n):
        return False
    for a in range(2, n):
        if math.gcd(a, n) == 1:  
            if pow(a, n-1, n) != 1:
                return False  
    return True  

for num in [561, 1105, 1729, 15, 7]:
    print(num, is_carmichael(num))









   
     
    
       

