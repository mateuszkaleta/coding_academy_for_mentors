# Write a function:
#
#     def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
#         N is an integer within the range [1..100,000];
#         each element of array A is an integer within the range [−1,000,000..1,000,000].
#


def __merge_sort(A):

    result = A[::]
    part_size = 1
    while part_size < len(A):
        left_beginning = 0
        while left_beginning < len(A) - 1:
            middle = left_beginning + part_size
            right_end = min(middle + part_size, len(A))
            left = result[left_beginning:middle]
            right = result[middle:right_end]
            left_index = right_index = 0
            while left_index < len(left) and right_index < len(right):
                if left[left_index] > right[right_index]:
                    result[left_beginning + left_index+right_index] = right[right_index]
                    right_index += 1
                else:
                    result[left_beginning + left_index + right_index] = left[left_index]
                    left_index += 1
            while left_index < len(left):
                result[left_beginning + left_index + right_index] = left[left_index]
                left_index += 1
            while right_index < len(right):
                result[left_beginning + left_index + right_index] = right[right_index]
                right_index += 1
            left_beginning += 2*part_size
        part_size *= 2
    return result


def solution(A):
    min_missing_int = 1
    for k in __merge_sort(A):
        # albo tablica hashująca... :)
        if k >= min_missing_int:
            min_missing_int = k + 1
    return min_missing_int
