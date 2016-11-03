# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Oct 21 10:20:05 2016
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1243, 824)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lbl_image = QtGui.QLabel(self.centralwidget)
        self.lbl_image.setGeometry(QtCore.QRect(50, 30, 1024, 576))
        self.lbl_image.setObjectName(_fromUtf8("lbl_image"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 660, 169, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_class_1 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.lbl_class_1.setObjectName(_fromUtf8("lbl_class_1"))
        self.horizontalLayout.addWidget(self.lbl_class_1)
        self.btn_class_1 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_class_1.setObjectName(_fromUtf8("btn_class_1"))
        self.horizontalLayout.addWidget(self.btn_class_1)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 700, 169, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lbl_class_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.lbl_class_2.setObjectName(_fromUtf8("lbl_class_2"))
        self.horizontalLayout_2.addWidget(self.lbl_class_2)
        self.btn_class_2 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_class_2.setObjectName(_fromUtf8("btn_class_2"))
        self.horizontalLayout_2.addWidget(self.btn_class_2)
        self.btn_view_imgs = QtGui.QPushButton(self.centralwidget)
        self.btn_view_imgs.setGeometry(QtCore.QRect(1130, 30, 96, 31))
        self.btn_view_imgs.setObjectName(_fromUtf8("btn_view_imgs"))
        self.btn_predict = QtGui.QPushButton(self.centralwidget)
        self.btn_predict.setGeometry(QtCore.QRect(1130, 140, 96, 31))
        self.btn_predict.setObjectName(_fromUtf8("btn_predict"))
        self.btn_prev_img = QtGui.QPushButton(self.centralwidget)
        self.btn_prev_img.setGeometry(QtCore.QRect(1130, 80, 96, 31))
        self.btn_prev_img.setObjectName(_fromUtf8("btn_prev_img"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1243, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lbl_image.setText(_translate("MainWindow", "TextLabel", None))
        self.lbl_class_1.setText(_translate("MainWindow", "Face", None))
        self.btn_class_1.setText(_translate("MainWindow", "Learn", None))
        self.lbl_class_2.setText(_translate("MainWindow", "Not Face", None))
        self.btn_class_2.setText(_translate("MainWindow", "Learn", None))
        self.btn_view_imgs.setText(_translate("MainWindow", "Next Image", None))
        self.btn_predict.setText(_translate("MainWindow", "Predict", None))
        self.btn_prev_img.setText(_translate("MainWindow", "Prev Image", None))

