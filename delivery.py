from enum import IntEnum
from typing import Literal


class PackageSize(IntEnum):
    small = 0
    large = 1


def calc_delivery_payment(distance: int | float, small_size: bool, fragility: bool, workload: Literal[0, 1, 2, 3]) -> int:
    """
    Функиця расчёта стоймости доставки
    :param distance: Расстояние в км до точки назначения
    :param small_size: Размер посылки (True - да, False - большой)
    :param fragility: Хрупоксть посылки (True - хрупкая, False - не хрупкая)
    :param workload: Загруженность доставки (1 - повышенная, 2 - высокая, 3 - очень высокая, 0 - во всех остальных)
    :return: Стоймость доставки
    """
    min = 400
    payment = 0
    if distance <= 0:
        raise Exception("Расстояние не может быть отрицательным или нулем")
    elif 0 < distance < 2:
        payment += 50
    elif 2 <= distance < 10:
        payment += 100
    elif 10 <= distance < 30:
        payment += 200
    else:
        payment += 300

    payment += 100 if small_size else 200

    if fragility:
        if distance >= 30:
            raise Exception("Хрупкие грузы нельзя возить на расстояние более 30 км")
        else:
            payment += 300

    match workload:
        case 1:
            payment *= 1.2
        case 2:
            payment += payment * 0.4
        case 3:
            payment *= 1.6
        case _:
            payment *= 1.0
    if payment < min:
        return min
    return payment




