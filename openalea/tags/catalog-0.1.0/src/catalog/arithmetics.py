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



from openalea.core import *


        

class Add(Node):
    """ Generic Addition
    Input 0 : First value to add
    Input 1 : Second value to add
    Output 0 : In0 + In1
    """

    def __init__(self):

        Node.__init__(self)

        # defines I/O
        self.add_input( name = "In 0", interface = None, value = 0.)
        self.add_input( name = "In 1", interface = None, value = 0.)
            
        self.add_output( name = "Out", interface = None) 


    def __call__(self, inputs):
        """ inputs is the list of input values """

        return ( inputs[0] + inputs[1], )
        

class Sub(Node):
    """ Generic Soustraction
    Output 0 : Input 0 - Input 1
    """

    def __init__(self):

        Node.__init__(self)

        # defines I/O
        self.add_input( name = "In 0", interface = None, value = 0.)
        self.add_input( name = "In 1", interface = None, value = 0.)
            
        self.add_output( name = "Out", interface = None) 


    def __call__(self, inputs):
        """ inputs is the list of input values """

        return ( inputs[0]- inputs[1], )


class Mult(Node):
    """ Generic Multiplication
    Output 0 : Input 0 * Input 1
    """

    def __init__(self):

        Node.__init__(self)

        # defines I/O
        self.add_input( name = "In 0", interface = None, value = 1.)
        self.add_input( name = "In 1", interface = None, value = 1.)
            
        self.add_output( name = "Out", interface = None) 


    def __call__(self, inputs):
        """ inputs is the list of input values """

        return ( inputs[0] * inputs[1], )


class Div(Node):
    """ Generic Division
    Output 0 : Input 0 / Input 1
    """

    def __init__(self):

        Node.__init__(self)

        # defines I/O
        self.add_input( name = "In 0", interface = None, value = 1.)
        self.add_input( name = "In 1", interface = None, value = 1.)
            
        self.add_output( name = "Out", interface = None) 


    def __call__(self, inputs):
        """ inputs is the list of input values """

        return ( inputs[0] / inputs[1], )


class Abs( Node ):
    __doc__= abs.__doc__

    def __init__(self):

        Node.__init__(self)

        self.add_input ( name = "object", interface = None, value=0 ) 
        self.add_output( name = "abs", interface = None ) 

    def __call__(self, inputs):
        obj = self.get_input_by_key("object")

        f = None
        if callable(obj):
            f = lambda x: abs(obj(x))
        else:
            f = abs(obj)
        return ( f, )


class Cmp( Node ):
    __doc__= cmp.__doc__

    def __init__(self):

        Node.__init__(self)

        self.add_input ( name = "x", interface = None, value=0 )
        self.add_input ( name = "y", interface = None, value=0 ) 
        self.add_output( name = "cmp", interface = None ) 

    def __call__(self, inputs):
        
        x = self.get_input_by_key("x")
        y = self.get_input_by_key("y")
        
        f = cmp(x,y)
        return ( f, )


class Pow( Node ):
    __doc__= pow.__doc__

    def __init__(self):

        Node.__init__(self)

        self.add_input ( name = "x", interface = None, value=0 )
        self.add_input ( name = "y", interface = None, value=0 ) 
        self.add_output( name = "pow", interface = None ) 

    def __call__(self, inputs):
        
        x = self.get_input_by_key("x")
        y = self.get_input_by_key("y")
        
        f = pow(x,y)
        return ( f, )


class Round( Node ):
    __doc__= round.__doc__

    def __init__(self):

        Node.__init__(self)

        self.add_input ( name = "x", interface = None, value=0 )
        self.add_input ( name = "n", interface = IInt, value=1 ) 
        self.add_output( name = "round", interface = None ) 

    def __call__(self, inputs):
        
        x = self.get_input_by_key("x")
        n = self.get_input_by_key("n")
        
        f = round(x,n)
        return ( f, )


class Min( Node ):
    __doc__= min.__doc__

    def __init__(self):

        Node.__init__(self)

        self.add_input ( name = "s", interface = ISequence, value=[] )
        self.add_output( name = "min", interface = None ) 

    def __call__(self, inputs):
        
        s = self.get_input_by_key("s")
        
        f = min(s)
        return ( f, )


class Max( Node ):
    __doc__= max.__doc__

    def __init__(self):

        Node.__init__(self)

        self.add_input ( name = "s", interface = ISequence, value=[] )
        self.add_output( name = "max", interface = None ) 

    def __call__(self, inputs):
        
        s = self.get_input_by_key("s")
        
        f = max(s)
        return ( f, )
