from password import get_password


def test_get_password_exists():
    assert get_password


def test_right_zero_():
    assert get_password(['R0']) == 0


def test_left_zero_():
    assert get_password(['L0']) == 0


def test_right_one_():
    assert get_password(['R1']) == 0


def test_left_50():
    assert get_password(['L50']) == 1


def test_right_50():
    assert get_password(['R50']) == 1


def test_right_51():
    assert get_password(['R50']) == 0