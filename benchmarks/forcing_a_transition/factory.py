

import logging
import random
from typing import Tuple, Callable, Generator
from dataclasses import dataclass
from itertools import product

from ortools.constraint_solver.pywrapcp import DefaultRoutingSearchParameters

from benchmarks.templates import ImplementationBase, ProblemBase
from utilities.solution import Solution
from utilities.assignments import solve_and_read_solution
from utilities.callbacks import constant_k
from utilities.models import basic_model_with_depot, Model
from utilities.dimensions import add_stop_count_dimension

log = logging.getLogger()


@dataclass()
class Problem(ProblemBase):
    n_vehicles: int
    n_stops: int
    transition: Tuple[int, int]
    vehicle_stop_capacity: int


def solve(problem: Problem, search_parameters: DefaultRoutingSearchParameters, implementation: ImplementationBase) -> Solution:

    log.debug(f"n_stops = {problem.n_stops}")
    log.debug(f"n_vehicles = {problem.n_vehicles}")
    log.debug(f"capacity = {problem.vehicle_stop_capacity}")

    arc_cost_evaluator = constant_k(k=1)
    model = basic_model_with_depot(n_vehicles=problem.n_vehicles, n_stops=problem.n_stops, depot=0, arc_cost_evaluator=arc_cost_evaluator)
    add_stop_count_dimension(model=model, capacity=problem.vehicle_stop_capacity)

    if implementation is not None:
        implementation.apply(model=model, problem=problem)

    return solve_and_read_solution(model=model, search_parameters=search_parameters)


def generator(seed: int) -> Generator[Problem, None, None]:
    random.seed(seed)

    for n_vehicles, n_stops in product([1, 5, 10], range(5, 101, 5)):
        capacity = round(n_stops / n_vehicles + 2)

        x, y = random.sample(population=range(1, n_stops), k=2)
        transition = (x, y)

        yield Problem(n_vehicles=n_vehicles, n_stops=n_stops, vehicle_stop_capacity=capacity, transition=transition)


if __name__ == "__main__":
    for x in generator(seed=1):
        print(x)
