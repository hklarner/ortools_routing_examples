

from typing import Callable
import random


def constant_k(k: int) -> Callable[[int, int], int]:
    def cb(x: int, y: int) -> int:
        return k

    return cb


def random_int(a: int, b: int, seed: int) -> Callable[[int, int], int]:
    random.seed(seed)

    def cb(x: int, y: int) -> int:
        return random.randint(a, b)

    return cb


def plus() -> Callable[[int, int], int]:

    def cb(x: int, y: int) -> int:
        return x + y

    return cb
