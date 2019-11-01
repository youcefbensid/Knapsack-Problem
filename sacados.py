# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\EssaiPython\TPGO1\sacados.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from code import *

objets = [] 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 418)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/EssaiPython/TPGO1/sacados.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.supprimer = QtWidgets.QPushButton(self.centralwidget)
        self.supprimer.setGeometry(QtCore.QRect(360, 330, 101, 21))
        self.supprimer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.supprimer.setObjectName("supprimer")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 21, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 31, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 30, 21, 21))
        self.label_3.setObjectName("label_3")
        self.nom = QtWidgets.QLineEdit(self.centralwidget)
        self.nom.setGeometry(QtCore.QRect(70, 30, 113, 20))
        self.nom.setObjectName("nom")
        self.poids = QtWidgets.QSpinBox(self.centralwidget)
        self.poids.setGeometry(QtCore.QRect(230, 30, 42, 22))
        self.poids.setObjectName("poids")
        self.gain = QtWidgets.QSpinBox(self.centralwidget)
        self.gain.setGeometry(QtCore.QRect(330, 30, 42, 22))
        self.gain.setObjectName("gain")
        self.ajouter = QtWidgets.QPushButton(self.centralwidget)
        self.ajouter.setGeometry(QtCore.QRect(420, 30, 91, 23))
        self.ajouter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ajouter.setObjectName("ajouter")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 60, 491, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.poidstotal = QtWidgets.QSpinBox(self.centralwidget)
        self.poidstotal.setGeometry(QtCore.QRect(90, 120, 42, 22))
        self.poidstotal.setObjectName("poidstotal")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 51, 21))
        self.label_4.setObjectName("label_4")
        self.lancer = QtWidgets.QPushButton(self.centralwidget)
        self.lancer.setGeometry(QtCore.QRect(140, 120, 111, 23))
        self.lancer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lancer.setObjectName("lancer")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 170, 91, 21))
        self.label_5.setObjectName("label_5")
        self.liste = QtWidgets.QListWidget(self.centralwidget)
        self.liste.setGeometry(QtCore.QRect(300, 110, 221, 211))
        self.liste.setObjectName("liste")
        self.resultat = QtWidgets.QListWidget(self.centralwidget)
        self.resultat.setGeometry(QtCore.QRect(40, 190, 211, 131))
        self.resultat.setObjectName("resultat")
        self.gainMaximal = QtWidgets.QLabel(self.centralwidget)
        self.gainMaximal.setGeometry(QtCore.QRect(90, 330, 171, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gainMaximal.setFont(font)
        self.gainMaximal.setObjectName("gainMaximal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ajouter.clicked.connect(self.ajouterElem)
        self.supprimer.clicked.connect(self.supprimerElem)
        self.lancer.clicked.connect(self.lancerAlgo) 


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Problème du sac à dos"))
        self.supprimer.setText(_translate("MainWindow", "Supprimer élément"))
        self.label.setText(_translate("MainWindow", "Nom"))
        self.label_2.setText(_translate("MainWindow", "Poids"))
        self.label_3.setText(_translate("MainWindow", "Gain"))
        self.ajouter.setText(_translate("MainWindow", "Ajouter élément"))
        self.label_4.setText(_translate("MainWindow", "Poids total"))
        self.lancer.setText(_translate("MainWindow", "Lancer algorithme"))
        self.label_5.setText(_translate("MainWindow", "Eléments choisis :"))
        self.gainMaximal.setText(_translate("MainWindow", "Gain maximal = "))


    def ajouterElem(self):
        nomAct = self.nom.text()
        poidsAct = self.poids.value()
        gainAct = self.gain.value()
        elementActuel = Element(nomAct,poidsAct,gainAct)
        objets.append(elementActuel)    
        
        texteListe = "nom = " + elementActuel.nom + ", poids = " + str(elementActuel.poids) + ", gain = " + str(elementActuel.gain)
        self.liste.addItem(texteListe) 

        self.nom.clear()
        self.poids.clear()
        self.gain.clear()

        
    def supprimerElem(self):
        index = self.liste.currentRow()
        del objets[index]
        self.liste.takeItem(index)


    def lancerAlgo(self):
        self.resultat.clear()
        colonnes = self.poidstotal.value() + 1
        lignes = len(objets) + 1
        matrice = creerMatrice(objets,lignes,colonnes)
        resultat = trouveResultat(matrice,self.poidstotal.value(),objets)
        for objet in resultat:
            texteRes = "nom = " + objet.nom + ", poids = " + str(objet.poids) + ", gain = " + str(objet.gain)
            self.resultat.addItem(texteRes)
        gainMaxTexte = "Gain maximal = " + str(matrice[lignes-1][colonnes-1])
        self.gainMaximal.setText(gainMaxTexte)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

