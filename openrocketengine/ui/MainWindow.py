from openrocketengine.core.rocket import Engine
from openrocketengine.core.interface import standard_types, read_config
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import platform

if platform.system() == "Linux":
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
        self.label_13.setText("K")
        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)
        self.label_3 = QLabel(self.tab)
        self.label_3.setText("Thrust")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.area_ratio = QLineEdit(self.tab)
        self.gridLayout.addWidget(self.area_ratio, 9, 1, 1, 1)
        self.thrust = QLineEdit(self.tab)
        self.gridLayout.addWidget(self.thrust, 1, 1, 1, 1)
        self.label_11 = QLabel(self.tab)
        self.label_11.setText("Area Ratio")
        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)
        self.pe = QLineEdit(self.tab)
        self.gridLayout.addWidget(self.pe, 4, 1, 1, 1)
        self.label_12 = QLabel(self.tab)
        self.label_12.setText("N")
        self.gridLayout.addWidget(self.label_12, 1, 2, 1, 1)
        self.gamma = QLineEdit(self.tab)
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
        self.pc = QLineEdit(self.tab)
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
        self.Tc = QLineEdit(self.tab)
        self.gridLayout.addWidget(self.Tc, 2, 1, 1, 1)
        self.label_19 = QLabel(self.tab)
        self.label_19.setText("m")
        self.gridLayout.addWidget(self.label_19, 8, 2, 1, 1)
        self.MR = QLineEdit(self.tab)
        self.gridLayout.addWidget(self.MR, 5, 1, 1, 1)
        self.label_18 = QLabel(self.tab)
        self.label_18.setText("")
        self.gridLayout.addWidget(self.label_18, 7, 2, 1, 1)
        self.label = QLabel(self.tab)
        self.label.setText("Name")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lstar = QLineEdit(self.tab)
        self.gridLayout.addWidget(self.lstar, 8, 1, 1, 1)
        self.MW = QLineEdit(self.tab)
        self.gridLayout.addWidget(self.MW, 6, 1, 1, 1)
        self.label_7 = QLabel(self.tab)
        self.label_7.setText("Mixture Ratio")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "Input")
        self.tab_2 = QWidget()
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.output = QTextBrowser(self.tab_2)
        self.output.setStyleSheet('font: "Georgia"')
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
        if platform.system() == "Linux":
            homedir = os.path.expanduser("~")
            shortfn = self.filename.replace(homedir, "~")
        else:
            shortfn = self.filename
        self.setWindowTitle(shortfn + " - Open Rocket Engine")
        self.name.setText(self.config["name"])
        self.thrust.setText(str(self.config["thrust"]))
        self.Tc.setText(str(self.config["Tc"]))
        self.pc.setText(str(self.config["pc"]))
        self.pe.setText(str(self.config["pe"]))
        self.MR.setText(str(self.config["MR"]))
        self.MW.setText(str(self.config["MW"]))
        self.gamma.setText(str(self.config["gamma"]))
        self.lstar.setText(str(self.config["lstar"]))
        self.area_ratio.setText(str(self.config["area_ratio"]))

    def clearDisplay(self):
        self.name.setText("")
        self.thrust.setText(0)
        self.Tc.setText(0)
        self.pc.setText(0)
        self.pe.setText(0)
        self.MR.setText(0)
        self.MW.setText(0)
        self.gamma.setText(0)
        self.lstar.setText(0)
        self.area_ratio.setText(0)

    def pullFromDisplay(self):
        self.config["name"] = self.name.text()
        self.config["thrust"] = float(self.thrust.text())
        self.config["Tc"] = float(self.Tc.text())
        self.config["pc"] = float(self.pc.text())
        self.config["pe"] = float(self.pe.text())
        self.config["MR"] = float(self.MR.text())
        self.config["MW"] = float(self.MW.text())
        self.config["gamma"] = float(self.gamma.text())
        self.config["lstar"] = float(self.lstar.text())
        self.config["area_ratio"] = float(self.area_ratio.text())

    def newAction(self):
        self.filename = ""
        self.config = {}
        self.clearDisplay()

    def saveAsAction(self):
        fname = QFileDialog.getSaveFileName(
            self, "Open file", "", "Config Files (*.cfg)"
        )[0]
        if fname == "":
            return
        else:
            self.savefile(fname)

    def saveAction(self):
        self.savefile("")

    def savefile(self, new=""):
        self.pullFromDisplay()
        if new != "":
            self.filename = new

        with open(self.filename, "w+") as file:
            output = "name " + self.config["name"]
            output += "\nunits SI"
            output += "\nthrust " + str(self.config["thrust"])
            output += "\nTc " + str(self.config["Tc"])
            output += "\npc " + str(self.config["pc"])
            output += "\npe " + str(self.config["pe"])
            output += "\nMR " + str(self.config["MR"])
            output += "\nMW " + str(self.config["MW"])
            output += "\ngamma " + str(self.config["gamma"])
            output += "\nlstar " + str(self.config["lstar"])
            output += "\narea_ratio " + str(self.config["area_ratio"])
            file.write(output)

    def load(self):
        fname = QFileDialog.getOpenFileName(
            self, "Open file", "", "Config Files (*.cfg)"
        )[0]
        if fname == "":
            return
        self.filename = fname

        self.config = read_config(self.filename)
        self.updateDisplay()

    def run(self):
        if not self.config:
            QMessageBox.critical(self, "Error", "No input file!")
            return
        engine = Engine(**self.config)
        self.tabWidget.setCurrentIndex(1)
        self.output.append("Engine Name: " + engine.name)
        self.output.append("")
        self.output.append("Thrust: " + str(engine.thrust) + " N")
        self.output.append("Thrust Vac: " + str(engine.thrust_vac) + " N")
        self.output.append("Isp: " + str(engine.Isp) + " s")
        self.output.append("Isp Vac: " + str(engine.Isp_vac) + " s")
        self.output.append("Mdot: " + str(engine.mdot) + " kg/s")
        self.output.append("Mixture Ratio: " + str(engine.MR) + ":1")
        self.output.append("")
        self.output.append("Geometry:")
        self.output.append("Ac, Chamber Area: " + str(engine.Ac) + " m^2")
        self.output.append("Rc, Chamber Radius: " + str(engine.Rc) + " m")
        self.output.append("At, Throat Area: " + str(engine.At) + " m^2")
        self.output.append("Rt, Throat Radius: " + str(engine.Rt) + " m")
        self.output.append("Ae, Exit Area: " + str(engine.Ae) + " m^2")
        self.output.append("Re, Exit Radius: " + str(engine.Re) + " m")
        self.output.append("Rn, Radius Leaving Throat: " + str(engine.Rn) + " m")
        self.output.append(
            "Ea, expansion area ratio (Ae/At): "
            + str(engine.expansion_area_ratio)
            + ":1"
        )
        self.output.append(
            "Ec, contraction area ratio (Ac/Ae): "
            + str(engine.contraction_area_ratio)
            + ":1"
        )
        self.output.append(
            "Thetac, contraction angle: " + str(engine.contraction_angle) + " degrees"
        )
        self.output.append("L*: " + str(engine.lstar) + " m")
        self.output.append("Vc, chamber volume: " + str(engine.Vc) + " m")
        self.output.append(
            "lcyl, cylindrical section of combustion chamber: "
            + str(engine.lcyl)
            + " m"
        )
        self.output.append("length of nozzle: " + str(engine.ln) + " m")
