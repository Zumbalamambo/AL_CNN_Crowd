# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue Nov  8 15:54:37 2016
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
        MainWindow.resize(1300, 1100)
        self.labels = []
        self.btn_L0 = []
        self.btn_L1 = []
        self.btn_L2 = []
        self.btn_L3 = []


        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lbl_image = QtGui.QLabel(self.centralwidget)
        self.lbl_image.setGeometry(QtCore.QRect(50, 30, 1024, 576))
        self.lbl_image.setObjectName(_fromUtf8("lbl_image"))
        self.btn_view_imgs = QtGui.QPushButton(self.centralwidget)
        self.btn_view_imgs.setGeometry(QtCore.QRect(1130, 30, 96, 31))
        self.btn_view_imgs.setObjectName(_fromUtf8("btn_view_imgs"))

        self.btn_predict = QtGui.QPushButton(self.centralwidget)
        self.btn_predict.setGeometry(QtCore.QRect(1130, 140, 96, 31))
        self.btn_predict.setObjectName(_fromUtf8("btn_predict"))

        self.btn_clear_points = QtGui.QPushButton(self.centralwidget)
        self.btn_clear_points.setGeometry(QtCore.QRect(1130, 190, 96, 31))
        self.btn_clear_points.setObjectName(_fromUtf8("btn_predict"))

        self.btn_prev_img = QtGui.QPushButton(self.centralwidget)
        self.btn_prev_img.setGeometry(QtCore.QRect(1130, 80, 96, 31))
        self.btn_prev_img.setObjectName(_fromUtf8("btn_prev_img"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1100, 640, 101, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_class_1 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_class_1.setObjectName(_fromUtf8("btn_class_1"))
        self.horizontalLayout.addWidget(self.btn_class_1)

        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 640, 500, 91))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 750, 250, 120))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.GL_L0 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.GL_L0.setMargin(0)
        self.GL_L0.setObjectName(_fromUtf8("GL_L0"))

        self.gridLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(320, 750, 300, 120))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.GL_L1 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.GL_L1.setMargin(0)
        self.GL_L1.setObjectName(_fromUtf8("GL_L1"))

        self.gridLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(630, 750, 250, 250))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.GL_L2 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.GL_L2.setMargin(0)
        self.GL_L2.setObjectName(_fromUtf8("GL_L2"))

        self.gridLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(890, 750, 300, 120))
        self.gridLayoutWidget_5.setObjectName(_fromUtf8("gridLayoutWidget_5"))
        self.GL_L3 = QtGui.QGridLayout(self.gridLayoutWidget_5)
        self.GL_L3.setMargin(0)
        self.GL_L3.setObjectName(_fromUtf8("GL_L3"))


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
        self.btn_view_imgs.setText(_translate("MainWindow", "Next Image", None))
        self.btn_predict.setText(_translate("MainWindow", "Predict", None))
        self.btn_prev_img.setText(_translate("MainWindow", "Prev Image", None))
        self.btn_class_1.setText(_translate("MainWindow", "Train", None))
        self.btn_clear_points.setText(_translate("MainWindow", "cl_points", None))

    def create_lbl_layers(self, nkerns):
        for idx in range(nkerns[0]):
            self.labels.append(QtGui.QLabel(self.gridLayoutWidget))
            self.labels[idx].setObjectName(_fromUtf8("lbl_L0_%d" % idx))
            # self.Hlayout_filters_L0.addWidget(self.labels[idx])
            self.labels[idx].setText(_translate("MainWindow", "TextLabel", None))
            # self.labels[idx].setMinimumSize(QtCore.QSize(100, 100))
        c = 0
        for i in range(4):
            for j in range(10):
                if c < nkerns[0]:
                    self.gridLayout.addWidget(self.labels[c], i, j, 1, 1)
                    self.gridLayout.addWidget(self.labels[c], i, j, 1, 1)
                    c += 1

    def create_btn_Layers(self, nkerns):
        for idx in range(nkerns[0]):
            self.btn_L0.append(QtGui.QPushButton(self.gridLayoutWidget_2))
            self.btn_L0[idx].setObjectName(_fromUtf8("btn_L0_%d" % idx))
            self.btn_L0[idx].setText(_translate("MainWindow", "%d" % idx, None))

        c = 0
        for i in range(4):
            for j in range(8):
                self.GL_L0.addWidget(self.btn_L0[c], i, j, 1, 1)
                c += 1

        for idx in range(nkerns[1]):
            self.btn_L1.append(QtGui.QPushButton(self.gridLayoutWidget_3))
            self.btn_L1[idx].setObjectName(_fromUtf8("btn_L1_%d" % idx))
            self.btn_L1[idx].setText(_translate("MainWindow", "%d" % idx, None))

        c = 0
        for i in range(5):
            for j in range(10):
                self.GL_L1.addWidget(self.btn_L1[c], i, j, 1, 1)
                c += 1


        for idx in range(nkerns[2]):
            self.btn_L2.append(QtGui.QPushButton(self.gridLayoutWidget_4))
            self.btn_L2[idx].setObjectName(_fromUtf8("btn_L2_%d" % idx))
            self.btn_L2[idx].setText(_translate("MainWindow", "%d" % idx, None))

        c = 0
        for i in range(8):
            for j in range(8):
                self.GL_L2.addWidget(self.btn_L2[c], i, j, 1, 1)
                c += 1


        for idx in range(nkerns[3]):
            self.btn_L3.append(QtGui.QPushButton(self.gridLayoutWidget_5))
            self.btn_L3[idx].setObjectName(_fromUtf8("btn_L3_%d" % idx))
            self.btn_L3[idx].setText(_translate("MainWindow", "%d" % idx, None))

        c = 0
        for i in range(5):
            for j in range(10):
                self.GL_L3.addWidget(self.btn_L3[c], i, j, 1, 1)
                c += 1
