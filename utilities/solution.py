

from typing import Optional
from dataclasses import dataclass

from utilities.tours import Tours


class ReturnCodes:
    ROUTING_NOT_SOLVED = 0
    ROUTING_SUCCESS = 1
    ROUTING_FAIL_NO_SOLUTION = 2
    ROUTING_FAIL_TIMEOUT = 3
    ROUTING_INVALID = 4


@dataclass()
class Solution:
    tours: Optional[Tours]
    return_code: int
    cost: Optional[int]
