

from ortools.constraint_solver.pywrapcp import RoutingIndexManager, RoutingModel, DefaultRoutingSearchParameters

from utilities.assignments import print_solution


def run():
    """
    - 3 vehicles service 10 stops
    - cost is sum of all transition durations
    - transit distance between stops is constant 20 meters
    - vehicle speeds are 1, 10, 5 meters per second

    -> cheapest solution is to only use the fastest vehicle
    -> objective of cheapest solution = 20
    """

    n_vehicles = 3
    n_stops = 10
    vehicle_speeds_ms = [1, 10, 5]
    distance_m = 20
    vehicle_transit_s = [int(distance_m / speed) for speed in vehicle_speeds_ms]

    assert n_vehicles == len(vehicle_speeds_ms)
    assert all(x >= 0 for x in vehicle_transit_s)

    search_parameters = DefaultRoutingSearchParameters()
    search_parameters.time_limit.seconds = 10

    start_locations = n_vehicles * [0]
    end_locations = n_vehicles * [0]
    index_manager = RoutingIndexManager(n_stops, n_vehicles, start_locations, end_locations)
    routing_model = RoutingModel(index_manager)

    evaluator_indices = []
    for vehicle, seconds in enumerate(vehicle_transit_s):
        index = routing_model.RegisterTransitCallback(callback=lambda x, y: seconds)
        evaluator_indices.append(index)
        print(vehicle, seconds)
        routing_model.SetArcCostEvaluatorOfVehicle(evaluator_index=index, vehicle=vehicle)

    routing_model.AddDimensionWithVehicleTransits(
        evaluator_indices=evaluator_indices,
        slack_max=0,
        capacity=1000000,
        fix_start_cumul_to_zero=True,
        name="transit_seconds")

    assignment = routing_model.SolveWithParameters(search_parameters)

    if assignment is not None:
        print_solution(routing_model=routing_model, index_manager=index_manager, assignment=assignment)
    else:
        print(f"{assignment=}")


if __name__ == '__main__':
    run()
