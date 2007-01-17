# -*- python -*-
#
#       OpenAlea.Core.Library: OpenAlea Core Library module
#
#       Copyright or (C) or Copr. 2006 INRIA - CIRAD - INRA  
#
#       File author(s): Christophe Pradal <christophe.prada@cirad.fr>
#                       Samuel Dufour-Kowalski <samuel.dufour@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#


__doc__="""
Arithmetic nodes
"""

__license__= "Cecill-C"
__revision__=" $Id$ "



from openalea.core.core import Node
from openalea.core.interface import IFloat
from openalea.core.interface import IFileStr

class LinearModel(Node):
    """
    Ax + B model 
    Input 0 : x value
    Ouput 0 : Ax + B
    Parameters :
        A : linear coefficient
        B : intercept
    """

    def __init__(self):

        Node.__init__(self)

        self.add_input( name = "X", interface = IFloat, value = 0.)
        self.add_input( name = "A", interface = IFloat, value = 0.)
        self.add_input( name = "B", interface = IFloat, value = 0.)
            
        self.add_output( name = "Y", interface = None) 

        

    def __call__(self, inputs):
        """ inputs is the list of input values """

        # We prefer here to get the value by key
        x = self.get_input_by_key("X")
        a = self.get_input_by_key("A")
        b = self.get_input_by_key("B")

        y = a*x + b

        return ( y,  )


class InputFile(Node):
    """
    A file path
    Out :  the file path string
    """

    def __init__(self):

        Node.__init__(self)

        self.add_input( name = "Filename", interface = IFileStr, value = "")
        self.add_output( name = "Filename", interface = IFileStr)
            
        

    def __call__(self, inputs):
        """ inputs is the list of input values """

        return ( inputs(0),  )

