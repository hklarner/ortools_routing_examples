

from benchmarks.forcing_a_transition.factory import Problem, solve
from benchmarks.forcing_a_transition.implementation_by_locks import Implementation as ImpLocks
from benchmarks.forcing_a_transition.implementation_by_member_ct import Implementation as ImpMem
from utilities.search_parameters import create_search_parameters


if __name__ == '__main__':

    search_params = create_search_parameters(time_limit_seconds=10)
    problem = Problem(n_vehicles=1, n_stops=10, transition=(4, 8), vehicle_stop_capacity=15)
    imp = ImpLocks()
    solution = solve(problem=problem, search_parameters=search_params, implementation=imp)

    print(problem)
    print(solution)
