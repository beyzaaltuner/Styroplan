import sys

from PySide6 import QtWidgets
from mainwindow import MainWindow

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()




