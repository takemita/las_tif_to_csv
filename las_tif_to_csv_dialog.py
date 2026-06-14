# -*- coding: utf-8 -*-

from qgis.PyQt import QtWidgets
from qgis.PyQt.QtWidgets import QFileDialog, QMessageBox

from .las_tif_to_csv_dialog_base import Ui_LasTifToCsvDialogBase


class LasTifToCsvDialog(
        QtWidgets.QDialog,
        Ui_LasTifToCsvDialogBase):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        self.progressBar.setValue(0)

        self.pushButtonLas.clicked.connect(
            self.select_las
        )

        self.pushButtonTif.clicked.connect(
            self.select_tif
        )

        self.pushButtonCsv.clicked.connect(
            self.select_csv
        )

        self.pushButtonRun.clicked.connect(
            self.run_process
        )

    # --------------------------------------------------
    # LAS選択
    # --------------------------------------------------
    def select_las(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "LAS/LAZファイル選択",
            "",
            "LAS Files (*.las *.laz)"
        )

        if file_path:
            self.lineEditLas.setText(file_path)

    # --------------------------------------------------
    # GeoTIFF選択
    # --------------------------------------------------
    def select_tif(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "GeoTIFF選択",
            "",
            "GeoTIFF (*.tif *.tiff)"
        )

        if file_path:
            self.lineEditTif.setText(file_path)

    # --------------------------------------------------
    # CSV保存先
    # --------------------------------------------------
    def select_csv(self):

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "CSV保存先",
            "",
            "CSV Files (*.csv)"
        )

        if file_path:

            if not file_path.lower().endswith(".csv"):
                file_path += ".csv"

            self.lineEditCsv.setText(file_path)

    # --------------------------------------------------
    # 実行
    # --------------------------------------------------
    def run_process(self):

        try:

            import laspy
            import rasterio
            import pandas as pd
            import numpy as np

            las_file = self.lineEditLas.text().strip()
            tif_file = self.lineEditTif.text().strip()
            csv_file = self.lineEditCsv.text().strip()

            if not las_file:
                QMessageBox.warning(
                    self,
                    "入力エラー",
                    "LASファイルを選択してください"
                )
                return

            if not tif_file:
                QMessageBox.warning(
                    self,
                    "入力エラー",
                    "GeoTIFFを選択してください"
                )
                return

            if not csv_file:
                QMessageBox.warning(
                    self,
                    "入力エラー",
                    "CSV保存先を指定してください"
                )
                return

            self.progressBar.setValue(10)

            # --------------------------------
            # LAS読込
            # --------------------------------
            las = laspy.read(las_file)

            x = np.array(las.x)
            y = np.array(las.y)
            z = np.array(las.z)

            total = len(x)

            self.progressBar.setValue(20)

            # --------------------------------
            # RGB GeoTIFF読込
            # --------------------------------
            with rasterio.open(tif_file) as src:

                if src.count < 3:

                    raise Exception(
                        f"RGB GeoTIFFではありません "
                        f"(Band数={src.count})"
                    )

                red_band = src.read(1)
                green_band = src.read(2)
                blue_band = src.read(3)

                height = red_band.shape[0]
                width = red_band.shape[1]

                r_list = []
                g_list = []
                b_list = []

                for i in range(total):

                    try:

                        row, col = src.index(
                            float(x[i]),
                            float(y[i])
                        )

                        if (
                            0 <= row < height and
                            0 <= col < width
                        ):

                            r = int(
                                red_band[row, col]
                            )

                            g = int(
                                green_band[row, col]
                            )

                            b = int(
                                blue_band[row, col]
                            )

                        else:

                            r = 0
                            g = 0
                            b = 0

                    except Exception:

                        r = 0
                        g = 0
                        b = 0

                    r_list.append(r)
                    g_list.append(g)
                    b_list.append(b)

                    if i % 10000 == 0:

                        progress = (
                            20 +
                            int(
                                (i / total) * 75
                            )
                        )

                        self.progressBar.setValue(
                            progress
                        )

            self.progressBar.setValue(95)

            # --------------------------------
            # CSV出力
            # --------------------------------
            df = pd.DataFrame({

                "X": x,
                "Y": y,
                "Z": z,

                "R": r_list,
                "G": g_list,
                "B": b_list

            })

            df.to_csv(
                csv_file,
                index=False,
                encoding="utf-8-sig"
            )

            self.progressBar.setValue(100)

            QMessageBox.information(
                self,
                "完了",
                f"CSV出力完了\n\n"
                f"{csv_file}\n\n"
                f"点群数 : {len(df):,}"
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "エラー",
                str(e)
            )