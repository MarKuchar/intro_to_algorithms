# The Apocalypse
import random


def run_one_family() -> [int]:
    """
    Returns a number of girls and boys in one family by randomly choosing gender

    :return: list of [number of girls, number of boys] in one family
    """
    boys = 0
    girls = 0
    while girls == 0:
        # randomly choose between 0(Girl), 1(Boy)
        if random.choice([0, 1]) == 0:
            girls += 1
        else:
            boys += 1

    return [girls, boys]


def run_n_families(n: int) -> float:
    """
    Returns the gender ratio of the new generation.
    :param n: the number of families
    :return: ratio between girls/boys
    """
    boys = 0
    girls = 0
    for _ in range(n):
        genders = run_one_family()
        girls += genders[0]
        boys += genders[1]
    return girls / boys


if __name__ == "__main__":
    for n in range(1_000, 2_000):
        print(f"ratio(girls/boys) for {n} families: {run_n_families(n)}")
