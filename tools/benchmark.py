

import logging
import time

import pandas as pd

from routing_problems.forcing_a_transition import factory
from routing_problems.forcing_a_transition import implementation_by_setting_values_of_next_var
from routing_problems.forcing_a_transition import implementation_by_member_ct
from utilities.search_parameters import create_search_parameters
from utilities.solution import ReturnCodes
from utilities.files import path_relative_to_file as path

log = logging.getLogger()


def run() -> pd.DataFrame:
    implementations = [implementation_by_member_ct.Implementation, implementation_by_setting_values_of_next_var.Implementation]
    search_parameters = create_search_parameters(time_limit_seconds=1)

    data = []

    for problem in factory.generator(seed=1):
        for imp in list(implementations):

            start = time.time()
            solution = factory.solve(problem=problem, search_parameters=search_parameters, implementation=imp())
            end = time.time()
            time_ms = round(1000 * (end - start))

            if solution.return_code == ReturnCodes.ROUTING_FAIL_TIMEOUT:
                implementations.remove(imp)
                log.debug(f"time out: removed {imp}")

            data.append(dict(
                n_vehicles=problem.n_vehicles,
                n_stops=problem.n_stops,
                implementation=imp.short_name(),
                return_code=solution.return_code,
                time_ms=time_ms
            ))

    return pd.DataFrame(data=data)


if __name__ == '__main__':

    df = run()
    plot = df.plot.scatter(x="n_stops", y="time_ms", c="n_vehicles", colormap="viridis")
    plot.get_figure().savefig(path("../benchmark.pdf"), format="pdf")
    df.to_csv(path("../benchmark.csv"), index=False, header=True)


