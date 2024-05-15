from PySide6.QtCore import Qt, QEvent, QDate, QDataStream, QIODevice, QAbstractItemModel, QModelIndex, QAbstractTableModel
from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton, QCheckBox, QCalendarWidget, QTableWidget, QTableView
from PySide6.QtGui import QTextCharFormat, QStandardItemModel, QStandardItem

from ui_interface import Ui_MainWindow

import pyodbc as pyodbc

server = 'LAPTOP-Q7SJNQHU\SQLEXPRESS'
database = 'StyroPlanDB'

conn_str = (
    f'DRIVER={{SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


class Arrange_Table_Model(QStandardItemModel):

    def dropMimeData(self, data, action, row, col, parent):
        """
        Always move the entire row, and don't allow column "shifting"
        """
        response = super().dropMimeData(data, Qt.CopyAction, row, 0, parent)
        return response


class Custom_SQL_Table_Model(QAbstractTableModel):
    def __init__(self, data, header_data, parent=None):
        super().__init__(parent)
        self._data = data
        self._header_data = header_data

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        if self._data:
            return len(self._data[0])
        return 0

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        column = index.column()

        if role == Qt.DisplayRole:
            return str(self._data[row][column])

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return str(self._header_data[section])
        return None


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("StyroPlan")

        self.icon_only_widget.hide()
        self.stackedWidget.setCurrentIndex(0)   # First to be displayed is 'unplanned_orders'
        self.menu_unplanned_btn_2.setChecked(True)
        self.planlanmamis_combobox.setCurrentIndex(-1)
        self.planlanmamis_combobox.setCurrentText("Sırala")
        self.planlanmis_combobox.setCurrentIndex(-1)
        self.planlanmis_combobox.setCurrentText("Sırala")

        # Connecting buttons to pages
        self.menu_unplanned_btn.clicked.connect(self.change_page_to_unplanned_orders)
        self.menu_unplanned_btn_2.clicked.connect(self.change_page_to_unplanned_orders)
        self.menu_planned_btn.clicked.connect(self.change_page_to_planned_orders)
        self.menu_planned_btn_2.clicked.connect(self.change_page_to_planned_orders)
        self.menu_stock_btn.clicked.connect(self.change_page_to_stok_raporlari)
        self.menu_stock_btn_2.clicked.connect(self.change_page_to_stok_raporlari)
        self.planla_btn.clicked.connect(self.change_page_to_planned_orders)
        self.arrange_table_btn.clicked.connect(self.change_page_to_arrange_tables)
        self.kaydet_btn.clicked.connect(self.change_page_to_planned_orders)

        # Make filters invisible initially
        self.kalip_genisligi_check_boxes_2.setVisible(False)
        self.montaj_ihtiyac_calendar_widget_2.setVisible(False)
        self.kalip_genisligi_check_boxes.setVisible(False)
        self.makineler_check_boxes.setVisible(False)
        self.montaj_ihtiyac_calendar_widget.setVisible(False)
        self.type_check_boxes.setVisible(False)
        self.type_check_boxes_2.setVisible(False)

        # Hovering over filter buttons
        self.kalip_genisligi_widget_2.installEventFilter(self)
        self.kalip_genisligi_widget_2.setMouseTracking(True)

        self.kalip_genisligi_widget.installEventFilter(self)
        self.kalip_genisligi_widget.setMouseTracking(True)

        self.montaj_ihtiyac_widget_2.installEventFilter(self)
        self.montaj_ihtiyac_widget_2.setMouseTracking(True)

        self.montaj_ihtiyac_widget.installEventFilter(self)
        self.montaj_ihtiyac_widget.setMouseTracking(True)

        self.makineler_widget.installEventFilter(self)
        self.makineler_widget.setMouseTracking(True)

        self.type_widget_2.installEventFilter(self)
        self.type_widget_2.setMouseTracking(True)

        self.type_widget.installEventFilter(self)
        self.type_widget.setMouseTracking(True)

        # Implementing filtering
        self.uygula_btn_2.clicked.connect(self.get_selected_kalip_genisligi_2_checkboxes)
        self.uygula_btn_2.clicked.connect(self.get_search_input_2)
        self.uygula_btn_2.clicked.connect(self.get_selected_type_2_checkboxes)

        self.selected_dates_2 = []
        self.deselected_dates_2 = []
        self.calendarWidget_2.clicked.connect(self.toggled_date_selection_2)
        self.uygula_btn_2.clicked.connect(self.get_selected_dates_2)


        self.uygula_btn.clicked.connect(self.get_selected_kalip_genisligi_checkboxes)
        self.uygula_btn.clicked.connect(self.get_selected_makineler_checkboxes)
        self.uygula_btn.clicked.connect(self.get_search_input)
        self.uygula_btn.clicked.connect(self.get_selected_type_checkboxes)

        self.selected_dates = []
        self.deselected_dates = []
        self.calendarWidget.clicked.connect(self.toggled_date_selection)
        self.uygula_btn.clicked.connect(self.get_selected_dates)

        #Implementing sorting
        self.planlanmamis_combobox.currentTextChanged.connect(self.get_selected_order_planlanmamis)
        self.planlanmis_combobox.currentTextChanged.connect(self.get_selected_order_planlanmis)


        # Fill Unordered Table
        planlanmamis_table_column_names = ["Parça Kodu", "Sipariş Teslim Tarihi", "Cycle Time", "Kalıp Raf No.",
                                           "Erkek Kalıp Raf No.", "Type", "Kalıp Genişliği"]
        cursor.execute('''SELECT CAST(m.PARCA_KODU AS varchar(50)) AS PARCA_KODU, s.PTARIH, m.CYCLE_TIME, m.KALIP_RAF_NO, m.ERKEK_KALIP_RAF_NO, m.TYPE,  m.KALIP_GENISLIGI
FROM SAP_URT_SIP s
INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))
WHERE CAST(TYPE AS varchar(50)) = 'TOP' OR CAST(TYPE AS varchar(50)) = 'BOTTOM' OR CAST(TYPE AS varchar(50)) = 'MIDDLE' OR CAST(TYPE AS varchar(50)) = 'FRONT' OR CAST(TYPE AS varchar(50)) = 'BACK'
''')
        unordered_table_data = cursor.fetchall()
        for row in unordered_table_data:
            print(row)
        self.unordered_model = Custom_SQL_Table_Model(unordered_table_data, planlanmamis_table_column_names)
        self.tableView.setModel(self.unordered_model)


        #Fill Ordered Tables
        planlanmis_table_column_names = ["Sıra", "Parça Kodu", "Kalıp Raf No.", "Erkek Kalıp Raf No.", "Type",
                                         "Kalıp Genişliği", "Başlangıç Tarihi - Saati", "Bitiş Tarihi - Saati",
                                         "Gecikme"]
        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        kz_1_table_data = cursor.fetchall()
        for row in kz_1_table_data:
            print(row)
        self.kz_1_model = Custom_SQL_Table_Model(kz_1_table_data, planlanmis_table_column_names)
        self.KZ_1_table_view.setModel(self.kz_1_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        kz_2_table_data = cursor.fetchall()
        for row in kz_2_table_data:
            print(row)
        self.kz_2_model = Custom_SQL_Table_Model(kz_2_table_data, planlanmis_table_column_names)
        self.KZ_2_table_view.setModel(self.kz_2_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        kz_3_table_data = cursor.fetchall()
        for row in kz_3_table_data:
            print(row)
        self.kz_3_model = Custom_SQL_Table_Model(kz_3_table_data, planlanmis_table_column_names)
        self.KZ_3_table_view.setModel(self.kz_3_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        kz_4_table_data = cursor.fetchall()
        for row in kz_4_table_data:
            print(row)
        self.kz_4_model = Custom_SQL_Table_Model(kz_4_table_data, planlanmis_table_column_names)
        self.KZ_4_table_view.setModel(self.kz_4_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        kz_5_table_data = cursor.fetchall()
        for row in kz_5_table_data:
            print(row)
        self.kz_5_model = Custom_SQL_Table_Model(kz_5_table_data, planlanmis_table_column_names)
        self.KZ_5_table_view.setModel(self.kz_5_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        kz_6_table_data = cursor.fetchall()
        for row in kz_6_table_data:
            print(row)
        self.kz_6_model = Custom_SQL_Table_Model(kz_6_table_data, planlanmis_table_column_names)
        self.KZ_6_table_view.setModel(self.kz_6_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        kz_7_table_data = cursor.fetchall()
        for row in kz_7_table_data:
            print(row)
        self.kz_7_model = Custom_SQL_Table_Model(kz_7_table_data, planlanmis_table_column_names)
        self.KZ_7_table_view.setModel(self.kz_7_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        kz_8_table_data = cursor.fetchall()
        for row in kz_8_table_data:
            print(row)
        self.kz_8_model = Custom_SQL_Table_Model(kz_8_table_data, planlanmis_table_column_names)
        self.KZ_8_table_view.setModel(self.kz_8_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        kz_XL_1_table_data = cursor.fetchall()
        for row in kz_XL_1_table_data:
            print(row)
        self.kz_XL_1_model = Custom_SQL_Table_Model(kz_XL_1_table_data, planlanmis_table_column_names)
        self.KZ_XL_1_table_view.setModel(self.kz_XL_1_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        kz_XL_2_table_data = cursor.fetchall()
        for row in kz_XL_2_table_data:
            print(row)
        self.kz_XL_2_model = Custom_SQL_Table_Model(kz_XL_2_table_data, planlanmis_table_column_names)
        self.KZ_XL_2_table_view.setModel(self.kz_XL_2_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        kz_XL_3_table_data = cursor.fetchall()
        for row in kz_XL_3_table_data:
            print(row)
        self.kz_XL_3_model = Custom_SQL_Table_Model(kz_XL_3_table_data, planlanmis_table_column_names)
        self.KZ_XL_3_table_view.setModel(self.kz_XL_3_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        kz_XL_4_table_data = cursor.fetchall()
        for row in kz_XL_4_table_data:
            print(row)
        self.kz_XL_4_model = Custom_SQL_Table_Model(kz_XL_4_table_data, planlanmis_table_column_names)
        self.KZ_XL_4_table_view.setModel(self.kz_XL_4_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        ERL_1_table_data = cursor.fetchall()
        for row in ERL_1_table_data:
            print(row)
        self.ERL_1_model = Custom_SQL_Table_Model(ERL_1_table_data, planlanmis_table_column_names)
        self.ERL_1_table_view.setModel(self.ERL_1_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        ERL_2_table_data = cursor.fetchall()
        for row in ERL_2_table_data:
            print(row)
        self.ERL_2_model = Custom_SQL_Table_Model(ERL_2_table_data, planlanmis_table_column_names)
        self.ERL_2_table_view.setModel(self.ERL_2_model)

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, GOZ_SAYISI, KALIP_GENISLIGI FROM PLAN_MAKINELER")
        ERL_3_table_data = cursor.fetchall()
        for row in ERL_3_table_data:
            print(row)
        self.ERL_3_model = Custom_SQL_Table_Model(ERL_3_table_data, planlanmis_table_column_names)
        self.ERL_3_table_view.setModel(self.ERL_3_model)


        #Fill arrange tables
        arranged_table_column_names = ["Makine", "Parça Kodu", "Kalıp Raf No.", "Erkek Kalıp Raf No.", "Type",
                                       "Kalıp Genişliği"]

        cursor.execute("SELECT PARCA_KODU, PARCA_ADI, CYCLE_TIME, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE,  KALIP_GENISLIGI FROM PLAN_MAKINELER")
        arrange_table_data = cursor.fetchall()

        for row in arrange_table_data:
            print(row)

        # Allow table arranging by drag and drop
        self.arranged_table.setSelectionBehavior(QTableView.SelectRows)
        self.arranged_table.setSelectionMode(QTableView.SingleSelection)
        self.arranged_table.setDragDropMode(QTableView.InternalMove)
        self.arranged_table.setDragDropOverwriteMode(False)

        self.arranged_table_model = Arrange_Table_Model()
        self.arranged_table_model.setHorizontalHeaderLabels(arranged_table_column_names)

        for row in arrange_table_data:
            items = []
            for item in row:
                item = QStandardItem(str(item))
                item.setDropEnabled(False)
                items.append(item)
            self.arranged_table_model.appendRow(items)

        self.arranged_table.setModel(self.arranged_table_model)


        #Fill Stock Table
        stock_table_columns = ['Hafta', 'Hat', 'Operasyon Başlangıcı', 'İş Yükü', 'Ürün Kodu', 'Ürün Grubu', 'Orijinal Miktar', 'Bakiye Miktarı','Strafor Top Kodu', 'Strafor Top Tanımı', 'Strafor Top Stok', 'Strafor Bottom Kodu', 'Strafor Bottom Stok' ]
        cursor.execute("SELECT TOP 50 WERKS, MATNR, LABST,ERFMG,ERFMGCO1P, LBLAB,INSME,MIKTAR, MENGE, STOK, NAKIL, MENGEKONS, ERP_TABLE_NAME FROM SAP_STOK_BILGI")
        stock_table_data = cursor.fetchall()

        for row in stock_table_data:
            print(row)

        self.stock_model = Custom_SQL_Table_Model(stock_table_data, stock_table_columns)
        self.stok_tablosu.setModel(self.stock_model)

        conn.close()


    # Functions for changing pages
    def change_page_to_unplanned_orders(self):
        self.stackedWidget.setCurrentIndex(0)

    def change_page_to_planned_orders(self):
        if self.planla_btn.isChecked():
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.change_page_to_no_planned_order()

    def change_page_to_no_planned_order(self):
        self.stackedWidget.setCurrentIndex(2)

    def change_page_to_arrange_tables(self):
        self.stackedWidget.setCurrentIndex(3)

    def change_page_to_stok_raporlari(self):
        self.stackedWidget.setCurrentIndex(4)


    # For hovering on filter widgets
    def eventFilter(self, obj, ev):
        if ev.type() == QEvent.HoverEnter:
            for child in obj.findChildren(QPushButton):
                child.setStyleSheet("background-color: #EEEEEE;"
                                    "text-align:left;")

        elif ev.type() == QEvent.HoverLeave:
            for child in obj.findChildren(QPushButton):
                child.setStyleSheet("background-color: #fff;"
                                    "text-align:left;")

        return False

    def get_search_input_2(self):
        text = self.search_input_2.text()
        print("Searching for: ", text)

    def get_search_input(self):
        text = self.search_input.text()
        print("Searching for: ", text)

    def get_selected_kalip_genisligi_2_checkboxes(self):
        # Getting values as string
        selected_checkboxes = []

        if self.kalip_genisligi_checkBox_S_2.isChecked():
            selected_checkboxes.append(self.kalip_genisligi_checkBox_S_2.text())

        if self.kalip_genisligi_checkBox_M_2.isChecked():
            selected_checkboxes.append(self.kalip_genisligi_checkBox_M_2.text())

        if self.kalip_genisligi_checkBox_L_2.isChecked():
            selected_checkboxes.append(self.kalip_genisligi_checkBox_L_2.text())

        if self.kalip_genisligi_checkBox_ERL_2.isChecked():
            selected_checkboxes.append(self.kalip_genisligi_checkBox_ERL_2.text())

        print("Selected Kalip Genisligi Checkboxes:", selected_checkboxes)

    def get_selected_kalip_genisligi_checkboxes(self):
        # Getting values as string
        selected_checkboxes = []

        if self.kalip_genisligi_checkBox_S.isChecked():
            selected_checkboxes.append(self.kalip_genisligi_checkBox_S.text())

        if self.kalip_genisligi_checkBox_M.isChecked():
            selected_checkboxes.append(self.kalip_genisligi_checkBox_M.text())

        if self.kalip_genisligi_checkBox_L.isChecked():
            selected_checkboxes.append(self.kalip_genisligi_checkBox_L.text())

        if self.kalip_genisligi_checkBox_ERL.isChecked():
            selected_checkboxes.append(self.kalip_genisligi_checkBox_ERL.text())

        print("Selected Kalip Genisligi Checkboxes:", selected_checkboxes)

    def get_selected_makineler_checkboxes(self):
        # Getting values as string
        selected_checkboxes = []

        if self.makineler_checkBox_KZ_1.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_KZ_1.text())
        if self.makineler_checkBox_KZ_2.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_KZ_2.text())
        if self.makineler_checkBox_KZ_3.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_KZ_3.text())
        if self.makineler_checkBox_KZ_4.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_KZ_4.text())
        if self.makineler_checkBox_KZ_5.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_KZ_5.text())
        if self.makineler_checkBox_KZ_6.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_KZ_6.text())
        if self.makineler_checkBox_KZ_7.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_KZ_7.text())
        if self.makineler_checkBox_KZ_8.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_KZ_8.text())
        if self.makineler_checkBox_KZ_XL_1.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_KZ_XL_1.text())
        if self.makineler_checkBox_KZ_XL_2.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_KZ_XL_2.text())
        if self.makineler_checkBox_KZ_XL_3.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_KZ_XL_3.text())
        if self.makineler_checkBox_KZ_XL_4.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_KZ_XL_4.text())
        if self.makineler_checkBox_ERL_1.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_ERL_1.text())
        if self.makineler_checkBox_ERL_2.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_ERL_2.text())
        if self.makineler_checkBox_ERL_3.isChecked():
            selected_checkboxes.append(self.makineler_checkBox_ERL_3.text())

        print("Selected Makineler Checkboxes:", selected_checkboxes)

    def toggled_date_selection(self, date):
        if date in self.selected_dates:
            self.selected_dates.remove(date)
            self.deselected_dates.append(date)
        else:
            self.selected_dates.append(date)
            if date in self.deselected_dates:
                self.deselected_dates.remove(date)
        self.highlight_selected_dates()

    def highlight_selected_dates(self):
        selected_date_format = QTextCharFormat()
        selected_date_format.setBackground(Qt.gray)

        deselected_date_format = QTextCharFormat()
        deselected_date_format.setBackground(Qt.white)

        for date in self.selected_dates:
            self.calendarWidget.setDateTextFormat(date, selected_date_format)

        for date in self.deselected_dates:
            self.calendarWidget.setDateTextFormat(date, deselected_date_format)


    def get_selected_dates(self):
        print("Selected Dates:")
        for date in self.selected_dates:
            print(date.toString("yyyy-MM-dd"))

        print("Deselected Dates:")
        for date in self.deselected_dates:
            print(date.toString("yyyy-MM-dd"))

    # DO WE NEED THIS?
    def reset_calendar(self):
        for date in self.selected_dates:
            self.calendarWidget.setDateTextFormat(date, QTextCharFormat())
        self.calendarWidget.setSelectedDate(QDate.currentDate())
        self.selected_dates = []


    def toggled_date_selection_2(self, date):
        if date in self.selected_dates_2:
            self.selected_dates_2.remove(date)
            self.deselected_dates_2.append(date)
        else:
            self.selected_dates_2.append(date)
            if date in self.deselected_dates_2:
                self.deselected_dates_2.remove(date)
        self.highlight_selected_dates_2()

    def highlight_selected_dates_2(self):
        selected_date_format = QTextCharFormat()
        selected_date_format.setBackground(Qt.gray)

        deselected_date_format = QTextCharFormat()
        deselected_date_format.setBackground(Qt.white)

        for date in self.selected_dates_2:
            self.calendarWidget_2.setDateTextFormat(date, selected_date_format)

        for date in self.deselected_dates:
            self.calendarWidget_2.setDateTextFormat(date, deselected_date_format)

    def get_selected_dates_2(self):
        print("Selected Dates:")
        for date in self.selected_dates_2:
            print(date.toString("yyyy-MM-dd"))

        print("Deselected Dates:")
        for date in self.deselected_dates_2:
            print(date.toString("yyyy-MM-dd"))

    # DO WE NEED THIS?
    def reset_calendar_2(self):
        for date in self.selected_dates_2:
            self.calendarWidget_2.setDateTextFormat(date, QTextCharFormat())
        self.calendarWidget_2.setSelectedDate(QDate.currentDate())


    def get_selected_type_2_checkboxes(self):
        # Getting values as string NOTE: Might convert to uppercase depending on how it is stored on db
        selected_checkboxes = []

        if self.type_checkBox_top_2.isChecked():
            selected_checkboxes.append(self.type_checkBox_top_2.text())

        if self.type_checkBox_bottom_2.isChecked():
            selected_checkboxes.append(self.type_checkBox_bottom_2.text())

        if self.type_checkBox_middle_2.isChecked():
            selected_checkboxes.append(self.type_checkBox_middle_2.text())


        print("Selected Type Checkboxes:", selected_checkboxes)

    def get_selected_type_checkboxes(self):
        # Getting values as string
        selected_checkboxes = []

        if self.type_checkBox_top.isChecked():
            selected_checkboxes.append(self.type_checkBox_top.text())

        if self.type_checkBox_bottom_2.isChecked():
            selected_checkboxes.append(self.type_checkBox_bottom.text())

        if self.type_checkBox_middle_2.isChecked():
            selected_checkboxes.append(self.type_checkBox_middle.text())


        print("Selected Type Checkboxes:", selected_checkboxes)

    def get_selected_order_planlanmamis(self, value):
        print("Selected order for planlanmamis :", value)

    def get_selected_order_planlanmis(self, value):
        print("Selected order for planlanmis :", value)