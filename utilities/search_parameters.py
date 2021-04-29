

from dataclasses import dataclass

from ortools.constraint_solver.pywrapcp import DefaultRoutingSearchParameters
from ortools.constraint_solver.routing_enums_pb2 import FirstSolutionStrategy as Strategy


@dataclass()
class FirstSolutionStrategy:
    AUTOMATIC: Strategy.AUTOMATIC
    PATH_CHEAPEST_ARC: Strategy.PATH_CHEAPEST_ARC
    PATH_MOST_CONSTRAINED_ARC: Strategy.PATH_MOST_CONSTRAINED_ARC
    EVALUATOR_STRATEGY: Strategy.EVALUATOR_STRATEGY
    SAVINGS: Strategy.SAVINGS
    SWEEP: Strategy.SWEEP
    CHRISTOFIDES: Strategy.CHRISTOFIDES
    ALL_UNPERFORMED: Strategy.ALL_UNPERFORMED
    BEST_INSERTION: Strategy.BEST_INSERTION
    PARALLEL_CHEAPEST_INSERTION: Strategy.PARALLEL_CHEAPEST_INSERTION
    LOCAL_CHEAPEST_INSERTION: Strategy.LOCAL_CHEAPEST_INSERTION
    GLOBAL_CHEAPEST_ARC: Strategy.GLOBAL_CHEAPEST_ARC
    LOCAL_CHEAPEST_ARC: Strategy.LOCAL_CHEAPEST_ARC
    FIRST_UNBOUND_MIN_VALUE: Strategy.FIRST_UNBOUND_MIN_VALUE


def create_search_parameters(time_limit_seconds: int, first_solution_strategy: int) -> DefaultRoutingSearchParameters():
    search_parameters = DefaultRoutingSearchParameters()
    search_parameters.time_limit.seconds = time_limit_seconds

    if first_solution_strategy is not None:
        search_parameters.first_solution_strategy = first_solution_strategy

    return search_parameters


if __name__ == '__main__':
    for x in FirstSolutionStrategy.__annotations__:
        print(x)
