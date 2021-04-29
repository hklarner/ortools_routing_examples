

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

        ct = model.routing_model.solver().MemberCt(model.routing_model.NextVar(ix), [ix, iy])
        model.routing_model.solver().Add(ct)

        log.debug(f"MemberCt(routing_model.NextVar({ix}), {[ix, iy]})")

    @staticmethod
    def short_name() -> str:
        return "member_ct"

