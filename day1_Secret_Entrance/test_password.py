from password import get_password


def test_get_password_exists():
    assert get_password


def test_right_zero_():
    assert get_password(['R0']) == 0


def test_left_zero_():
    assert get_password(['L0']) == 0


def test_right_one_():
    assert get_password(['R5']) == 0


def test_left_50():
    assert get_password(['L50']) == 1


def test_right_50():
    assert get_password(['R50']) == 1


def test_right_51():
    assert get_password(['R51']) == 0


def test_right_150():
    assert get_password(['R150']) == 1


def test_right_250():
    assert get_password(['R250']) == 1


def test_right_200():
    assert get_password(['R200']) == 0


def test_two_rotations_right():
    assert get_password(['R50', 'R50']) == 1


def test_two_rotations_left():
    assert get_password(['L50', 'L50']) == 1


def test_three_rotations():
    assert get_password(['R50', 'R100', 'L4']) == 2