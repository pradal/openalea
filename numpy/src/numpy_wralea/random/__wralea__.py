# -*- python -*-
# -*- coding: latin-1 -*-
#
#       operations : numpy package
#
#       Copyright 2006 - 2010 INRIA - CIRAD - INRA  
#
#       File author(s): Eric MOSCARDI <eric.moscardi@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
################################################################################


__doc__ = """ openalea.numpy.random """
__revision__ = " $Id: $ "

from openalea.core import Factory
from openalea.core.interface import *


__name__ = "openalea.numpy.random"

__version__ = '0.0.1'
__license__ = 'CECILL-C'
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'Numpy wrapping and utils module.'
__url__ = 'http://openalea.gforge.inria.fr'
__icon__ = 'icon.png'

__all__ = []
    

randn = Factory(name = "randn",
    description = "Return a sample (or samples) from the “standard normal” distribution.",
    category = "numpy",
    inputs = (dict(name='n', interface=IInt),),
    outputs = (dict(name='array', interface= ISequence),),
    nodemodule = "vnumpy",
    nodeclass = "randn",
    )

__all__.append("randn")

standard_normal = Factory(name = "standard_normal",
    description = "Returns samples from a Standard Normal distribution (mean=0, stdev=1).",
    category = "numpy",
    inputs = (dict(name='size', interface=ITuple),),
    outputs = (dict(name='array', interface= None),),
    nodemodule = "vnumpy",
    nodeclass = "wra_standard_normal",
    )

__all__.append("standard_normal")
