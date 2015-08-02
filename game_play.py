# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_play.ui'
#
# Created: Sun Aug  2 13:02:11 2015
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
        Dialog.resize(640, 369)
        self.label_scores = QtGui.QLabel(Dialog)
        self.label_scores.setGeometry(QtCore.QRect(30, 10, 221, 16))
        self.label_scores.setObjectName(_fromUtf8("label_scores"))
        self.label_error = QtGui.QLabel(Dialog)
        self.label_error.setGeometry(QtCore.QRect(30, 340, 591, 16))
        self.label_error.setObjectName(_fromUtf8("label_error"))
        self.label_player = QtGui.QLabel(Dialog)
        self.label_player.setGeometry(QtCore.QRect(310, 40, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_player.setFont(font)
        self.label_player.setAlignment(QtCore.Qt.AlignCenter)
        self.label_player.setObjectName(_fromUtf8("label_player"))
        self.label_input = QtGui.QLabel(Dialog)
        self.label_input.setGeometry(QtCore.QRect(330, 100, 62, 16))
        self.label_input.setObjectName(_fromUtf8("label_input"))
        self.inputField = QtGui.QLineEdit(Dialog)
        self.inputField.setGeometry(QtCore.QRect(380, 100, 113, 26))
        self.inputField.setObjectName(_fromUtf8("inputField"))
        self.submit = QtGui.QPushButton(Dialog)
        self.submit.setGeometry(QtCore.QRect(500, 100, 92, 27))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.quit = QtGui.QPushButton(Dialog)
        self.quit.setGeometry(QtCore.QRect(520, 330, 92, 27))
        self.quit.setObjectName(_fromUtf8("quit"))
        self.label_toss = QtGui.QLabel(Dialog)
        self.label_toss.setGeometry(QtCore.QRect(30, 170, 221, 16))
        self.label_toss.setObjectName(_fromUtf8("label_toss"))
        self.label_stats = QtGui.QLabel(Dialog)
        self.label_stats.setGeometry(QtCore.QRect(350, 170, 221, 16))
        self.label_stats.setObjectName(_fromUtf8("label_stats"))
        self.text_scores = QtGui.QTextBrowser(Dialog)
        self.text_scores.setGeometry(QtCore.QRect(30, 30, 241, 121))
        self.text_scores.setObjectName(_fromUtf8("text_scores"))
        self.text_toss = QtGui.QTextBrowser(Dialog)
        self.text_toss.setGeometry(QtCore.QRect(30, 190, 241, 121))
        self.text_toss.setObjectName(_fromUtf8("text_toss"))
        self.text_stats = QtGui.QTextBrowser(Dialog)
        self.text_stats.setGeometry(QtCore.QRect(350, 190, 241, 121))
        self.text_stats.setObjectName(_fromUtf8("text_stats"))
        self.undo = QtGui.QPushButton(Dialog)
        self.undo.setGeometry(QtCore.QRect(500, 140, 92, 27))
        self.undo.setObjectName(_fromUtf8("undo"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_scores.setText(_translate("Dialog", "Current Scores", None))
        self.label_error.setText(_translate("Dialog", "Error Message", None))
        self.label_player.setText(_translate("Dialog", "Player XX to throw", None))
        self.label_input.setText(_translate("Dialog", "Score:", None))
        self.submit.setText(_translate("Dialog", "Submit", None))
        self.quit.setText(_translate("Dialog", "Quit Game", None))
        self.label_toss.setText(_translate("Dialog", "Toss Values", None))
        self.label_stats.setText(_translate("Dialog", "Player Stats", None))
        self.undo.setText(_translate("Dialog", "Undo", None))

