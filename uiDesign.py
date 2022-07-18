from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from  PyQt5.uic import loadUi
import sys
from SubstitutionCipher.MonoAlphabetic.mono_alpha import MonoAlphabetic_Substituion

class InterfaceDesign(QMainWindow):
    def __init__(self):
        super(InterfaceDesign, self).__init__()
        loadUi('myUi.ui',self)

        self.connectEvents()

    def connectEvents(self):
        self.encipher_btn.clicked.connect(self.encipherText)
        self.encipher_clear_btn.clicked.connect(self.clear_encipher_boxes)
        self.decipher_btn.clicked.connect(self.decipherText)
        self.decipher_clear_btn.clicked.connect(self.clear_decipher_boxes)

    def decipherText(self):
        # check for empty values
        if len(self.decipher_text.text().strip()) > 0 and len(self.decipher_jumps.text()) > 0:
            try:

                # get the values from the boxes
                text = self.decipher_text.text().strip().replace(" ","")
                jumps = int(self.decipher_jumps.text())

                # print(text, jumps)


                # create the object of the method
                method = MonoAlphabetic_Substituion(text=text, jumps=jumps)
                # custom dialog box
                response = QMessageBox.question(self,"Info","Do you want case sensitivity?",QMessageBox.Yes |QMessageBox.No)

                if response == QMessageBox.Yes:
                    self.deciphered_text.setText(method.decipher(case_sensitive=True))

                if response == QMessageBox.No:
                    self.deciphered_text.setText(method.decipher(case_sensitive=False))








            except Exception as e:
                QMessageBox.information(self, "Error", "Invalid Data Type of <b>Jumps</b>")
        else:
            QMessageBox.information(self, "Error", "Data is Missing")

    def clear_decipher_boxes(self):
        self.deciphered_text.setText('')
        self.decipher_jumps.setText('')
        self.decipher_text.setText('')

    def encipherText(self):

        # check for empty values
        if len(self.encipher_text.text().strip()) > 0 and len(self.encipher_jumps.text()) > 0:
            try:

                # get the values from the boxes
                text = self.encipher_text.text().strip().replace(" ","")
                jumps = int(self.encipher_jumps.text())



                print(text,jumps)
                # create the object of the method
                method = MonoAlphabetic_Substituion(text=text,jumps=jumps)
                response = QMessageBox.question(self, "Info", "Do you want case sensitivity?",
                                                QMessageBox.Yes | QMessageBox.No)
                if response == QMessageBox.Yes:
                    self.enciphered_text.setText(method.encipher(case_sensitive=True))
                else:
                    self.enciphered_text.setText(method.encipher(case_sensitive=False))


            except Exception as e:
                QMessageBox.information(self, "Error", "Invalid Data Type of <b>Jumps</b>")
        else:
            QMessageBox.information(self,"Error","Data is Missing")

    def clear_encipher_boxes(self):
        self.enciphered_text.setText('')
        self.encipher_jumps.setText('')
        self.encipher_text.setText('')

app = QApplication(sys.argv)

window = InterfaceDesign()
window.show()
app.exec_()