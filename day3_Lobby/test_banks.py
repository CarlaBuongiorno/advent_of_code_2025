from banks import get_total_joltage


def test_get_total_joltage_exists():
    assert get_total_joltage


def test_get_two_largest_number_on_the_right():
    assert get_total_joltage(['12']) == 12


def test_get_largest_number_on_the_left():
    assert get_total_joltage(['21']) == 21


def test_get_two_largest_number_out_of_6():
    assert get_total_joltage(['212435']) == 45


def test_get_two_largest_number_more_items():
    assert get_total_joltage(['212534', '443647']) == 121


def test_get_one_example():
    assert get_total_joltage(['818181911112111']) == 92


def test_examples():
    assert get_total_joltage([
        '987654321111111',
        '811111111111119',
        '234234234234278',
        '818181911112111'
    ]) == 357