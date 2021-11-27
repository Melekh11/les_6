import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget
from add import Ui_Form
from release.not_main import Ui_MainWindow


class Change(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.app)

    def app(self):
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        if self.radioButton.isChecked():
            self.cur.execute('''
                                UPDATE coffee
                                SET name = ?, fired = ?, molot = ?, 
                                taste = ?, money = ?, v = ?  
                                WHERE id = ?
                                ''', (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(),
                                      self.lineEdit_4.text(), self.doubleSpinBox.value(), self.spinBox_2.value(),
                                      self.spinBox.value()))
        else:
            self.cur.execute('''
                                INSERT INTO coffee(name, fired, molot, taste, money, v) 
                                VALUES (?, ?, ?, ?, ?, ?)  
                                ''', (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(),
                                      self.lineEdit_4.text(), self.doubleSpinBox.value(),
                                      self.spinBox_2.value()))


        self.con.commit()
        self.con.close()
        self.app_2 = Example()
        self.app_2.show()
        self.close()



class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.ch)

        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        arr = self.cur.execute('''
                            SELECT * FROM coffee
                            ''').fetchall()

        for i, row in enumerate(arr):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

        self.con.close()

    def ch(self):
        self.app_in = Change()
        self.app_in.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())