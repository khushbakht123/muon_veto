from __future__ import annotations

import numpy as np
from pygama.dsp.errors import DSPFatal

from numba import guvectorize
from scipy.signal import find_peaks

from pygama.dsp.utils import numba_defaults_kwargs as nb_kwargs

@guvectorize(

   ["void(float32[:], float32, float32)", "void(float32[:], float32, float64)"],
    "(n),()->()",
    **nb_kwargs,
)

def integral(wfs: np.ndarray, value: float, trig: float) -> None:

    index = find_peaks(wfs, height = 10)[0]
    integ = 0.0

   for i in index:
        integ += wfs[i]
