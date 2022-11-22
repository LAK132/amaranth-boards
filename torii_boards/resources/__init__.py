# SPDX-License-Identifier: BSD-2-Clause

# TODO: Integrate resources into torii (torii.resources)

from .display    import *
from .interface  import *
from .memory     import *
from .user       import *
from .extensions import *

__all__ = (
	'Display7SegResource',
	'VGAResource',
	'UARTResource',
	'IrDAResource',
	'SPIResource',
	'I2CResource',
	'DirectUSBResource',
	'ULPIResource',
	'PS2Resource',
	'SPIFlashResources',
	'SDCardResources',
	'SRAMResource',
	'SDRAMResource',
	'NORFlashResources',
	'DDR3Resource',
	'LEDResources',
	'RGBLEDResource',
	'ButtonResources',
	'SwitchResources',
)
