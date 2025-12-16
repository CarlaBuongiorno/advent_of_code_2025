from invalid_ids import get_invalid_ids


# def test_get_invalid_ids_exists():
#     assert get_invalid_ids


# def test_range_has_one_invalid_id():
#     assert get_invalid_ids(['10-12']) == 11


# def test_range_has_two_invalid_ids():
#     assert get_invalid_ids(['11-22']) == 33


# def test_range_has_one_invalid_id_more_numbers():
#     assert get_invalid_ids(['95-115']) == 99

 
# def test_range_has_one_invalid_id_bigger_numbers():
#     assert get_invalid_ids(['998-1012']) == 1010


# def test_range_has_one_invalid_id_huge_numbers():
#     assert get_invalid_ids(['1188511880-1188511890']) == 1188511885


# def test_range_has_no_invalid_ids():
#     assert get_invalid_ids(['1698522-1698528']) == 0


# def test_range_has_invalid_ids_more_entries():
#     assert get_invalid_ids(['10-12', '20-23']) == 33


# def test_an_overlap():
#     assert get_invalid_ids(['11-22', '22-23']) == 55


# def test_example():
#     assert get_invalid_ids([
#         '11-22', '95-115', '998-1012',
#         '1188511880-1188511890', '222220-222224',
#         '1698522-1698528', '446443-446449',
#         '38593856-38593862', '565653-565659',
#         '824824821-824824827','2121212118-2121212124'
#     ]) == 1227775554


def test_example():
    assert get_invalid_ids([
        '11-22', '95-115', '998-1012',
        '1188511880-1188511890', '222220-222224',
        '1698522-1698528', '446443-446449',
        '38593856-38593862', '565653-565659',
        '824824821-824824827','2121212118-2121212124'
    ]) == 4174379265