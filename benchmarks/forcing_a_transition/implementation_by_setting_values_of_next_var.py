

import logging

from routing_problems.forcing_a_transition.factory import Problem
from utilities.models import Model
from routing_problems.templates import ImplementationBase


log = logging.getLogger()


class Implementation(ImplementationBase):
    @staticmethod
    def apply(model: Model, problem: Problem):
        nx, ny = problem.transition
        ix = model.index_manager.NodeToIndex(nx)
        iy = model.index_manager.NodeToIndex(ny)

        model.routing_model.NextVar(ix).SetValues([ix, iy])
        log.debug(f"routing_model.NextVar({ix}).SetValues([{ix}, {iy}])")

    @staticmethod
    def short_name() -> str:
        return "next_var"



