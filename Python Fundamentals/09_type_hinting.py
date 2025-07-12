from typing import List


def temperature_avg(temp: List) -> float:
    return sum(temp) / len(temp)


print(temperature_avg([21, 18, 25, 30, 27, 24, 19]))
# 23.428571428571427
