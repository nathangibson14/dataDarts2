# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Sat Aug  1 18:32:26 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(598, 350)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(31, 260, 121, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 50, 121, 201))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget_2 = QtGui.QListWidget(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(420, 50, 121, 201))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.newPlayer = QtGui.QPushButton(Dialog)
        self.newPlayer.setGeometry(QtCore.QRect(30, 300, 121, 27))
        self.newPlayer.setObjectName(_fromUtf8("newPlayer"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 0, 71, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(440, 0, 71, 51))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(160, 50, 251, 201))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.removePlayer = QtGui.QPushButton(Dialog)
        self.removePlayer.setGeometry(QtCore.QRect(420, 260, 121, 27))
        self.removePlayer.setObjectName(_fromUtf8("removePlayer"))
        self.playGame = QtGui.QPushButton(Dialog)
        self.playGame.setGeometry(QtCore.QRect(210, 260, 151, 71))
        self.playGame.setObjectName(_fromUtf8("playGame"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "AddPlayer", None))
        self.newPlayer.setText(_translate("Dialog", "NewPlayer", None))
        self.label.setText(_translate("Dialog", "Available Players", None))
        self.label_2.setText(_translate("Dialog", "Game Players", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stats</p></body></html>", None))
        self.removePlayer.setText(_translate("Dialog", "RemovePlayer", None))
        self.playGame.setText(_translate("Dialog", "Play Game!", None))

