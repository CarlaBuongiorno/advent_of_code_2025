from banks import get_total_joltage


def test_get_total_joltage_exists():
    assert get_total_joltage


# def test_get_two_largest_number_on_the_right():
#     assert get_total_joltage(['12']) == 12


# def test_get_largest_number_on_the_left():
#     assert get_total_joltage(['21']) == 21


# def test_get_two_largest_number_out_of_6():
#     assert get_total_joltage(['212435']) == 45


# def test_get_two_largest_number_more_items():
#     assert get_total_joltage(['212534', '443647']) == 121


# def test_get_one_example():
#     assert get_total_joltage(['818181911112111']) == 92


# def test_examples():
#     assert get_total_joltage([
#         '987654321111111',
#         '811111111111119',
#         '234234234234278',
#         '818181911112111'
#     ]) == 357


# -------------- part 2 -------------- #


def test_first_example():
    assert get_total_joltage(['987654321111111']) == 987654321111


def test_second_example():
    assert get_total_joltage(['811111111111119']) == 811111111119


def test_examples():
    assert get_total_joltage([
        '987654321111111',
        '811111111111119',
        '234234234234278',
        '818181911112111'
    ]) == 3121910778619


'''
To find the nth digit:
    start from the index you found the previous digit
    find the biggest number as long as there are still at least (12 - n) numbers left
--------------------------------------------------------------------------------------
To find the 1st digit:
    start from the index you found the previous digit
    find the biggest number as long as there are still at least 11 numbers left
To find the 2nd digit:
    start from the index you found the previous digit
    find the biggest number as long as there are still at least 10 numbers left
To find the 3rd digit:
    start from the index you found the previous digit
    find the biggest number as long as there are still at least 9 numbers left
............
To find the 12th digit:
    start from the index you found the previous digit
    find the biggest number as long as there are 0 numbers left

'''