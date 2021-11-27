import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('main.ui', self)

        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        arr = cur.execute('''
                            SELECT * FROM coffee
                            ''').fetchall()

        for i, row in enumerate(arr):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())