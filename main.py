from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3

con = sqlite3.connect(r"./dss.sql")

cur = con.cursor()

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(800, 574)
        Home.setStyleSheet("background-color: rgb(112, 112, 112);")
        self.centralwidget = QtWidgets.QWidget(Home)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 150, 121, 16))
        self.label.setObjectName("label")
        self.temperature = QtWidgets.QTextEdit(self.centralwidget)
        self.temperature.setGeometry(QtCore.QRect(220, 150, 221, 31))
        self.temperature.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.temperature.setObjectName("temperature")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 270, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 151, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 310, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 350, 161, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, -10, 551, 111))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(64, 480, 101, 23))
        self.clear_button.setObjectName("clear_button")
        self.dbAdd = QtWidgets.QPushButton(self.centralwidget)
        self.dbAdd.setGeometry(QtCore.QRect(180, 460, 221, 51))
        self.dbAdd.setObjectName("dbAdd")
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(660, 480, 75, 23))
        self.close_button.setObjectName("close_button")
        self.prime_symp = QtWidgets.QTextEdit(self.centralwidget)
        self.prime_symp.setGeometry(QtCore.QRect(220, 190, 221, 31))
        self.prime_symp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prime_symp.setObjectName("prime_symp")
        self.sec_symp = QtWidgets.QTextEdit(self.centralwidget)
        self.sec_symp.setGeometry(QtCore.QRect(220, 230, 221, 31))
        self.sec_symp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sec_symp.setObjectName("sec_symp")
        self.bp = QtWidgets.QTextEdit(self.centralwidget)
        self.bp.setGeometry(QtCore.QRect(220, 270, 221, 31))
        self.bp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bp.setObjectName("bp")
        self.heart = QtWidgets.QTextEdit(self.centralwidget)
        self.heart.setGeometry(QtCore.QRect(220, 310, 221, 31))
        self.heart.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.heart.setObjectName("heart")
        self.respiratory = QtWidgets.QTextEdit(self.centralwidget)
        self.respiratory.setGeometry(QtCore.QRect(220, 350, 221, 31))
        self.respiratory.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.respiratory.setObjectName("respiratory")
        self.lalDisease = QtWidgets.QLabel(self.centralwidget)
        self.lalDisease.setGeometry(QtCore.QRect(40, 110, 121, 16))
        self.lalDisease.setObjectName("lalDisease")
        self.Disease_name = QtWidgets.QTextEdit(self.centralwidget)
        self.Disease_name.setGeometry(QtCore.QRect(220, 110, 221, 31))
        self.Disease_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Disease_name.setObjectName("Disease_name")
        self.diagnosis = QtWidgets.QPushButton(self.centralwidget)
        self.diagnosis.setGeometry(QtCore.QRect(410, 460, 221, 51))
        self.diagnosis.setObjectName("diagnosis")
        self.prog_view = QtWidgets.QTextEdit(self.centralwidget)
        self.prog_view.setObjectName(u"prog_view")
        self.prog_view.setGeometry(QtCore.QRect(550, 220, 221, 31))
        self.prog_view.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label.raise_()
        self.temperature.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.clear_button.raise_()
        self.dbAdd.raise_()
        self.close_button.raise_()
        self.prime_symp.raise_()
        self.sec_symp.raise_()
        self.bp.raise_()
        self.heart.raise_()
        self.respiratory.raise_()
        self.lalDisease.raise_()
        self.Disease_name.raise_()
        self.diagnosis.raise_()
        self.label_7.raise_()
        self.prog_view.raise_()
        Home.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Home)
        self.statusbar.setObjectName("statusbar")
        Home.setStatusBar(self.statusbar)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

        

        def addTo():

            tempereature = self.temperature.toPlainText()
            prime_symp = self.prime_symp.toPlainText()
            sec_symp = self.sec_symp.toPlainText()
            bp = self.bp.toPlainText()
            heart = self.heart.toPlainText()
            respiratory = self.respiratory.toPlainText()
            disease = self.Disease_name.toPlainText()
            
            import sqlite3
            con = sqlite3.connect(r"./dss.sql")

            cur = con.cursor()
            cur.execute(
                "INSERT INTO Diseases VALUES(:Disease, :Prime_Symptom, :2nd_Symptom, :Temparature, :Bp_mmHg, :HR, :rrr)",
                {
                    'Disease': disease,
                    'Prime_Symptom': prime_symp,
                    '2nd_Symptom': sec_symp,
                    'Temparature': tempereature,
                    'Bp_mmHg': bp,
                    'HR': heart,
                    'rrr': respiratory,
                })

            con.commit()

        # Close connection
            con.close()

            return
        
        

        self.dbAdd.clicked.connect(addTo)


        def viewTo():
            tempereature = self.temperature.toPlainText()
            prime_symp = self.prime_symp.toPlainText()
            sec_symp = self.sec_symp.toPlainText()
            bp = self.bp.toPlainText()
            heart = self.heart.toPlainText()
            respiratory = self.respiratory.toPlainText()
            disease = self.Disease_name.toPlainText()
            
            import sqlite3
            con = sqlite3.connect(r"./dss.sql")

            cur = con.cursor()
            cur.execute(
                "SELECT * FROM Diseases WHERE Disease=?", (disease, ))
            rows = cur.fetchall()
            for row in rows:
                self.prog_view.toPlainText = print(row)

            con.commit()

        # Close connection
            con.close()

            return
        
        

        self.diagnosis.clicked.connect(viewTo)

        

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Home"))
        Home.setAccessibleName(_translate("Home", "DSS1"))
        self.label.setText(_translate("Home", "TEMPERATURE READING"))
        self.label_2.setText(_translate("Home", "BLOOD  PRESSURE"))
        self.label_3.setText(_translate("Home", "2ND SYMPTOM"))
        self.label_4.setText(_translate("Home", "PRIME SYMPTOM"))
        self.label_5.setText(_translate("Home", "HEART RATE"))
        self.label_6.setText(_translate("Home", "RESPIRATORY RATE"))
        self.label_7.setText(_translate("Home", "CLINICAL DECISION SUPPORT SYSTEM"))
        self.clear_button.setText(_translate("Home", "CLEAR"))
        self.dbAdd.setText(_translate("Home", "Add to Data Base"))
        self.close_button.setText(_translate("Home", "CLOSE"))
        self.lalDisease.setText(_translate("Home", "Disease Name"))
        self.diagnosis.setText(_translate("Home", "View prognosis"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Home = QtWidgets.QMainWindow()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec_())
