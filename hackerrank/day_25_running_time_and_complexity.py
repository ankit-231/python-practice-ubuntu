# def check_prime(n: int):
#     """
#     This is not efficient
#     """
#     num_divisors = 0
#     is_prime = True
#     for i in range(2, n + 1):
#         if n % i == 0:
#             num_divisors += 1
#         if num_divisors > 2:
#             is_prime = False
#             break

#     if not is_prime:
#         print("Not prime")
#     else:
#         print("Prime")


def check_prime(n: int):
    """

    Code here is inspired from https://github.com/nathan-abela/HackerRank-Solutions/blob/master/30%20Days%20of%20Code/Python/26%20-%20Day%2025%20-%20Running%20Time%20and%20Complexity.py

    A prime number is a number that is only divisible by 1 and itself, i.e, prime_num = 1 x prime_num

    So, we can also tell that, for a non-prime number,
    1. non_prime_num = 1 x non_prime_num
    2. non_prime_num = some_positive_num x another_positive_num

    Now here's one question. What's the biggest two numbers whose product can give a chosen_number. Let's say 9.

    - 9 = 1 x 9
    - 9 = 3 x 3

    This means the max numbers whose product is 9 is 3. We know that 3 is square root of 9, or 9 is square of 3.

    We can be definitely sure that:
    1. num_small_than_or_equal_to_3 x 3 = num_less_than_or_equal_to_9
    2. num_greater_than_3 x 3 = num_greater_than_9
    3. num_small_than_or_equal_to_3 x num_small_than_or_equal_to_3 = num_less_than_or_equal_to_9
    4. num_greater_than_3 x num_greater_than_3 = num_greater_than_9
    5. num_greater_than_3 x num_smaller_than_3 = (maybe) num_greater_than_or_smaller_than_or_equal_to_9

    We are interested in num_less_than_or_equal_to_9 and num_greater_than_or_smaller_than_or_equal_to_9, so we choose 1, 3 and 5. So, if we say a x b = 9, We can definitely say that a or b is less than or equal to 3.

    So, all we gotta do to check if a number is prime is: check if a num_less_than_square_root_of_the_number perfectly divides the number, i.e, num_less_than_square_root_of_the_number modulo number == 0.
    """
    is_prime = True

    if n <= 1:
        is_prime = False
    else:
        # checking if n is divisible by 2 and n is not 2.
        if n % 2 == 0 and n > 2:
            is_prime = False
        else:

            for i in range(
                3, int(get_square_root(n) + 1), 2
            ):  # skip the even numbers since they are non prime (they're divisible by 2)
                # because now i is 3, 5, 7 ... upto int(square_root of n) + 1. n is already divided by n itself, so any number dividing n would make it not prime.
                if n % i == 0:
                    is_prime = False
                    break

    if not is_prime:
        print("Not prime")
    else:
        print("Prime")


def check_prime(n: int):
    """

    Code here is inspired from ChatGPT

    A prime number is a number that is only divisible by 1 and itself, i.e, prime_num = 1 x prime_num

    So, we can also tell that, for a non-prime number,
    1. non_prime_num = 1 x non_prime_num
    2. non_prime_num = some_positive_num x another_positive_num

    Now here's one question. What's the biggest two numbers whose product can give a chosen_number. Let's say 9.

    - 9 = 1 x 9
    - 9 = 3 x 3

    This means the max numbers whose product is 9 is 3. We know that 3 is square root of 9, or 9 is square of 3.

    We can be definitely sure that:
    1. num_small_than_or_equal_to_3 x 3 = num_less_than_or_equal_to_9
    2. num_greater_than_3 x 3 = num_greater_than_9
    3. num_small_than_or_equal_to_3 x num_small_than_or_equal_to_3 = num_less_than_or_equal_to_9
    4. num_greater_than_3 x num_greater_than_3 = num_greater_than_9
    5. num_greater_than_3 x num_smaller_than_3 = (maybe) num_greater_than_or_smaller_than_or_equal_to_9

    We are interested in num_less_than_or_equal_to_9 and num_greater_than_or_smaller_than_or_equal_to_9, so we choose 1, 3 and 5. So, if we say a x b = 9, We can definitely say that a or b is less than or equal to 3.

    So, all we gotta do to check if a number is prime is: check if a num_less_than_square_root_of_the_number perfectly divides the number, i.e, num_less_than_square_root_of_the_number modulo number == 0.
    """
    is_prime = True

    if n <= 1:
        is_prime = False
    else:
        # checking if n is divisible by 2 or 3.
        """If n is divisible by a number A, and A is divisible by 3. We can definitely say that n is divisible by 3. So that means if n is not divisible by 3, we can be sure that A cannot surely divide n. Same goes with 2."""
        if n % 2 == 0 or n % 3 == 0:
            is_prime = False
        else:
            # I don't get it right now man, and am burnt out rn. Might check it out later.
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    is_prime = False
                    break
                i += 6

    if not is_prime:
        print("Not prime")
    else:
        print("Prime")


def get_square_root(n: int):
    return n ** (1 / 2)


if __name__ == "__main__":

    T = int(input())

    for i in range(T):
        n = int(input())
        check_prime(n)
