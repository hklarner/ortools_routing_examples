

import logging

from benchmarks.forcing_a_transition.factory import Problem
from utilities.models import Model
from benchmarks.templates import ImplementationBase

log = logging.getLogger()


class Implementation(ImplementationBase):
    @staticmethod
    def apply(model: Model, problem: Problem):
        nx, ny = problem.transition
        ix = model.index_manager.NodeToIndex(nx)
        iy = model.index_manager.NodeToIndex(ny)

        model.routing_model.ApplyLocks(locks=(ix, iy))
        print(model.routing_model.PreAssignment())
        log.debug(f"model.routing_model.ApplyLocks(locks=({ix}, {iy}))")

    @staticmethod
    def short_name() -> str:
        return "locks"

