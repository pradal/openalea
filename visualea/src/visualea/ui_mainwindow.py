# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Jul 22 11:19:15 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,847,593).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/icons/openalea_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setObjectName("vboxlayout")

        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")

        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")

        self.tabPackager = QtGui.QTabWidget(self.splitter_2)
        self.tabPackager.setObjectName("tabPackager")

        self.packageview = QtGui.QWidget()
        self.packageview.setObjectName("packageview")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.packageview)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setMargin(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.tabPackager.addTab(self.packageview,QtGui.QIcon(":/icons/package.png"),"")

        self.categoryview = QtGui.QWidget()
        self.categoryview.setObjectName("categoryview")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.categoryview)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setMargin(6)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.tabPackager.addTab(self.categoryview,QtGui.QIcon(":/icons/category.png"),"")

        self.searchview = QtGui.QWidget()
        self.searchview.setObjectName("searchview")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.searchview)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setMargin(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.search_lineEdit = QtGui.QLineEdit(self.searchview)
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.vboxlayout3.addWidget(self.search_lineEdit)
        self.tabPackager.addTab(self.searchview,QtGui.QIcon(":/icons/search.png"),"")

        self.poolTabWidget = QtGui.QTabWidget(self.splitter_2)
        self.poolTabWidget.setObjectName("poolTabWidget")

        self.pooltab = QtGui.QWidget()
        self.pooltab.setObjectName("pooltab")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.pooltab)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setMargin(6)
        self.vboxlayout4.setObjectName("vboxlayout4")
        self.poolTabWidget.addTab(self.pooltab,QtGui.QIcon(":/icons/datapool.png"),"")

        self.sensortab = QtGui.QWidget()
        self.sensortab.setObjectName("sensortab")
        self.poolTabWidget.addTab(self.sensortab,QtGui.QIcon(":/icons/info.png"),"")

        self.UseTabWidget = QtGui.QWidget()
        self.UseTabWidget.setObjectName("UseTabWidget")

        self.vboxlayout5 = QtGui.QVBoxLayout(self.UseTabWidget)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setMargin(6)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.useTable = QtGui.QTableWidget(self.UseTabWidget)
        self.useTable.setObjectName("useTable")
        self.vboxlayout5.addWidget(self.useTable)
        self.poolTabWidget.addTab(self.UseTabWidget,"")

        self.splitter = QtGui.QSplitter(self.splitter_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")

        self.tabWorkspace = QtGui.QTabWidget(self.splitter)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.tabWorkspace.sizePolicy().hasHeightForWidth())
        self.tabWorkspace.setSizePolicy(sizePolicy)
        self.tabWorkspace.setObjectName("tabWorkspace")

        self.usetab = QtGui.QWidget()
        self.usetab.setObjectName("usetab")

        self.vboxlayout6 = QtGui.QVBoxLayout(self.usetab)
        self.vboxlayout6.setSpacing(6)
        self.vboxlayout6.setMargin(6)
        self.vboxlayout6.setObjectName("vboxlayout6")
        self.tabWorkspace.addTab(self.usetab,"")
        self.vboxlayout.addWidget(self.splitter_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,847,26))
        self.menubar.setObjectName("menubar")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_Export = QtGui.QMenu(self.menu_File)
        self.menu_Export.setObjectName("menu_Export")

        self.menuDataPool = QtGui.QMenu(self.menubar)
        self.menuDataPool.setObjectName("menuDataPool")

        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")

        self.menu_Python = QtGui.QMenu(self.menubar)
        self.menu_Python.setObjectName("menu_Python")

        self.menu_Workspace = QtGui.QMenu(self.menubar)
        self.menu_Workspace.setObjectName("menu_Workspace")

        self.menu_Package = QtGui.QMenu(self.menubar)
        self.menu_Package.setObjectName("menu_Package")

        self.menuCreate = QtGui.QMenu(self.menu_Package)
        self.menuCreate.setObjectName("menuCreate")

        self.menu_Window = QtGui.QMenu(self.menubar)
        self.menu_Window.setObjectName("menu_Window")
        MainWindow.setMenuBar(self.menubar)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")

        self.action_Help = QtGui.QAction(MainWindow)
        self.action_Help.setObjectName("action_Help")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_New_Package = QtGui.QAction(MainWindow)
        self.action_New_Package.setObjectName("action_New_Package")

        self.actionSystem_Search = QtGui.QAction(MainWindow)
        self.actionSystem_Search.setObjectName("actionSystem_Search")

        self.action_Add_File = QtGui.QAction(MainWindow)
        self.action_Add_File.setObjectName("action_Add_File")

        self.action_Auto_Search = QtGui.QAction(MainWindow)
        self.action_Auto_Search.setObjectName("action_Auto_Search")

        self.action_Close_current_workspace = QtGui.QAction(MainWindow)
        self.action_Close_current_workspace.setObjectName("action_Close_current_workspace")

        self.action_Run = QtGui.QAction(MainWindow)
        self.action_Run.setObjectName("action_Run")

        self.action_New_Network = QtGui.QAction(MainWindow)
        self.action_New_Network.setObjectName("action_New_Network")

        self.actionOpenAlea_Web = QtGui.QAction(MainWindow)
        self.actionOpenAlea_Web.setObjectName("actionOpenAlea_Web")

        self.action_Execute_script = QtGui.QAction(MainWindow)
        self.action_Execute_script.setObjectName("action_Execute_script")

        self.action_New_Session = QtGui.QAction(MainWindow)
        self.action_New_Session.setObjectName("action_New_Session")

        self.action_Open_Session = QtGui.QAction(MainWindow)
        self.action_Open_Session.setObjectName("action_Open_Session")

        self.action_Save_Session = QtGui.QAction(MainWindow)
        self.action_Save_Session.setObjectName("action_Save_Session")

        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")

        self.action_Export_to_Factory = QtGui.QAction(MainWindow)
        self.action_Export_to_Factory.setObjectName("action_Export_to_Factory")

        self.actionExport_to_Application = QtGui.QAction(MainWindow)
        self.actionExport_to_Application.setObjectName("actionExport_to_Application")

        self.actionClear_Data_Pool = QtGui.QAction(MainWindow)
        self.actionClear_Data_Pool.setObjectName("actionClear_Data_Pool")

        self.actionFind_Node = QtGui.QAction(MainWindow)
        self.actionFind_Node.setObjectName("actionFind_Node")

        self.actionNew_Python_Node = QtGui.QAction(MainWindow)
        self.actionNew_Python_Node.setObjectName("actionNew_Python_Node")

        self.actionNew_Package = QtGui.QAction(MainWindow)
        self.actionNew_Package.setObjectName("actionNew_Package")

        self.action_EditNode = QtGui.QAction(MainWindow)
        self.action_EditNode.setObjectName("action_EditNode")

        self.actionShow_Pool = QtGui.QAction(MainWindow)
        self.actionShow_Pool.setObjectName("actionShow_Pool")

        self.action_OpenNode = QtGui.QAction(MainWindow)
        self.action_OpenNode.setObjectName("action_OpenNode")

        self.action_Delete_2 = QtGui.QAction(MainWindow)
        self.action_Delete_2.setObjectName("action_Delete_2")

        self.action_New_Empty_Workspace = QtGui.QAction(MainWindow)
        self.action_New_Empty_Workspace.setObjectName("action_New_Empty_Workspace")

        self.actionReload_from_Model = QtGui.QAction(MainWindow)
        self.actionReload_from_Model.setObjectName("actionReload_from_Model")

        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")

        self.actionConfigure_I_O = QtGui.QAction(MainWindow)
        self.actionConfigure_I_O.setObjectName("actionConfigure_I_O")

        self.actionGroup_Selection = QtGui.QAction(MainWindow)
        self.actionGroup_Selection.setObjectName("actionGroup_Selection")

        self.actionOpen_Console = QtGui.QAction(MainWindow)
        self.actionOpen_Console.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionOpen_Console.setObjectName("actionOpen_Console")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setObjectName("action_Paste")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setObjectName("action_Cut")

        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")

        self.actionPreview_Application = QtGui.QAction(MainWindow)
        self.actionPreview_Application.setObjectName("actionPreview_Application")

        self.actionLeft_Panel = QtGui.QAction(MainWindow)
        self.actionLeft_Panel.setObjectName("actionLeft_Panel")

        self.actionWorkspaces = QtGui.QAction(MainWindow)
        self.actionWorkspaces.setObjectName("actionWorkspaces")

        self.actionDisplay_Package_Manager = QtGui.QAction(MainWindow)
        self.actionDisplay_Package_Manager.setCheckable(True)
        self.actionDisplay_Package_Manager.setChecked(True)
        self.actionDisplay_Package_Manager.setObjectName("actionDisplay_Package_Manager")

        self.actionDisplay_Workspaces = QtGui.QAction(MainWindow)
        self.actionDisplay_Workspaces.setCheckable(True)
        self.actionDisplay_Workspaces.setChecked(True)
        self.actionDisplay_Workspaces.setObjectName("actionDisplay_Workspaces")

        self.actionInvalidate = QtGui.QAction(MainWindow)
        self.actionInvalidate.setObjectName("actionInvalidate")

        self.actionClea_r_Console = QtGui.QAction(MainWindow)
        self.actionClea_r_Console.setObjectName("actionClea_r_Console")

        self.action_Image = QtGui.QAction(MainWindow)
        self.action_Image.setObjectName("action_Image")

        self.action_Application = QtGui.QAction(MainWindow)
        self.action_Application.setObjectName("action_Application")

        self.action_Data_File = QtGui.QAction(MainWindow)
        self.action_Data_File.setObjectName("action_Data_File")
        self.menu_Export.addAction(self.action_Image)
        self.menu_Export.addAction(self.action_Application)
        self.menu_File.addAction(self.action_New_Session)
        self.menu_File.addAction(self.action_Open_Session)
        self.menu_File.addAction(self.action_Save_Session)
        self.menu_File.addAction(self.actionSave_as)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.menu_Export.menuAction())
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menuDataPool.addAction(self.actionClear_Data_Pool)
        self.menu_Help.addAction(self.action_Help)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_About)
        self.menu_Help.addAction(self.actionOpenAlea_Web)
        self.menu_Python.addAction(self.action_Execute_script)
        self.menu_Python.addAction(self.actionOpen_Console)
        self.menu_Python.addAction(self.actionClea_r_Console)
        self.menu_Workspace.addAction(self.action_Run)
        self.menu_Workspace.addAction(self.actionInvalidate)
        self.menu_Workspace.addAction(self.actionReset)
        self.menu_Workspace.addAction(self.actionConfigure_I_O)
        self.menu_Workspace.addSeparator()
        self.menu_Workspace.addAction(self.actionGroup_Selection)
        self.menu_Workspace.addAction(self.action_Copy)
        self.menu_Workspace.addAction(self.action_Paste)
        self.menu_Workspace.addAction(self.action_Cut)
        self.menu_Workspace.addAction(self.action_Delete_2)
        self.menu_Workspace.addSeparator()
        self.menu_Workspace.addAction(self.action_New_Empty_Workspace)
        self.menu_Workspace.addAction(self.action_Close_current_workspace)
        self.menu_Workspace.addSeparator()
        self.menu_Workspace.addAction(self.action_Export_to_Factory)
        self.menu_Workspace.addAction(self.actionReload_from_Model)
        self.menu_Workspace.addSeparator()
        self.menu_Workspace.addAction(self.actionExport_to_Application)
        self.menu_Workspace.addAction(self.actionPreview_Application)
        self.menuCreate.addAction(self.actionNew_Package)
        self.menuCreate.addAction(self.action_New_Network)
        self.menuCreate.addAction(self.actionNew_Python_Node)
        self.menuCreate.addAction(self.action_Data_File)
        self.menu_Package.addAction(self.action_Add_File)
        self.menu_Package.addAction(self.action_Auto_Search)
        self.menu_Package.addAction(self.actionFind_Node)
        self.menu_Package.addSeparator()
        self.menu_Package.addAction(self.menuCreate.menuAction())
        self.menu_Window.addAction(self.actionDisplay_Package_Manager)
        self.menu_Window.addAction(self.actionDisplay_Workspaces)
        self.menu_Window.addSeparator()
        self.menu_Window.addAction(self.actionPreferences)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Package.menuAction())
        self.menubar.addAction(self.menuDataPool.menuAction())
        self.menubar.addAction(self.menu_Workspace.menuAction())
        self.menubar.addAction(self.menu_Python.menuAction())
        self.menubar.addAction(self.menu_Window.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabPackager.setCurrentIndex(0)
        self.poolTabWidget.setCurrentIndex(0)
        self.tabWorkspace.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "VisuAlea", None, QtGui.QApplication.UnicodeUTF8))
        self.tabPackager.setTabText(self.tabPackager.indexOf(self.packageview), QtGui.QApplication.translate("MainWindow", "Package", None, QtGui.QApplication.UnicodeUTF8))
        self.tabPackager.setTabText(self.tabPackager.indexOf(self.categoryview), QtGui.QApplication.translate("MainWindow", "Category", None, QtGui.QApplication.UnicodeUTF8))
        self.tabPackager.setTabText(self.tabPackager.indexOf(self.searchview), QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.poolTabWidget.setTabText(self.poolTabWidget.indexOf(self.pooltab), QtGui.QApplication.translate("MainWindow", "DataPool", None, QtGui.QApplication.UnicodeUTF8))
        self.poolTabWidget.setTabText(self.poolTabWidget.indexOf(self.sensortab), QtGui.QApplication.translate("MainWindow", "Sensors", None, QtGui.QApplication.UnicodeUTF8))
        self.useTable.clear()
        self.useTable.setColumnCount(2)
        self.useTable.setRowCount(0)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("MainWindow", "Variable", None, QtGui.QApplication.UnicodeUTF8))
        self.useTable.setHorizontalHeaderItem(0,headerItem)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("MainWindow", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.useTable.setHorizontalHeaderItem(1,headerItem1)
        self.poolTabWidget.setTabText(self.poolTabWidget.indexOf(self.UseTabWidget), QtGui.QApplication.translate("MainWindow", "Use", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWorkspace.setTabText(self.tabWorkspace.indexOf(self.usetab), QtGui.QApplication.translate("MainWindow", "Root", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Export.setTitle(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDataPool.setTitle(QtGui.QApplication.translate("MainWindow", "&DataPool", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Python.setTitle(QtGui.QApplication.translate("MainWindow", "P&ython", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Workspace.setTitle(QtGui.QApplication.translate("MainWindow", "&Workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Package.setTitle(QtGui.QApplication.translate("MainWindow", "&Package Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCreate.setTitle(QtGui.QApplication.translate("MainWindow", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Window.setTitle(QtGui.QApplication.translate("MainWindow", "&Window", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Help.setText(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Help.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Package.setText(QtGui.QApplication.translate("MainWindow", "&Create Package", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Package.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSystem_Search.setText(QtGui.QApplication.translate("MainWindow", "System &Search", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_File.setText(QtGui.QApplication.translate("MainWindow", "&Load Package/Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Auto_Search.setText(QtGui.QApplication.translate("MainWindow", "&Reload All packages", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Close_current_workspace.setText(QtGui.QApplication.translate("MainWindow", "&Close Workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Run.setText(QtGui.QApplication.translate("MainWindow", "&Run ", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Run.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Network.setText(QtGui.QApplication.translate("MainWindow", "&Composite Node", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenAlea_Web.setText(QtGui.QApplication.translate("MainWindow", "OpenAlea Web", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Execute_script.setText(QtGui.QApplication.translate("MainWindow", "&Execute script", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Session.setText(QtGui.QApplication.translate("MainWindow", "&New Session", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Session.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open_Session.setText(QtGui.QApplication.translate("MainWindow", "&Open Session", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open_Session.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save_Session.setText(QtGui.QApplication.translate("MainWindow", "&Save Session", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save_Session.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save &as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export_to_Factory.setText(QtGui.QApplication.translate("MainWindow", "&Save as Composite Node", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export_to_Factory.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_to_Application.setText(QtGui.QApplication.translate("MainWindow", "Export to Application", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_Data_Pool.setText(QtGui.QApplication.translate("MainWindow", "Clear Data Pool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Node.setText(QtGui.QApplication.translate("MainWindow", "&Find Node", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Node.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Python_Node.setText(QtGui.QApplication.translate("MainWindow", "Python &Node", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Package.setText(QtGui.QApplication.translate("MainWindow", "&Package", None, QtGui.QApplication.UnicodeUTF8))
        self.action_EditNode.setText(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Pool.setText(QtGui.QApplication.translate("MainWindow", "Show Pool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Pool.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OpenNode.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Delete_2.setText(QtGui.QApplication.translate("MainWindow", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Empty_Workspace.setText(QtGui.QApplication.translate("MainWindow", "&New Empty Workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Empty_Workspace.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReload_from_Model.setText(QtGui.QApplication.translate("MainWindow", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReload_from_Model.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigure_I_O.setText(QtGui.QApplication.translate("MainWindow", "Configure I/O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGroup_Selection.setText(QtGui.QApplication.translate("MainWindow", "Group", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGroup_Selection.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+G", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Console.setText(QtGui.QApplication.translate("MainWindow", "Open &shell", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Console.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReset.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+K", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreview_Application.setText(QtGui.QApplication.translate("MainWindow", "Preview Application", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLeft_Panel.setText(QtGui.QApplication.translate("MainWindow", "Package Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspaces.setText(QtGui.QApplication.translate("MainWindow", "Workspaces", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisplay_Package_Manager.setText(QtGui.QApplication.translate("MainWindow", "Display Package Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisplay_Workspaces.setText(QtGui.QApplication.translate("MainWindow", "Display Workspaces", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInvalidate.setText(QtGui.QApplication.translate("MainWindow", "Invalidate", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInvalidate.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClea_r_Console.setText(QtGui.QApplication.translate("MainWindow", "&Clear shell", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Image.setText(QtGui.QApplication.translate("MainWindow", "&Image", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Application.setText(QtGui.QApplication.translate("MainWindow", "&Application", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Data_File.setText(QtGui.QApplication.translate("MainWindow", "&Data File", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
