# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\arknightsUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 300)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.centralwidget.setFont(font)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.frame.setStyleSheet("QFrame{background-image: url(:/新前缀/ui_img/background.png);}\n"
"\n"
"QLabel{color:#fff;background:transparent;font-size:14px;font-weight:bold}\n"
"\n"
"QPushButton{border:rgba(255,255,255,0.8);background:rgba(255,255,255,0.7);height:30px;border-radius:4px}\n"
"QPushButton:pressed{background-color:rgba(255,255,255,0.5);}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 5, 80, 20))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 244, 239, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.devConnectBt = QtWidgets.QPushButton(self.layoutWidget)
        self.devConnectBt.setObjectName("devConnectBt")
        self.horizontalLayout.addWidget(self.devConnectBt)
        self.startGameBt = QtWidgets.QPushButton(self.layoutWidget)
        self.startGameBt.setObjectName("startGameBt")
        self.horizontalLayout.addWidget(self.startGameBt)
        self.expMapBt = QtWidgets.QPushButton(self.layoutWidget)
        self.expMapBt.setObjectName("expMapBt")
        self.horizontalLayout.addWidget(self.expMapBt)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "设备未连接"))
        self.devConnectBt.setText(_translate("MainWindow", "连接设备"))
        self.startGameBt.setText(_translate("MainWindow", "启动游戏"))
        self.expMapBt.setText(_translate("MainWindow", "开始刷本"))
import ui_rc
