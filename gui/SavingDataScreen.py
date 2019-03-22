# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SavingDataScreen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_loadingScreen(object):
    def setupUi(self, loadingScreen):
        loadingScreen.setObjectName(_fromUtf8("loadingScreen"))
        loadingScreen.resize(210, 130)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../imgV/logoventuri.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loadingScreen.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(loadingScreen)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_gif = QtGui.QLabel(loadingScreen)
        self.lbl_gif.setText(_fromUtf8(""))
        self.lbl_gif.setScaledContents(True)
        self.lbl_gif.setObjectName(_fromUtf8("lbl_gif"))
        self.horizontalLayout.addWidget(self.lbl_gif)

        self.retranslateUi(loadingScreen)
        QtCore.QMetaObject.connectSlotsByName(loadingScreen)

    def retranslateUi(self, loadingScreen):
        loadingScreen.setWindowTitle(_translate("loadingScreen", "Saving Data", None))

