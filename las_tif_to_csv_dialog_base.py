# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class Ui_LasTifToCsvDialogBase(object):

    def setupUi(self, LasTifToCsvDialogBase):

        LasTifToCsvDialogBase.setObjectName("LasTifToCsvDialogBase")
        LasTifToCsvDialogBase.resize(520, 380)

        # LAS
        self.label = QtWidgets.QLabel(LasTifToCsvDialogBase)
        self.label.setGeometry(QtCore.QRect(20, 15, 150, 20))
        self.label.setObjectName("label")

        self.lineEditLas = QtWidgets.QLineEdit(LasTifToCsvDialogBase)
        self.lineEditLas.setGeometry(QtCore.QRect(20, 40, 380, 30))
        self.lineEditLas.setObjectName("lineEditLas")

        self.pushButtonLas = QtWidgets.QPushButton(LasTifToCsvDialogBase)
        self.pushButtonLas.setGeometry(QtCore.QRect(410, 40, 80, 30))
        self.pushButtonLas.setObjectName("pushButtonLas")

        # TIF
        self.label_2 = QtWidgets.QLabel(LasTifToCsvDialogBase)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 150, 20))
        self.label_2.setObjectName("label_2")

        self.lineEditTif = QtWidgets.QLineEdit(LasTifToCsvDialogBase)
        self.lineEditTif.setGeometry(QtCore.QRect(20, 115, 380, 30))
        self.lineEditTif.setObjectName("lineEditTif")

        self.pushButtonTif = QtWidgets.QPushButton(LasTifToCsvDialogBase)
        self.pushButtonTif.setGeometry(QtCore.QRect(410, 115, 80, 30))
        self.pushButtonTif.setObjectName("pushButtonTif")

        # CSV
        self.label_3 = QtWidgets.QLabel(LasTifToCsvDialogBase)
        self.label_3.setGeometry(QtCore.QRect(20, 165, 150, 20))
        self.label_3.setObjectName("label_3")

        self.lineEditCsv = QtWidgets.QLineEdit(LasTifToCsvDialogBase)
        self.lineEditCsv.setGeometry(QtCore.QRect(20, 190, 380, 30))
        self.lineEditCsv.setObjectName("lineEditCsv")

        self.pushButtonCsv = QtWidgets.QPushButton(LasTifToCsvDialogBase)
        self.pushButtonCsv.setGeometry(QtCore.QRect(410, 190, 80, 30))
        self.pushButtonCsv.setObjectName("pushButtonCsv")

        # ProgressBar
        self.progressBar = QtWidgets.QProgressBar(LasTifToCsvDialogBase)
        self.progressBar.setGeometry(QtCore.QRect(20, 250, 470, 25))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        # 実行ボタン
        self.pushButtonRun = QtWidgets.QPushButton(LasTifToCsvDialogBase)
        self.pushButtonRun.setGeometry(QtCore.QRect(310, 310, 80, 30))
        self.pushButtonRun.setObjectName("pushButtonRun")

        # キャンセルボタン
        self.pushButtonCancel = QtWidgets.QPushButton(LasTifToCsvDialogBase)
        self.pushButtonCancel.setGeometry(QtCore.QRect(410, 310, 80, 30))
        self.pushButtonCancel.setObjectName("pushButtonCancel")

        self.retranslateUi(LasTifToCsvDialogBase)

        self.pushButtonCancel.clicked.connect(
            LasTifToCsvDialogBase.reject
        )

        QtCore.QMetaObject.connectSlotsByName(
            LasTifToCsvDialogBase
        )

    def retranslateUi(self, LasTifToCsvDialogBase):

        _translate = QtCore.QCoreApplication.translate

        LasTifToCsvDialogBase.setWindowTitle(
            _translate(
                "LasTifToCsvDialogBase",
                "LAS/TIF to CSV"
            )
        )

        self.label.setText(
            _translate(
                "LasTifToCsvDialogBase",
                "LAS/LAZファイル"
            )
        )

        self.label_2.setText(
            _translate(
                "LasTifToCsvDialogBase",
                "GeoTIFFファイル"
            )
        )

        self.label_3.setText(
            _translate(
                "LasTifToCsvDialogBase",
                "CSV保存先"
            )
        )

        self.pushButtonLas.setText(
            _translate(
                "LasTifToCsvDialogBase",
                "参照"
            )
        )

        self.pushButtonTif.setText(
            _translate(
                "LasTifToCsvDialogBase",
                "参照"
            )
        )

        self.pushButtonCsv.setText(
            _translate(
                "LasTifToCsvDialogBase",
                "保存先"
            )
        )

        self.pushButtonRun.setText(
            _translate(
                "LasTifToCsvDialogBase",
                "実行"
            )
        )

        self.pushButtonCancel.setText(
            _translate(
                "LasTifToCsvDialogBase",
                "キャンセル"
            )
        )