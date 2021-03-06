from . import _Inputs
import torch


class TimeseriesInputs(_Inputs):
    r"""Base Inputs class for Time Series.
    """
    def __init__(self):
        super(TimeseriesInputs, self).__init__()
        raise NotImplementedError("")
    
    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        return torch.Tensor
