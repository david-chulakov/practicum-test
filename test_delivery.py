import pytest
from delivery import calc_delivery_payment


@pytest.mark.parametrize("distance, expected",
                         [(0.001, 550),
                          (1.999, 550),
                          (2, 600),
                          (2.001, 600),
                          (9.999, 600),
                          (10, 700),
                          (10.001, 700),
                          (29.999, 700)])
def test_distance_impact(distance, expected):
    result = calc_delivery_payment(distance=distance, small_size=False, fragility=True, workload=0)
    assert result == expected, (f"Не верный результат. Не корректно добавляет стоймость в зависимости от расстояния."
                                f"ОР: {expected}, ФР: {result}")


def test_fragility_long_range():
    with pytest.raises(Exception):
        calc_delivery_payment(distance=30.001, small_size=False, fragility=True, workload=0)


@pytest.mark.parametrize("small_size, expected",
                         [(True, 600),
                          (False, 700)])
def test_size_impact(small_size, expected):
    result = calc_delivery_payment(15, small_size=small_size, fragility=True, workload=0)
    assert result == expected, (f"Не верный результат. Не корректно добавляет стоймость в зависимости от габаритов."
                                f"ОР: {expected}, ФР: {result}")


@pytest.mark.parametrize("fragility, expected",
                         [(True, 700),
                          (False, 400)])
def test_fragility_impact(fragility, expected):
    result = calc_delivery_payment(15, small_size=False, fragility=fragility, workload=0)
    assert result == expected, (f"Не верный результат. Не корректно добавляет стоймость в зависимости от хрупкости."
                                f"ОР: {expected}, ФР: {result}")


@pytest.mark.parametrize("workload, expected",
                         [(0, 700),
                          (1, 840),
                          (2, 980),
                          (3, 1120),
                          (-1, 700),
                          (4, 700)])
def test_workload_impact(workload, expected):
    result = calc_delivery_payment(15, small_size=False, fragility=True, workload=workload)
    assert result == expected, (f"Не верный результат. Не корректно добавляет стоймость в зависимости от загруженности."
                                f"ОР: {expected}, ФР: {result}")


@pytest.mark.parametrize("distance, small_size, fragility, workload",
                         [(1, True, False, 0),
                          (25, True, False, 1)])
def test_lower_minimum(distance, small_size, fragility, workload):
    expected = 400
    result = calc_delivery_payment(distance=distance, small_size=small_size, fragility=fragility, workload=workload)
    assert result == expected, (f"Не верный результат. Если итог меньше 400, то стоймость должна быть 400"
                                f"ОР: {expected}, ФР: {result}")


@pytest.mark.parametrize("distance",
                         [0, -1])
def test_distance_negative(distance):
    with pytest.raises(Exception):
        calc_delivery_payment(distance=distance, small_size=True, fragility=False, workload=0)




