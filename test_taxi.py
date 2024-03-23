from taxi import tinh_tien_taxi


def test_case_1():
    assert tinh_tien_taxi(2, 4) == 2 * 10000 + 4 * 5000


def test_case_2():
    assert tinh_tien_taxi(3, 4) == 2 * 10000 + 1 * 15000 + 4 * 5000


def test_case_3():
    assert tinh_tien_taxi(20, 9) == (2 * 10000 + 18 * 15000 + 9 * 5000)


def test_case_4():
    assert tinh_tien_taxi(20, 11) == (2 * 10000 + 18 * 15000 + 10 * 5000 + 1 * 7000)
