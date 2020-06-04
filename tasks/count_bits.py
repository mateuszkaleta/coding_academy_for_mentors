# Write a function:
#
#     def solution(A, B)
#
# that, given two non-negative integers A and B, returns the number of bits set to 1 in the binary representation
# of the number A * B.
#
# For example, given A = 3 and B = 7 the function should return 3, because the binary representation of
# A * B = 3 * 7 = 21 is 10101 and it contains three bits set to 1.
#
# Assume that:
# A and B are integers within the range [0..100,000,000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.


def solution(A, B):

    assert A >= 0
    assert B >= 0

    product = A*B
    amount_of_ones = 0
    while product >= 1:
        amount_of_ones += product % 2
        product //= 2
    return amount_of_ones
