

from ortools.constraint_solver.pywrapcp import RoutingIndexManager, RoutingModel, DefaultRoutingSearchParameters

from benchmarks.forcing_a_transition.factory import Problem
from utilities.assignments import print_solution


def run():
    """
    - 3 vehicles should serve 10 stops
    - each vehicle can serve at most 4 stops
    - the transition (7, 4) must occur on some tour
    """

    problem = Problem(n_vehicles=3, n_stops=10, transition=(7, 4), vehicle_stop_capacity=4)
    search_parameters = DefaultRoutingSearchParameters()
    search_parameters.time_limit.seconds = 10

    start_locations = problem.n_vehicles * [0]
    end_locations = problem.n_vehicles * [0]
    index_manager = RoutingIndexManager(problem.n_stops, problem.n_vehicles, start_locations, end_locations)
    routing_model = RoutingModel(index_manager)

    def constant_callback(x: int, y: int) -> int:
        return 1

    callback_index = routing_model.RegisterTransitCallback(callback=constant_callback)
    routing_model.SetArcCostEvaluatorOfAllVehicles(callback_index)

    routing_model.AddDimension(
        evaluator_index=callback_index,
        slack_max=0,
        capacity=problem.vehicle_stop_capacity,
        fix_start_cumul_to_zero=True,
        name="stop_count_dimension")

    nx, ny = problem.transition
    ix = index_manager.NodeToIndex(nx)
    iy = index_manager.NodeToIndex(ny)
    routing_model.NextVar(ix).SetValues([ix, iy])

    assignment = routing_model.SolveWithParameters(search_parameters)

    print(problem)

    if assignment is not None:
        print_solution(routing_model=routing_model, index_manager=index_manager, assignment=assignment)
    else:
        print(f"{assignment=}")


if __name__ == '__main__':
    run()
