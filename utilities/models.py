

from typing import Callable
from dataclasses import dataclass

from ortools.constraint_solver.pywrapcp import RoutingIndexManager, RoutingModel


@dataclass()
class Model:
    routing_model: RoutingModel
    index_manager: RoutingIndexManager


def basic_model_with_depot(n_vehicles: int, n_stops: int, depot: int, arc_cost_evaluator: Callable[[int, int], int]) -> Model:
    if depot >= n_stops:
        raise ValueError(f"depot index too large: {depot=}, {n_stops=}")

    start_locations = n_vehicles * [0]
    end_locations = n_vehicles * [0]
    index_manager = RoutingIndexManager(n_stops, n_vehicles, start_locations, end_locations)
    routing_model = RoutingModel(index_manager)

    callback_index_cost = routing_model.RegisterTransitCallback(callback=arc_cost_evaluator)
    routing_model.SetArcCostEvaluatorOfAllVehicles(callback_index_cost)

    return Model(routing_model=routing_model, index_manager=index_manager)


if __name__ == '__main__':
    
    routing_model = RoutingModel()

    print(routing_model.TYPE_ADDED_TO_VEHICLE)
    print(routing_model.TYPE_ON_VEHICLE_UP_TO_VISIT)
    print(routing_model.TYPE_SIMULTANEOUSLY_ADDED_AND_REMOVED)
    print(routing_model.ADDED_TYPE_REMOVED_FROM_VEHICLE)
    print(routing_model.AddHardTypeIncompatibility(type1=1, type2=1))
    print(routing_model.AddRequiredTypeAlternativesWhenAddingType(dependent_type=1, required_type_alternatives=None))
    print(routing_model.AddRequiredTypeAlternativesWhenRemovingType(dependent_type=1, required_type_alternatives=None))
    print(routing_model.AddSameVehicleRequiredTypeAlternatives(dependent_type=1, required_type_alternatives=None))
    print(routing_model.AddTemporalTypeIncompatibility(type1=1, type2=1))
    print(routing_model.CloseVisitTypes())
    print(routing_model.GetHardTypeIncompatibilitiesOfType(type=1))
    print(routing_model.GetNumberOfVisitTypes())
    print(routing_model.GetRequiredTypeAlternativesWhenAddingType(type=1))
    print(routing_model.GetRequiredTypeAlternativesWhenRemovingType(type=1))
    print(routing_model.HasHardTypeIncompatibilities())
    print(routing_model.HasSameVehicleTypeRequirements())
    print(routing_model.HasTemporalTypeIncompatibilities())
    print(routing_model.HasTemporalTypeRequirements())
    print(routing_model.HasTypeRegulations())
    print(routing_model.SetVisitType(index=None, type=1, type_policy=None))
