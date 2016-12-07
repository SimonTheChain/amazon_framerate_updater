# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'framerate_updater_ui.ui'
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

class Ui_AmazonFramerateApp(object):
    def setupUi(self, AmazonFramerateApp):
        AmazonFramerateApp.setObjectName(_fromUtf8("AmazonFramerateApp"))
        AmazonFramerateApp.resize(800, 238)
        self.centralwidget = QtGui.QWidget(AmazonFramerateApp)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.original_btn = QtGui.QPushButton(self.centralwidget)
        self.original_btn.setObjectName(_fromUtf8("original_btn"))
        self.horizontalLayout.addWidget(self.original_btn)
        self.original_text = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.original_text.sizePolicy().hasHeightForWidth())
        self.original_text.setSizePolicy(sizePolicy)
        self.original_text.setReadOnly(True)
        self.original_text.setObjectName(_fromUtf8("original_text"))
        self.horizontalLayout.addWidget(self.original_text)
        self.clear_btn = QtGui.QPushButton(self.centralwidget)
        self.clear_btn.setObjectName(_fromUtf8("clear_btn"))
        self.horizontalLayout.addWidget(self.clear_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.destination_btn = QtGui.QPushButton(self.centralwidget)
        self.destination_btn.setObjectName(_fromUtf8("destination_btn"))
        self.horizontalLayout_2.addWidget(self.destination_btn)
        self.destination_line = QtGui.QLineEdit(self.centralwidget)
        self.destination_line.setReadOnly(True)
        self.destination_line.setObjectName(_fromUtf8("destination_line"))
        self.horizontalLayout_2.addWidget(self.destination_line)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.process_btn = QtGui.QPushButton(self.centralwidget)
        self.process_btn.setObjectName(_fromUtf8("process_btn"))
        self.horizontalLayout_3.addWidget(self.process_btn)
        self.process_line = QtGui.QLineEdit(self.centralwidget)
        self.process_line.setReadOnly(True)
        self.process_line.setObjectName(_fromUtf8("process_line"))
        self.horizontalLayout_3.addWidget(self.process_line)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        AmazonFramerateApp.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(AmazonFramerateApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        AmazonFramerateApp.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(AmazonFramerateApp)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        AmazonFramerateApp.setStatusBar(self.statusbar)

        self.retranslateUi(AmazonFramerateApp)
        QtCore.QMetaObject.connectSlotsByName(AmazonFramerateApp)

    def retranslateUi(self, AmazonFramerateApp):
        AmazonFramerateApp.setWindowTitle(_translate("AmazonFramerateApp", "Amazon Framerate Updater", None))
        self.label.setText(_translate("AmazonFramerateApp", "Locate MMC(s)", None))
        self.original_btn.setText(_translate("AmazonFramerateApp", "Browse...", None))
        self.clear_btn.setText(_translate("AmazonFramerateApp", "Clear", None))
        self.label_2.setText(_translate("AmazonFramerateApp", "Select destination", None))
        self.destination_btn.setText(_translate("AmazonFramerateApp", "Browse...", None))
        self.process_btn.setText(_translate("AmazonFramerateApp", "Process", None))

