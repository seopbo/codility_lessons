def count_digits(n):
    result = 0

    while n > 0:
        n = n // 10
        result += 1

    return result


def test_count_digits():
    assert count_digits(20) == 2