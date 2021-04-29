
import logging
import random
from typing import Generator
from dataclasses import dataclass
from itertools import product

from ortools.constraint_solver.pywrapcp import DefaultRoutingSearchParameters

from utilities.solution import Solution
from utilities.assignments import solve_and_read_solution
from utilities.callbacks import constant_k
from utilities.models import Model, basic_model_with_depot

log = logging.getLogger()


@dataclass()
class ProblemBase:
    n_vehicles: int
    n_stops: int


class ImplementationBase:
    @staticmethod
    def apply(model: Model, problem: ProblemBase):
        raise NotImplementedError

    @staticmethod
    def short_name() -> str:
        raise NotImplementedError


def solve(problem: ProblemBase, search_parameters: DefaultRoutingSearchParameters, implementation: ImplementationBase) -> Solution:

    log.debug(f"n_stops = {problem.n_stops}")
    log.debug(f"n_vehicles = {problem.n_vehicles}")

    arc_cost_evaluator = constant_k(k=1)
    model = basic_model_with_depot(n_vehicles=problem.n_vehicles, n_stops=problem.n_stops, depot=0, arc_cost_evaluator=arc_cost_evaluator)
    implementation.apply(model=model, problem=problem)

    return solve_and_read_solution(model=model, search_parameters=search_parameters)


def generator(seed: int) -> Generator[ProblemBase, None, None]:
    random.seed(seed)

    for n_vehicles, n_stops in product([1, 5, 10], range(5, 101, 5)):
        yield ProblemBase(n_vehicles=n_vehicles, n_stops=n_stops)


if __name__ == "__main__":
    for x in generator(seed=1):
        print(x)