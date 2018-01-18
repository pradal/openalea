from streamredirection import GraphicalStreamRedirection


from qtconsole.rich_jupyter_widget import RichJupyterWidget as RichIPythonWidget
from qtconsole.inprocess import QtInProcessKernelManager


class ShellWidget(RichIPythonWidget, GraphicalStreamRedirection):

    """
    ShellWidget is an IPython shell.
    """

    def __init__(self, interpreter=None, message="", log='', parent=None):
        """
        :param interpreter : InteractiveInterpreter in which
        the code will be executed

        :param message: welcome message string

        :param  parent: specifies the parent widget.
        If no parent widget has been specified, it is possible to
        exit the interpreter by Ctrl-D.
        """
        RichIPythonWidget.__init__(self, parent)

        self.kernel_manager = QtInProcessKernelManager()

        # Write welcome message
        #self.write(message)

        self.kernel_manager.start_kernel(show_banner=False)


        self.kernel = self.kernel_manager.kernel
        self.kernel.gui = 'qt4'
        self.shell = self.kernel.shell

        self.kernel_client = self.kernel_manager.client()
        self.kernel_client.start_channels()

        self.kernel.locals = self.kernel.shell.user_ns

        # Set interpreter
        self.interpreter = self.kernel
        self.interpreter.widget = self

        # Multiple Stream Redirection
        GraphicalStreamRedirection.__init__(self, self.kernel.stdout, self.kernel.stderr)

        #######################################################



        # Compatibility with visualea
        self.runsource = self.interpreter.shell.run_cell
        self.runcode = self.interpreter.shell.run_code
        # run_cell_magic?
        #self.loadcode = self.interpreter.load_code


    def read(self, *args, **kwargs):
        self.kernel_client.stdin_channel.input(*args, **kwargs)

    def readline(self, size=None):
        from openalea.oalab.utils import raw_input_dialog
        txt = raw_input_dialog()
        self.write(txt)
        return txt

    def get_interpreter(self):
        """
        :return: the interpreter object
        """
        return self

    def write(self, txt):
        """
        Write a text in the stdout of the shell and flush it.
        :param txt: String to write.
        """
        self.interpreter.shell.write(str(txt))
        self.interpreter.stdout.flush()

    def push(self, var):
        """
        Push variables in the namespace.
        :param var: dict of objects
        """
        if var is not None:
            for v in var:
                print v
                self.interpreter.locals += v

    def initialize(self):
        return
        if not hasattr(self.interpreter, "shell"):
            self.interpreter.shell = self.interpreter
        if hasattr(self.interpreter.shell, "events"):
            self.interpreter.shell.events.register("post_execute", self.add_to_history)
        else:
            print("You need ipython >= 2.0 to use history.")

    def add_to_history(self, *args, **kwargs):
        """
        Send the last sent of history to the components that display history
        """
        from openalea.oalab.service.history import display_history
        records = self.interpreter.shell.history_manager.get_range()

        input_ = ''
        # loop all elements in iterator to get last one.
        # TODO: search method returning directly last input
        for session, line, input_ in records:
            pass
        display_history(input_)


def main():
    from openalea.vpltk.qt import QtGui
    import sys

    app = QtGui.QApplication(sys.argv)

    # Set Shell Widget
    shellwdgt = ShellWidget()
    shellwdgt.kernel.locals['kernel']=shellwdgt.kernel

    mainWindow = QtGui.QMainWindow()
    mainWindow.setCentralWidget(shellwdgt)
    mainWindow.show()

    app.exec_()


if(__name__ == "__main__"):
    main()
