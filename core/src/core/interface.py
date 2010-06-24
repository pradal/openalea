# -*- python -*-
#
#       OpenAlea.Core
#
#       Copyright 2006-2009 INRIA - CIRAD - INRA
#
#       File author(s): Samuel Dufour-Kowalski <samuel.dufour@sophia.inria.fr>
#                       Christophe Pradal <christophe.prada@cirad.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
##############################################################################
"""This module defines Interface classes (I/O types)"""

__license__ = "Cecill-C"
__revision__ = " $Id$ "

from openalea.core.metaclass import make_metaclass
from openalea.core.singleton import Singleton
from openalea.core.observer import AbstractListener
import types

# Dictionary to map Interface with corresponding python type


class TypeInterfaceMap(dict):
    """
    Singleton class to map Interface with standard python type
    InterfaceWidgetMap inherits from dict class
    """

    __metaclass__ = Singleton

    def declare_interface(self, type, interface):
        """
        Declare an interface and its optional widget

        :param interface: IInterface class object

        :param type: Python type
        """

        if type and type not in self:
            self[type] = interface

            TypeNameInterfaceMap().declare_interface(str(interface), interface)

class TypeNameInterfaceMap(dict):
    """
    Singleton class to map Interface Name with interface type
    InterfaceWidgetMap inherits from dict class
    """

    __metaclass__ = Singleton

    def declare_interface(self, name, interface):
        """
        Declare an interface and its optional widget

        :param interface: IInterface class object

        :param type: Python type
        """

        if name and name not in self:
            self[name] = interface

class IInterfaceMetaClass(type):
    """
    IInterface Metaclass
    Allow to register corresponding python type
    """


    all = [] # all interfaces
    def __new__(cls, name, bases, dict):
        newCls = type.__new__(cls, name, bases, dict)
        return newCls

    def __init__(cls, name, bases, dic):
        super(IInterfaceMetaClass, cls).__init__(name, bases, dic)
        if( hasattr(cls, "__pytype__") ):
            TypeInterfaceMap().declare_interface(cls.__pytype__, cls)
        IInterfaceMetaClass.all.append(cls)

    def __repr__(cls):
        return cls.__name__

# Defaults interfaces


class IInterface(object):
    """ Abstract base class for all interfaces """
    __metaclass__ = IInterfaceMetaClass
    __pytype__ = None
    __color__  = None

    @classmethod
    def default(cls):
        return None

    def __init__(self, **kargs):
        """ Default init"""

        ## the desc should be used as  a dynamic description of IInterace
        ## default visualisation in widget is done with tooltip
        #self.desc = kargs.get('desc', None)
        ## the label should be used to describe the default static description
        ## default visualisation in widget is done with label
        #self.label = kargs.get('label', None)


class IStr(IInterface):
    """ String interface """

    __pytype__ = types.StringType
    __color__  = (0,125,0)

    @classmethod
    def default(cls):
        return str()


class IFileStr(IStr):
    """ File Path interface """
    __color__  = (0,125,100)

    def __init__(self, filter="All (*.*)", save=False, **kargs):
        IInterface.__init__(self, **kargs)
        self.filter = filter
        self.save = save

    def __repr__(self):
        if self.filter == "All (*.*)" and not self.save: # default values
            return 'IFileStr'
        else:
            return 'IFileStr(filter="%s", save=%s)' % \
                (self.filter, str(self.save))


class IDirStr(IStr):
    """ Directory Path interface """
    __color__  = (100,125,0)
    pass


class ITextStr(IStr):
    """ Long String interface """
    __color__  = (100,125,100)
    pass


class IFloat(IInterface):
    """ Float interface """

    __pytype__ = types.FloatType
    __color__  = (0,125,170)

    def __init__(self, min = -2.**24, max = 2.**24, step=1., **kargs):
        IInterface.__init__(self, **kargs)
        self.min = min
        self.max = max
        self.step = step

    @classmethod
    def default(cls):
        return 0.

    def __repr__(self):
        default_min = -2**24
        default_max = 2**24
        default_step = 1.
        if (self.min == default_min and
            self.max == default_max and
            self.step == default_step):
            return self.__class__.__name__
        else:
            return 'IFloat(min=%d, max=%d, step=%f)' % \
                (self.min, self.max, self.step)


class IInt(IInterface):
    """ Int interface """
    __pytype__ = types.IntType
    __color__  = (0,0,255)

    def __init__(self, min = -2**24, max = 2**24, step=1, **kargs):
        IInterface.__init__(self, **kargs)
        self.min = min
        self.max = max
        self.step = step

    @classmethod
    def default(cls):
        return 0

    def __repr__(self):
        default_min = -2**24
        default_max = 2**24
        default_step = 1
        if (self.min == default_min and
            self.max == default_max and
            self.step == default_step):
            return self.__class__.__name__
        else:
            return 'IInt(min=%d, max=%d, step=%d)' % \
                (self.min, self.max, self.step)


class IBool(IInterface):
    """ Bool interface """

    __pytype__ = types.BooleanType
    __color__  = (100,0,255)    

    @classmethod
    def default(cls):
        return False


class IEnumStr(IStr):
    """ String enumeration """
    __color__  = (100,125,255) 

    def __init__(self, enum = [], **kargs):
        IInterface.__init__(self, **kargs)
        self.enum = enum

    def __repr__(self):
        return 'IEnumStr(enum=%s)' % (str(self.enum))


class IRGBColor(IInterface):
    """ RGB Color """
    __color__  = (0,255,0) 
    pass


class IDateTime(IInterface):
    """ DateTime """
    __color__  = (175,100,50) 
    pass


class ITuple3(IInterface):
    """ Tuple3 """
    __color__  = (175,175,175) 
    
    @classmethod
    def default(cls):
        return (None, None, None)


class IFunction(IInterface):
    """ Function interface """
    __color__  = (175,255,255) 
    __pytype__ = types.FunctionType


class ISequence(IInterface):
    """ Sequence interface (list, tuple, ...) """
    __pytype__ = types.ListType
    __color__  = (175,100,0) 

    @classmethod
    def default(cls):
        return list()


class IDict(IInterface):
    """ Dictionary interface """
    __pytype__ = types.DictType
    __color__  = (175,120,0) 

    @classmethod
    def default(cls):
        """todo"""
        return dict()


class IData(IStr):
    """ Package data interface """
    pass

# Dictionary to map Interface with corresponding widget


class InterfaceWidgetMap(dict):
    """
    Singleton class to map Interface with InterfaceWidget
    InterfaceWidgetMap inherits from dict class
    """

    __metaclass__ = Singleton

    def __init__(self, *args):
        dict.__init__(self, *args)

    def declare_interface(self, interface, widget=None):
        """
        Declare an interface and its optional widget
        @param interface : IInterface class object
        @param widget : IInterfaceWidget class object
        """

        self[interface] = widget


# Base class for interface widget


class IWidgetMetaClass(type):
    """ InterfaceWidget Metaclass """

    def __init__(cls, name, bases, dic, **kargs):
        super(IWidgetMetaClass, cls).__init__(name, bases, dic)
        if(cls.__interface__):
            InterfaceWidgetMap().declare_interface(cls.__interface__, cls)


class IInterfaceWidget(AbstractListener):
    """ Base class for widget associated to an interface """

    __metaclass__ = IWidgetMetaClass
    __interface__ = None

    def __init__(self, node, parent, parameter_str, interface):
        """
        @param parameter_str : the parameter key the widget is associated to
        @param interface : instance of interface object
        """
        AbstractListener.__init__(self)
        self.node = node
        self.param_str = parameter_str

    def update_state(self):
        """ Enable or disable widget depending of connection status """

        #i = self.node.get_input_index(self.param_str)
        state = self.node.get_input_state(self.param_str)

        # By default, disable the entire widget
        try:
            notconnected = bool(state != "connected")
            if(self.node.internal_data.get('minimal', False)):
                self.setVisible(notconnected)
            else:
                self.setEnabled(notconnected)
        except:
            pass

    def notify(self, sender, event):
        """ Notification sent by node """
        pass

