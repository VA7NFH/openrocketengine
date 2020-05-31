from PyQt5.QtWidgets import *
import sys
from openrocketengine.ui.MainWindow import MainWindow

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
