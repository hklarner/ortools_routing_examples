

from utilities.models import Model
from utilities.callbacks import constant_k


def add_stop_count_dimension(model: Model, capacity: int):
    callback = constant_k(k=1)
    callback_index_count = model.routing_model.RegisterTransitCallback(callback=callback)
    model.routing_model.AddDimension(
        evaluator_index=callback_index_count,
        slack_max=0,
        capacity=capacity,
        fix_start_cumul_to_zero=True,
        name="stop_count_dimension")
