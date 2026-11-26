from Parkingg import get_fee


def test_two_wheeler():
    assert get_fee("Two-wheeler", 2) == 40


def test_four_wheeler():
    assert get_fee("  FOUR-WHEELER ", 3) == 150


def test_heavy_vehicle():
    assert get_fee("heavy vehicle", 1.5) == 150