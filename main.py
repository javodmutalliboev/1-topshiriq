import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QCheckBox,
    QComboBox,
    QRadioButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="javod",
    password="hHh(26Y2%C~w",
    database="n106_5_oy_sakkiz_dars_hw_bir",
)

cursor = conn.cursor()


class TalabalarRoyxati(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Talabalar ro'yxatini boshqarish tizimi")

        v_layout = QVBoxLayout()

        self.ism = QLineEdit()
        self.ism.setPlaceholderText("Ism kiriting")
        v_layout.addWidget(self.ism)

        h_layout = QHBoxLayout()
        fakultet_label = QLabel("Fakultet tanlang:")
        h_layout.addWidget(fakultet_label)
        self.fakultet_combo_box = QComboBox()
        h_layout.addWidget(self.fakultet_combo_box)
        self.fakultetlarni_yuklash()

        h_layout_2 = QHBoxLayout()
        jins_label = QLabel("Jinsi:")
        h_layout_2.addWidget(jins_label)
        self.jins_erkak = QRadioButton()
        erkak_label = QLabel("erkak")
        h_layout_2.addWidget(self.jins_erkak)
        h_layout_2.addWidget(erkak_label)
        self.jins_ayol = QRadioButton()
        ayol_label = QLabel("ayol")
        h_layout_2.addWidget(self.jins_ayol)
        h_layout_2.addWidget(ayol_label)

        h_layout_3 = QHBoxLayout()
        faol_label = QLabel("Faol:")
        h_layout_3.addWidget(faol_label)
        self.faol_checkbox = QCheckBox()
        h_layout_3.addWidget(self.faol_checkbox)

        talaba_qoshish_button = QPushButton("Talaba qo'shish")
        talaba_qoshish_button.clicked.connect(self.talaba_qoshish)
        talaba_update_button = QPushButton("Tanlangan talabani update qilish")
        right_join_button = QPushButton("RIGHT JOIN")
        right_join_button.clicked.connect(self.right_join)
        talaba_update_button.clicked.connect(self.talaba_update)
        talaba_delete_button = QPushButton("Tanlangan talabani o'chirish")
        talaba_delete_button.clicked.connect(self.delete_talaba)
        reset_button = QPushButton("Reset")
        reset_button.clicked.connect(self.reset)
        full_outer_join_button = QPushButton("FULL OUTER JOIN")
        full_outer_join_button.clicked.connect(self.full_outer_join)

        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_layout_2)
        v_layout.addLayout(h_layout_3)
        h_layout_4 = QHBoxLayout()
        h_layout_4.addWidget(talaba_qoshish_button)
        h_layout_4.addWidget(talaba_update_button)
        h_layout_4.addWidget(right_join_button)
        v_layout.addLayout(h_layout_4)

        h_layout_5 = QHBoxLayout()
        h_layout_5.addWidget(talaba_delete_button)
        h_layout_5.addWidget(reset_button)
        h_layout_5.addWidget(full_outer_join_button)
        v_layout.addLayout(h_layout_5)

        h_layout_6 = QHBoxLayout()
        search_label = QLabel("Search:")
        self.search_line_edit = QLineEdit()
        self.search_line_edit.setPlaceholderText("Enter search text")
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search)
        h_layout_6.addWidget(search_label)
        h_layout_6.addWidget(self.search_line_edit)
        h_layout_6.addWidget(search_button)
        v_layout.addLayout(h_layout_6)

        h_layout_7 = QHBoxLayout()
        distinct_button = QPushButton("DISTINCT")
        distinct_button.clicked.connect(self.distinct)
        count_button = QPushButton("COUNT")
        count_button.clicked.connect(self.count)
        length_button = QPushButton("LENGTH")
        length_button.clicked.connect(self.length)
        length_kichik5_button = QPushButton("LENGTH < 5")
        length_kichik5_button.clicked.connect(self.length_kichik5)
        order_by_ism_asc_button = QPushButton("ORDER BY ism ASC")
        order_by_ism_asc_button.clicked.connect(self.oreder_by_ism_asc)
        order_by_ism_desc_button = QPushButton("ORDER BY ism DESC")
        order_by_ism_desc_button.clicked.connect(self.oreder_by_ism_desc)
        max_button = QPushButton("MAX")
        max_button.clicked.connect(self.max)
        h_layout_7.addWidget(distinct_button)
        h_layout_7.addWidget(count_button)
        h_layout_7.addWidget(length_button)
        h_layout_7.addWidget(length_kichik5_button)
        h_layout_7.addWidget(order_by_ism_asc_button)
        h_layout_7.addWidget(order_by_ism_desc_button)
        h_layout_7.addWidget(max_button)
        v_layout.addLayout(h_layout_7)

        self.table = QTableWidget()
        self.table.cellClicked.connect(self.select_talaba)
        v_layout.addWidget(self.table)

        self.setLayout(v_layout)

        self.setStyleSheet(
            """
                QWidget {
                    font-size: 22px;
                }
                
                QPushButton:focus {
                    background-color: lightblue;
                }
            """
        )

        self.yuklash()

    def full_outer_join(self):
        try:
            cursor.execute(
                "SELECT t.id, t.ism, f.nomi, t.jins, t.faol \
                    FROM fakultet f LEFT JOIN talaba t \
                        ON f.id = t.fakultet_id \
                            UNION SELECT t.id, t.ism, f.nomi, t.jins, t.faol \
                                FROM fakultet f RIGHT JOIN talaba t \
                                    ON f.id = t.fakultet_id;"
            )
            self.table_ni_qurish()

        except Exception as exp:
            print(exp)

    def right_join(self):
        try:
            cursor.execute(
                "SELECT t.id, t.ism, f.nomi, t.jins, t.faol \
                    FROM fakultet f RIGHT JOIN talaba t ON f.id = t.fakultet_id;"
            )
            self.table_ni_qurish()

        except Exception as exp:
            print(exp)

    def max(self):
        try:
            cursor.execute(
                "SELECT nomi, soni FROM \
                    (SELECT f.nomi, COUNT(t.id) AS soni \
                        FROM talaba t \
                            INNER JOIN fakultet f ON\
                                  t.fakultet_id = f.id GROUP BY f.nomi) AS td \
                                    WHERE soni = (SELECT MAX(soni) FROM \
                                        (SELECT COUNT(t.id) AS soni FROM talaba t \
                                            INNER JOIN fakultet f ON t.fakultet_id = f.id \
                                                GROUP BY f.nomi) AS subquery );"
            )
            self.table_ni_qurish(mode="max")
        except Exception as exp:
            print(exp)

    def oreder_by_ism_asc(self):
        try:
            cursor.execute(
                "SELECT t.id, t.ism, f.nomi, t.jins, \
                      t.faol FROM talaba AS t INNER JOIN \
                          fakultet AS f ON t.fakultet_id = f.id ORDER BY t.ism ASC;"
            )
            self.table_ni_qurish()

        except Exception as exp:
            print(exp)

    def oreder_by_ism_desc(self):
        try:
            cursor.execute(
                "SELECT t.id, t.ism, f.nomi, t.jins, \
                      t.faol FROM talaba AS t INNER JOIN \
                          fakultet AS f ON t.fakultet_id = f.id ORDER BY t.ism DESC;"
            )
            self.table_ni_qurish()

        except Exception as exp:
            print(exp)

    def length(self):
        try:
            cursor.execute(
                "SELECT t.ism, LENGTH(t.ism) uzunligi FROM talaba t GROUP BY t.ism;"
            )
            self.table_ni_qurish(mode="length")
        except Exception as exp:
            print(exp)

    def length_kichik5(self):
        try:
            cursor.execute(
                "SELECT t.ism, LENGTH(t.ism) uzunligi FROM talaba t WHERE \
                     LENGTH(t.ism)<5 GROUP BY t.ism;"
            )
            self.table_ni_qurish(mode="length")
        except Exception as exp:
            print(exp)

    def count(self):
        try:
            cursor.execute(
                "SELECT f.nomi, COUNT(t.id) soni FROM talaba t \
                      INNER JOIN fakultet f ON t.fakultet_id=f.id GROUP BY f.nomi;"
            )
            self.table_ni_qurish(mode="count")
        except Exception as exp:
            print(exp)

    def distinct(self):
        try:
            cursor.execute(
                "SELECT DISTINCT t.ism, f.nomi FROM talaba t INNER JOIN fakultet f ON t.fakultet_id=f.id;"
            )
            self.table_ni_qurish(mode="distinct")
        except Exception as exp:
            print(exp)

    def search(self):
        try:
            search_text = self.search_line_edit.text()
            cursor.execute(
                "SELECT t.id, t.ism, f.nomi, t.jins, t.faol \
                      FROM talaba AS t INNER JOIN fakultet AS f \
                          ON t.fakultet_id = f.id WHERE t.ism LIKE %s \
                              OR f.nomi LIKE %s OR t.jins LIKE %s;",
                ("%" + search_text + "%",) * 3,
            )
            self.table_ni_qurish()
        except Exception as exp:
            print(exp)

    def reset(self):
        self.ism.clear()
        self.fakultet_combo_box.setCurrentText("<fakultet tanlang>")

        self.jins_erkak.setAutoExclusive(False)
        self.jins_ayol.setAutoExclusive(False)

        self.jins_erkak.setChecked(False)
        self.jins_ayol.setChecked(False)

        self.jins_erkak.setAutoExclusive(True)
        self.jins_ayol.setAutoExclusive(True)

        self.faol_checkbox.setChecked(False)
        self.yuklash()

    def delete_talaba(self):
        try:
            id = self.getTableRowID()
            cursor.execute("DELETE FROM talaba WHERE id=%s", (id,))
            conn.commit()
            self.reset()

        except Exception as exp:
            print(exp)

    def getTableRowID(self):
        try:
            row_idx = self.table.currentRow()
            id = int(self.table.item(row_idx, 0).text())
            return id
        except Exception as exp:
            print(exp)

    def talaba_update(self):
        try:
            id = self.getTableRowID()
            ism = self.ism.text()
            fakultet = (
                None
                if self.fakultet_combo_box.currentText() == "<fakultet tanlang>"
                else self.fakultetlar[self.fakultet_combo_box.currentText()]
            )
            jins = (
                "erkak"
                if self.jins_erkak.isChecked()
                else "ayol" if self.jins_ayol.isChecked() else None
            )
            faol = self.faol_checkbox.isChecked()

            if not ism or not jins:
                QMessageBox.warning(
                    self, "invalid input", "ism va jins kiritilishi kerak"
                )
                return

            cursor.execute(
                "UPDATE talaba SET ism=%s, jins=%s, faol=%s, fakultet_id=%s WHERE id=%s",
                (ism, jins, faol, fakultet, id),
            )
            conn.commit()
            self.reset()

        except Exception as exp:
            print(exp)

    def select_talaba(self, row, column):
        id = int(self.table.item(row, 0).text())
        ism = self.table.item(row, 1).text()
        fakultet = self.table.item(row, 2).text()
        jins = self.table.item(row, 3).text()
        faol = (
            True
            if self.table.item(row, 4).text() == "True"
            else False if self.table.item(row, 4).text() == "False" else None
        )
        self.ism.setText(ism)
        self.fakultet_combo_box.setCurrentText(fakultet)
        (
            self.jins_erkak.setChecked(True)
            if jins == "erkak"
            else self.jins_ayol.setChecked(True) if jins == "ayol" else None
        )
        self.faol_checkbox.setChecked(faol)

    def table_ni_qurish(self, mode=None):
        if mode == "count":
            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels(["Fakultet nomi", "Talabalar soni"])
        elif mode == "length":
            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels(
                ["Talaba ismi", "Talaba ismi uzunligi"]
            )
        elif mode == "max":
            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels(
                ["Talabalari soni eng ko'p fakultet nomi", "Talabalari soni"]
            )
        else:
            self.table.setColumnCount(5)
            self.table.setHorizontalHeaderLabels(
                ["IDsi", "Ismi", "Fakulteti", "Jinsi", "Faolligi"]
            )
        self.table.setRowCount(0)
        if mode == "distinct":
            for row_idx, (t_ism, t_fakultet) in enumerate(cursor.fetchall()):
                self.table.insertRow(row_idx)
                self.table.setItem(row_idx, 1, QTableWidgetItem(t_ism))
                self.table.setItem(row_idx, 2, QTableWidgetItem(t_fakultet))
        elif mode == "count":
            for row_idx, (fakultet_nomi, t_soni) in enumerate(cursor.fetchall()):
                self.table.insertRow(row_idx)
                self.table.setItem(row_idx, 0, QTableWidgetItem(fakultet_nomi))
                self.table.setItem(row_idx, 1, QTableWidgetItem(str(t_soni)))
        elif mode == "length":
            for row_idx, (t_ismi, ti_uzunligi) in enumerate(cursor.fetchall()):
                self.table.insertRow(row_idx)
                self.table.setItem(row_idx, 0, QTableWidgetItem(t_ismi))
                self.table.setItem(row_idx, 1, QTableWidgetItem(str(ti_uzunligi)))
        elif mode == "max":
            for row_idx, (f_nomi, t_soni) in enumerate(cursor.fetchall()):
                self.table.insertRow(row_idx)
                self.table.setItem(row_idx, 0, QTableWidgetItem(f_nomi))
                self.table.setItem(row_idx, 1, QTableWidgetItem(str(t_soni)))
        else:
            for row_idx, (t_id, t_ism, t_fakultet, t_jins, t_faol) in enumerate(
                cursor.fetchall()
            ):
                self.table.insertRow(row_idx)
                self.table.setItem(
                    row_idx,
                    0,
                    QTableWidgetItem(
                        str(t_id) if t_id else str(t_id) if t_id == 0 else ""
                    ),
                )
                self.table.setItem(row_idx, 1, QTableWidgetItem(t_ism))
                self.table.setItem(row_idx, 2, QTableWidgetItem(t_fakultet))
                self.table.setItem(row_idx, 3, QTableWidgetItem(t_jins))
                self.table.setItem(
                    row_idx,
                    4,
                    QTableWidgetItem(
                        str(bool(t_faol))
                        if t_faol == 0
                        else str(bool(t_faol)) if t_faol == 1 else ""
                    ),
                )

    def yuklash(self):
        try:
            cursor.execute(
                "SELECT t.id, t.ism, f.nomi, t.jins, \
                      t.faol FROM talaba AS t INNER JOIN \
                          fakultet AS f ON t.fakultet_id = f.id;"
            )
            self.table_ni_qurish()

        except Exception as exp:
            print(exp)

    def talaba_qoshish(self):
        try:
            ism = self.ism.text()
            fakultet = (
                None
                if self.fakultet_combo_box.currentText() == "<fakultet tanlang>"
                else self.fakultetlar[self.fakultet_combo_box.currentText()]
            )
            if self.jins_erkak.isChecked():
                jins = "erkak"
            elif self.jins_ayol.isChecked():
                jins = "ayol"
            else:
                jins = None
            faol = self.faol_checkbox.isChecked()

            if not ism or not jins:
                QMessageBox.warning(
                    self, "invalid input", "ism va jins kiritilishi kerak"
                )
                return

            cursor.execute(
                "INSERT INTO talaba (ism, jins, faol, fakultet_id) \
                    VALUES (%s, %s, %s, %s);",
                (ism, jins, faol, fakultet),
            )
            conn.commit()
            self.reset()

        except Exception as exp:
            print(exp)

    def fakultetlarni_yuklash(self):
        try:
            cursor.execute("SELECT * FROM fakultet")
            self.fakultetlar = {}
            for f_id, f_nomi in cursor.fetchall():
                self.fakultetlar[f_nomi] = f_id
            self.fakultet_combo_box.addItem("<fakultet tanlang>")
            self.fakultet_combo_box.addItems(self.fakultetlar.keys())
        except Exception as exp:
            print(exp)


def main():
    app = QApplication(sys.argv)
    window = TalabalarRoyxati()
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
