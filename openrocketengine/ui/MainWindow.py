from openrocketengine.core.rocket import Engine
from openrocketengine.core.interface import standard_types, read_config
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import platform
if platform.system() == 'Linux':
    import os.path

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()
        self.filename = ""
        self.config = {}

    def setupUi(self):
        self.setWindowTitle("Open Rocket Engine")
        self.resize(800, 600)
        self.centralwidget = QWidget(self)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.runButton = QPushButton(self.centralwidget)
        self.runButton.setText("Run")
        self.runButton.setMinimumSize(QSize(50, 50))
        self.runButton.setMaximumSize(QSize(50, 50))
        self.runButton.setStyleSheet("")
        self.runButton.clicked.connect(self.run)
        self.horizontalLayout.addWidget(self.runButton)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tab = QWidget()
        self.gridLayout = QGridLayout(self.tab)
        self.label_16 = QLabel(self.tab)
        self.label_16.setText(":1")
        self.gridLayout.addWidget(self.label_16, 5, 2, 1, 1)
        self.label_8 = QLabel(self.tab)
        self.label_8.setText("Molecular Weight")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_15 = QLabel(self.tab)
        self.label_15.setText("Pascals")
        self.gridLayout.addWidget(self.label_15, 4, 2, 1, 1)
        self.label_13 = QLabel(self.tab)
        self.label_13.setText("Pascals")
        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)
        self.label_3 = QLabel(self.tab)
        self.label_3.setText("Thrust")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.area_ratio = QDoubleSpinBox(self.tab)
        self.area_ratio.setMaximum(1000000000.0)
        self.gridLayout.addWidget(self.area_ratio, 9, 1, 1, 1)
        self.thrust = QSpinBox(self.tab)
        self.thrust.setMaximum(1000000000)
        self.gridLayout.addWidget(self.thrust, 1, 1, 1, 1)
        self.label_11 = QLabel(self.tab)
        self.label_11.setText("Area Ratio")
        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)
        self.pe = QSpinBox(self.tab)
        self.pe.setMaximum(1000000000)
        self.gridLayout.addWidget(self.pe, 4, 1, 1, 1)
        self.label_12 = QLabel(self.tab)
        self.label_12.setText("N")
        self.gridLayout.addWidget(self.label_12, 1, 2, 1, 1)
        self.gamma = QDoubleSpinBox(self.tab)
        self.gamma.setMaximum(1000000000.0)
        self.gridLayout.addWidget(self.gamma, 7, 1, 1, 1)
        self.label_14 = QLabel(self.tab)
        self.label_14.setText("Pascals")
        self.gridLayout.addWidget(self.label_14, 3, 2, 1, 1)
        self.label_20 = QLabel(self.tab)
        self.label_20.setText(":1")
        self.gridLayout.addWidget(self.label_20, 9, 2, 1, 1)
        spacerItem1 = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 3, 1, 1)
        self.label_6 = QLabel(self.tab)
        self.label_6.setText("Exit Press")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_10 = QLabel(self.tab)
        self.label_10.setText("L*")
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 10, 1, 1, 1)
        self.pc = QSpinBox(self.tab)
        self.pc.setMaximum(1000000000)
        self.gridLayout.addWidget(self.pc, 3, 1, 1, 1)
        self.label_9 = QLabel(self.tab)
        self.label_9.setText("Gamma")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_17 = QLabel(self.tab)
        self.label_17.setText("")
        self.gridLayout.addWidget(self.label_17, 6, 2, 1, 1)
        self.name = QLineEdit(self.tab)
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.label_5 = QLabel(self.tab)
        self.label_5.setText("Chamber Pres")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_4 = QLabel(self.tab)
        self.label_4.setText("Chamber Temp")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.Tc = QSpinBox(self.tab)
        self.Tc.setMaximum(1000000000)
        self.gridLayout.addWidget(self.Tc, 2, 1, 1, 1)
        self.label_19 = QLabel(self.tab)
        self.label_19.setText("m")
        self.gridLayout.addWidget(self.label_19, 8, 2, 1, 1)
        self.MR = QDoubleSpinBox(self.tab)
        self.MR.setMaximum(1000000000.0)
        self.gridLayout.addWidget(self.MR, 5, 1, 1, 1)
        self.label_18 = QLabel(self.tab)
        self.label_18.setText("")
        self.gridLayout.addWidget(self.label_18, 7, 2, 1, 1)
        self.label = QLabel(self.tab)
        self.label.setText("Name")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lstar = QDoubleSpinBox(self.tab)
        self.lstar.setMaximum(1000000000.0)
        self.gridLayout.addWidget(self.lstar, 8, 1, 1, 1)
        self.MW = QDoubleSpinBox(self.tab)
        self.MW.setMaximum(1000000000.0)
        self.gridLayout.addWidget(self.MW, 6, 1, 1, 1)
        self.label_7 = QLabel(self.tab)
        self.label_7.setText("Mixture Ratio")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "Input")
        self.tab_2 = QWidget()
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.output = QTextBrowser(self.tab_2)
        self.output.setStyleSheet("font: \"Georgia\"")
        self.output.setObjectName("output")
        self.verticalLayout_2.addWidget(self.output)
        self.tabWidget.addTab(self.tab_2, "Output")
        self.verticalLayout.addWidget(self.tabWidget)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setTitle("File")
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.actionNew = QAction("New", self)
        self.actionNew.setShortcut("Ctrl+N")
        self.actionNew.triggered.connect(self.newAction)
        self.actionOpen = QAction("Open", self)
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.triggered.connect(self.load)
        self.actionSave = QAction("Save", self)
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.triggered.connect(self.saveAction)
        self.actionSave_As = QAction("Save As", self)
        self.actionSave_As.setShortcut("Ctrl+Shift+S")
        self.actionSave_As.triggered.connect(self.saveAsAction)
        self.actionQuit = QAction("Quit", self)
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.triggered.connect(qApp.quit)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

    def updateDisplay(self):
        if platform.system() == 'Linux':
            homedir = os.path.expanduser("~")
            shortfn = self.filename.replace(homedir,"~")
        else:
            shortfn = self.filename
        self.setWindowTitle(shortfn + " - Open Rocket Engine")
        self.name.setText(self.config["name"])
        self.thrust.setValue(self.config["thrust"])
        self.Tc.setValue(self.config["Tc"])
        self.pc.setValue(self.config["pc"])
        self.pe.setValue(self.config["pe"])
        self.MR.setValue(self.config["MR"])
        self.MW.setValue(self.config["MW"])
        self.gamma.setValue(self.config["gamma"])
        self.lstar.setValue(self.config["lstar"])
        self.area_ratio.setValue(self.config["area_ratio"])

    def clearDisplay(self):
        self.name.setText("")
        self.thrust.setValue(0)
        self.Tc.setValue(0)
        self.pc.setValue(0)
        self.pe.setValue(0)
        self.MR.setValue(0)
        self.MW.setValue(0)
        self.gamma.setValue(0)
        self.lstar.setValue(0)
        self.area_ratio.setValue(0)

    def pullFromDisplay(self):
        self.config['name'] = self.name.text()
        self.config['thrust'] = self.thrust.value()
        self.config['Tc'] = self.Tc.value()
        self.config['pc'] = self.pc.value()
        self.config['pe'] = self.pe.value()
        self.config['MR'] = self.MR.value()
        self.config['MW'] = self.MW.value()
        self.config['gamma'] = self.gamma.value()
        self.config['lstar'] = self.lstar.value()
        self.config['area_ratio'] = self.area_ratio.value()

    def newAction(self):
        self.filename = "";
        self.config = {}
        self.clearDisplay()

    def saveAsAction(self):
        fname = QFileDialog.getSaveFileName(self, 'Open file',
                '',"Config Files (*.cfg)")[0]
        if (fname == ""):
            return;
        else:
            self.savefile(fname)

    def saveAction(self):
        self.savefile("")

    def savefile(self, new = ""):
        self.pullFromDisplay()
        if (new != ""):
            self.filename = new;

        with open(self.filename,'w+') as file:
            output = "name "+self.config['name']
            output += "\nunits SI"
            output += "\nthrust "+str(self.config['thrust'])
            output += "\nTc "+str(self.config['Tc'])
            output += "\npc "+str(self.config['pc'])
            output += "\npe "+str(self.config['pe'])
            output += "\nMR "+str(self.config['MR'])
            output += "\nMW "+str(self.config['MW'])
            output += "\ngamma "+str(self.config['gamma'])
            output += "\nlstar "+str(self.config['lstar'])
            output += "\narea_ratio "+str(self.config['area_ratio'])
            file.write(output)

    def load(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                '',"Config Files (*.cfg)")[0]
        if (fname == ""):
            print("test")
            return;
        self.filename = fname

        self.config = read_config(self.filename)
        self.updateDisplay()

    def run(self):
        engine = Engine(**self.config)
        self.tabWidget.setCurrentIndex(1)
        self.output.setText(engine.text_output())
