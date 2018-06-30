# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(502, 454)
        self.buttonBoxAbout = QtWidgets.QDialogButtonBox(About)
        self.buttonBoxAbout.setGeometry(QtCore.QRect(20, 400, 461, 32))
        self.buttonBoxAbout.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxAbout.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxAbout.setObjectName("buttonBoxAbout")
        self.labelAbout = QtWidgets.QLabel(About)
        self.labelAbout.setGeometry(QtCore.QRect(50, 40, 411, 341))
        self.labelAbout.setTextFormat(QtCore.Qt.AutoText)
        self.labelAbout.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelAbout.setWordWrap(True)
        self.labelAbout.setObjectName("labelAbout")

        self.retranslateUi(About)
        self.buttonBoxAbout.accepted.connect(About.accept)
        self.buttonBoxAbout.rejected.connect(About.reject)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Dialog"))
        self.labelAbout.setText(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">PyRotor Controller GUI </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Version</span> 1.0<br /><span style=\" font-weight:600;\">License</span>: MIT<br /><span style=\" font-weight:600;\">Author</span>: David Fannin, KK6DF<br /><br />URL: http://github.com/dfannin/pyrotor<br /><br /><span style=\" font-weight:600;\">Description:</span> QT5 front-end GUI for hamlib rotctld. <br />Provides control and display of ham radio antenna rotor.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Features</span>: Rotctld start/stop, Configuration, Compass Display,<br />Move/Stop Buttons, Position Buttons, Numerical Display. <br /><br /><span style=\" font-weight:600;\">Requires: </span>hamlib (rotctl), qt5, python3, Linux or Mac</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

