from enum import Enum


class Day(Enum):
    MONDAY = 1,
    TUESDAY = 2,
    WEDNESDAY = 3,
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def is_weekend_day(day_name):
    if day_name.value > 5:
        print(f"{day_name.name} is weekend day")


day_status = Day.SUNDAY
is_weekend_day(day_status)

