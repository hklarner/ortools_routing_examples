

from typing import Optional

from ortools.constraint_solver.pywrapcp import RoutingModel, RoutingIndexManager, DefaultRoutingSearchParameters, Assignment

from utilities.tours import Tours
from utilities.solution import Solution
from utilities.models import Model


def read_solution(model: Model, assignment: Assignment) -> Solution:
    return_code = model.routing_model.status()

    if assignment is None:
        return Solution(tours=None, return_code=return_code, cost=None)

    n_vehicles = model.routing_model.vehicles()
    tour_indices = []
    for vehicle_ix in range(n_vehicles):

        x = model.routing_model.Start(vehicle_ix)
        indices = [x]

        while not model.routing_model.IsEnd(x):
            x = assignment.Value(model.routing_model.NextVar(x))
            indices.append(x)

        tour_indices.append(int(x) for x in map(model.index_manager.IndexToNode, indices))

    tours = Tours(indices=tuple(tuple(x) for x in tour_indices))
    cost = assignment.ObjectiveValue()

    # todo:
    #routes = [model.routing_model.vehicles() * []]
    #model.routing_model.AssignmentToRoutes(assignment=assignment, routes=routes)
    #x = model.routing_model.IsMatchingModel()

    return Solution(tours=tours, return_code=return_code, cost=cost)


def print_solution(routing_model: RoutingModel, index_manager: RoutingIndexManager, assignment: Assignment):
    model = Model(routing_model=routing_model, index_manager=index_manager)
    print(read_solution(model=model, assignment=assignment))


def solve_and_read_solution(model: Model, search_parameters: Optional[DefaultRoutingSearchParameters]) -> Solution:
    if search_parameters is not None:
        assignment = model.routing_model.SolveWithParameters(search_parameters)
    else:
        assignment = model.routing_model.Solve()

    return read_solution(model=model, assignment=assignment)
