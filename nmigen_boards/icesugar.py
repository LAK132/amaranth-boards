from torii_boards.icesugar import *
from torii_boards.icesugar import __all__


import warnings
warnings.warn("instead of nmigen_boards.icesugar, use amaranth_boards.icesugar",
              DeprecationWarning, stacklevel=2)
