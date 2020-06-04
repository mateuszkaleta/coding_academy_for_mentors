# Card number validity can be checked using Luhn algorithm.
# https://en.wikipedia.org/wiki/Luhn_algorithm
#
# Your task is to implement this algorithm.
#
# Write function to validate credit card numbers:
#   def solution(card_number):
#
# Variable card_number will be provided as string (no spaces inside).
# Function should return True for valid card number, and False for invalid.
#
# Sample data:
# Valid card numbers
# 4111111111111111
# 5500000000000004
#
# Invalid card numbers
# 4198786787558765
# 9875787643456354


def solution(card_number):

    sum_ = int(card_number[-1])
    card_number = card_number[:-1][::-1]
    for position, digit in enumerate(card_number):
        digit = int(digit)
        if position % 2 == 0:
            digit *= 2
            digit = digit - 9 if digit > 9 else digit
        sum_ += digit
    return sum_ % 10 == 0
