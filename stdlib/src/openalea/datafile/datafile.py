from openalea.core import Node
from openalea.core.pkgmanager import PackageManager

class GetData(Node):
    """This node permits to find a shared data file located in a given Python package.
    The data file is searched among the data nodes of the PackageManager.
    
    This node can be used either interactively or by connecting input nodes.

    To use it interactively, double click on it and :
        #. select the package you are interested in (e.g. 'alinea.caribu.data'),
        #. set a glob pattern (e.g. '*' or '*.can') ; the filename list is then updated by itself,
        #. select the filename you are interested in.
    
    :return: the file path of the selected data file.

    This interactive browsing is useful for demonstration or simply to found and 
    identify data filenames.

    To use it non-interactively:
        #. set the package name by connecting a string node to the first connector,
        #. set the file name by connecting a string node to the third connector.

    """
    def __init__(self, package, glob):
        Node.__init__(self, package, glob)
        self._output = None

    def __call__(self, inputs):
        package, glob, filename = inputs
        if package and filename:
            pm = PackageManager()
            data_factories = pm.get_data(glob, package)
            nodes = [data_factory.instantiate() for data_factory in data_factories]
            for node in nodes:
                node.eval()
            node_names = [data_factory.name for data_factory in data_factories]
            file_paths = [node.get_output(0) for node in nodes]
            zipped_names_paths = dict(zip(node_names, file_paths))
            self._output = zipped_names_paths.get(filename)
            return (self._output,)
        else:
            return (self._output,)

