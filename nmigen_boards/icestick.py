from torii_boards.icestick import *
from torii_boards.icestick import __all__


import warnings
warnings.warn("instead of nmigen_boards.icestick, use amaranth_boards.icestick",
              DeprecationWarning, stacklevel=2)
