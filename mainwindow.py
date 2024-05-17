from PySide6.QtCore import Qt, QEvent, QDate, QDataStream, QIODevice, QAbstractItemModel, QModelIndex, \
    QAbstractTableModel
from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton, QCheckBox, QCalendarWidget, QTableWidget, QTableView
from PySide6.QtGui import QTextCharFormat, QStandardItemModel, QStandardItem

from genetic_algorithm import *
from greedy_algorithm import *
from ui_interface import Ui_MainWindow
import pandas as pd
from openpyxl.workbook import Workbook

import pyodbc as pyodbc
from job_creator.jobsFromDb import *

server = 'localhost\\SQLEXPRESS'
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
        self.stackedWidget.setCurrentIndex(0)  # First to be displayed is 'unplanned_orders'
        self.menu_unplanned_btn_2.setChecked(True)


        self.init_machine_table_data()

        # Connecting buttons to pages
        self.menu_unplanned_btn.clicked.connect(self.change_page_to_unplanned_orders)
        self.menu_unplanned_btn_2.clicked.connect(self.change_page_to_unplanned_orders)
        self.menu_planned_btn.clicked.connect(self.change_page_to_planned_orders)
        self.menu_planned_btn_2.clicked.connect(self.change_page_to_planned_orders)
        self.menu_stock_btn.clicked.connect(self.change_page_to_stok_raporlari)
        self.menu_stock_btn_2.clicked.connect(self.change_page_to_stok_raporlari)
        self.planla_btn.clicked.connect(self.change_page_to_planned_orders)
        self.planla_counter = 0
        self.arrange_table_btn.clicked.connect(self.change_page_to_arrange_tables)
        self.kaydet_btn.clicked.connect(self.export_to_excel)

        # Make filters invisible initially
        self.kalip_genisligi_check_boxes_2.setVisible(False)
        self.montaj_ihtiyac_calendar_widget_2.setVisible(False)
        self.kalip_genisligi_check_boxes.setVisible(False)
        self.makineler_check_boxes.setVisible(False)
        self.type_check_boxes.setVisible(False)
        self.type_check_boxes_2.setVisible(False)

        # Make machines filter checkboxes checked initially
        self.makineler_checkBox_KZ_1.setChecked(True)
        self.makineler_checkBox_KZ_2.setChecked(True)
        self.makineler_checkBox_KZ_3.setChecked(True)
        self.makineler_checkBox_KZ_4.setChecked(True)
        self.makineler_checkBox_KZ_5.setChecked(True)
        self.makineler_checkBox_KZ_6.setChecked(True)
        self.makineler_checkBox_KZ_7.setChecked(True)
        self.makineler_checkBox_KZ_8.setChecked(True)
        self.makineler_checkBox_KZ_XL_1.setChecked(True)
        self.makineler_checkBox_KZ_XL_2.setChecked(True)
        self.makineler_checkBox_KZ_XL_3.setChecked(True)
        self.makineler_checkBox_KZ_XL_4.setChecked(True)
        self.makineler_checkBox_ERL_1.setChecked(True)
        self.makineler_checkBox_ERL_2.setChecked(True)
        self.makineler_checkBox_ERL_3.setChecked(True)

        # Hovering over filter buttons
        self.kalip_genisligi_widget_2.installEventFilter(self)
        self.kalip_genisligi_widget_2.setMouseTracking(True)

        self.kalip_genisligi_widget.installEventFilter(self)
        self.kalip_genisligi_widget.setMouseTracking(True)

        self.montaj_ihtiyac_widget_2.installEventFilter(self)
        self.montaj_ihtiyac_widget_2.setMouseTracking(True)

        self.makineler_widget.installEventFilter(self)
        self.makineler_widget.setMouseTracking(True)

        self.type_widget_2.installEventFilter(self)
        self.type_widget_2.setMouseTracking(True)

        self.type_widget.installEventFilter(self)
        self.type_widget.setMouseTracking(True)

        # Implementing filtering
        self.selected_dates_2 = []
        self.deselected_dates_2 = []
        self.calendarWidget_2.clicked.connect(self.toggled_date_selection_2)
        self.uygula_btn_2.clicked.connect(self.get_unplanned_filter_results)

        #self.uygula_btn_2.clicked.connect(self.get_selected_kalip_genisligi_2_checkboxes)
        #self.uygula_btn_2.clicked.connect(self.get_search_input_2)
        #self.uygula_btn_2.clicked.connect(self.get_selected_type_2_checkboxes)

        self.uygula_btn.clicked.connect(self.update_table_models)




        # Fill Unordered Table
        planlanmamis_table_column_names = ["Parça Kodu", "Sipariş Teslim Tarihi", "Cycle Time", "Kalıp Raf No.",
                                           "Erkek Kalıp Raf No.", "Type", "Kalıp Genişliği"]
        cursor.execute('''SELECT TOP 50 CAST(m.PARCA_KODU AS varchar(50)) AS PARCA_KODU, s.PTARIH, m.CYCLE_TIME, m.KALIP_RAF_NO, m.ERKEK_KALIP_RAF_NO, m.TYPE,  m.KALIP_GENISLIGI
FROM SAP_URT_SIP s
INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))
WHERE CAST(TYPE AS varchar(50)) = 'TOP' OR CAST(TYPE AS varchar(50)) = 'BOTTOM' OR CAST(TYPE AS varchar(50)) = 'MIDDLE' OR CAST(TYPE AS varchar(50)) = 'FRONT' OR CAST(TYPE AS varchar(50)) = 'BACK'
ORDER BY CAST(s.AUFNR AS varchar(50)) ASC''')
        unordered_table_data = cursor.fetchall()
        for row in unordered_table_data:
            print(row)
        self.unordered_model = Custom_SQL_Table_Model(unordered_table_data, planlanmamis_table_column_names)
        self.tableView.setModel(self.unordered_model)

        #Fill Ordered Tables
        self.planlanmis_table_column_names = ["Sıra", "Parça Kodu", "Kalıp Raf No.", "Erkek Kalıp Raf No.", "Type",
                                         "Kalıp Genişliği", "Başlangıç Tarihi - Saati", "Bitiş Tarihi - Saati",
                                         "Gecikme"]

        self.kz_1_model = Custom_SQL_Table_Model(self.machine_table_data_kz.get(0, []), self.planlanmis_table_column_names)
        self.KZ_1_table_view.setModel(self.kz_1_model)

        self.kz_2_model = Custom_SQL_Table_Model(self.machine_table_data_kz.get(1, []), self.planlanmis_table_column_names)
        self.KZ_2_table_view.setModel(self.kz_2_model)

        self.kz_3_model = Custom_SQL_Table_Model(self.machine_table_data_kz.get(2, []), self.planlanmis_table_column_names)
        self.KZ_3_table_view.setModel(self.kz_3_model)

        self.kz_4_model = Custom_SQL_Table_Model(self.machine_table_data_kz.get(3, []), self.planlanmis_table_column_names)
        self.KZ_4_table_view.setModel(self.kz_4_model)

        self.kz_5_model = Custom_SQL_Table_Model(self.machine_table_data_kz.get(4, []), self.planlanmis_table_column_names)
        self.KZ_5_table_view.setModel(self.kz_5_model)

        self.kz_6_model = Custom_SQL_Table_Model(self.machine_table_data_kz.get(5, []), self.planlanmis_table_column_names)
        self.KZ_6_table_view.setModel(self.kz_6_model)

        self.kz_7_model = Custom_SQL_Table_Model(self.machine_table_data_kz.get(6, []), self.planlanmis_table_column_names)
        self.KZ_7_table_view.setModel(self.kz_7_model)

        self.kz_8_model = Custom_SQL_Table_Model(self.machine_table_data_kz.get(7, []), self.planlanmis_table_column_names)
        self.KZ_8_table_view.setModel(self.kz_8_model)

        self.kz_XL_1_model = Custom_SQL_Table_Model(self.machine_table_data_xl.get(0, []),
                                                    self.planlanmis_table_column_names)
        self.KZ_XL_1_table_view.setModel(self.kz_XL_1_model)

        self.kz_XL_2_model = Custom_SQL_Table_Model(self.machine_table_data_xl.get(1, []),
                                                    self.planlanmis_table_column_names)
        self.KZ_XL_2_table_view.setModel(self.kz_XL_2_model)

        self.kz_XL_3_model = Custom_SQL_Table_Model(self.machine_table_data_xl.get(2, []),
                                                   self.planlanmis_table_column_names)
        self.KZ_XL_3_table_view.setModel(self.kz_XL_3_model)

        self.kz_XL_4_model = Custom_SQL_Table_Model(self.machine_table_data_xl.get(3, []),
                                                    self.planlanmis_table_column_names)
        self.KZ_XL_4_table_view.setModel(self.kz_XL_4_model)

        self.ERL_1_model = Custom_SQL_Table_Model(self.machine_table_data_erl.get(0, []), self.planlanmis_table_column_names)
        self.ERL_1_table_view.setModel(self.ERL_1_model)

        self.ERL_2_model = Custom_SQL_Table_Model(self.machine_table_data_kz.get(1, []), self.planlanmis_table_column_names)
        self.ERL_2_table_view.setModel(self.ERL_2_model)

        self.ERL_3_model = Custom_SQL_Table_Model(self.machine_table_data_kz.get(2, []), self.planlanmis_table_column_names)
        self.ERL_3_table_view.setModel(self.ERL_3_model)

        #Fill arrange tables
        self.arranged_table_column_names = ["Makine", "Parça Kodu", "Kalıp Raf No.", "Erkek Kalıp Raf No.", "Type",
                                       "Kalıp Genişliği", "Başlangıç Tarihi - Saati", "Bitiş Tarihi - Saati", "Gecikme"]



        # Allow table arranging by drag and drop
        self.arranged_table.setSelectionBehavior(QTableView.SelectRows)
        self.arranged_table.setSelectionMode(QTableView.SingleSelection)
        self.arranged_table.setDragDropMode(QTableView.InternalMove)
        self.arranged_table.setDragDropOverwriteMode(False)

        self.arranged_table_model = Arrange_Table_Model()

        self.arranged_table_model.setHorizontalHeaderLabels(self.arranged_table_column_names)

        table_names = [self.machine_table_data_kz.get(0, []), self.machine_table_data_kz.get(1, []), self.machine_table_data_kz.get(2,[]), self.machine_table_data_kz.get(3,[]),
                       self.machine_table_data_kz.get(4,[]), self.machine_table_data_kz.get(5,[]), self.machine_table_data_kz.get(6,[]), self.machine_table_data_kz.get(7,[]),
                       self.machine_table_data_xl.get(0, []), self.machine_table_data_xl.get(1, []), self.machine_table_data_xl.get(2, []), self.machine_table_data_xl.get(3, []),
                       self.machine_table_data_erl.get(0, []), self.machine_table_data_erl.get(1, []), self.machine_table_data_erl.get(2, [])]

        empty_row_values = ['KZ-1', 'KZ-2', 'KZ-3', 'KZ-4','KZ-5', 'KZ-6', 'KZ-7', 'KZ-8', 'KZ-XL-1', 'KZ-XL-2', 'KZ-XL-3', 'KZ-XL-4',
                            'ERL-1', 'ERL-2', 'ERL-3']



        # Iterate through each table
        for i, table_name in enumerate(table_names):
            # Add an empty row before adding rows from each table
            empty_row = [QStandardItem(empty_row_values[i]) if index == 0 else QStandardItem('') for index in
                         range(len(self.arranged_table_column_names))]
            for item in empty_row:
                item.setDropEnabled(False)
            self.arranged_table_model.appendRow(empty_row)


            table_data = table_name

            # Iterate through rows of the current table data
            for row in table_data:
                items = []
                for item in row:
                    item = QStandardItem(str(item))
                    item.setDropEnabled(False)
                    items.append(item)
                self.arranged_table_model.appendRow(items)

        self.arranged_table.setModel(self.arranged_table_model)

        #Fill Stock Table
        stock_table_columns = ['Hafta', 'Hat', 'Operasyon Başlangıcı', 'İş Yükü', 'Ürün Kodu', 'Bakiye Miktarı', 'Strafor Top Kodu', 'Strafor Top Tanımı',
                               'Strafor Top Stok', 'Strafor Bottom Kodu', 'Strafor Bottom Stok']
        cursor.execute('''SELECT Hafta, Hat, Operasyon_Başlangıcı, İş_Yükü, Ürün_Kodu, Bakiye_Miktarı, Strafor_Top_Kodu, Strafor_Top_Tanımı,
                               Strafor_Top_Stok, Strafor_Bottom_Kodu, Strafor_Bottom_Stok FROM SUFFICIENCY_REPORT''')
        stock_table_data = cursor.fetchall()

        for row in stock_table_data:
            print(row)

        self.stock_model = Custom_SQL_Table_Model(stock_table_data, stock_table_columns)
        self.stok_tablosu.setModel(self.stock_model)

        #conn.close()

    def init_machine_table_data(self):
        # Initialize machine table data
        best_solution_xl, job_times_xl, tardiness_xl = genetic_algorithm(population_size, mutation_rate, max_generations,
                                                           num_machines_xl,
                                                           jobs_xl, calculate_setup_time_change_XL)
        final_solution_xl, job_times_greedy_xl_, total_tardiness_xl = greedy_algorithm(jobs_xl, machines_xl, calculate_setup_time_change_XL)

        if tardiness_xl <= total_tardiness_xl:
            organized_jobs_xl = self.organize_jobs_by_machine(best_solution_xl, job_times_xl)
            self.machine_table_data_xl = self.prepare_machine_table_data(organized_jobs_xl, jobs_list_xl)
        else:
            organized_jobs_xl = self.organize_jobs_by_machine(final_solution_xl, job_times_greedy_xl)
            self.machine_table_data_xl = self.prepare_machine_table_data(organized_jobs_xl, jobs_list_xl)


        best_solution_kz, job_times_kz, tardiness_kz = genetic_algorithm(population_size, mutation_rate, max_generations,
                                                           num_machines_kz,
                                                           jobs_kz, calculate_setup_time_change_KZ)
        final_solution_kz, job_times_greedy_kz, total_tardiness_kz = greedy_algorithm(jobs_kz, machines_kz, calculate_setup_time_change_KZ)

        if tardiness_kz <= total_tardiness_kz:
            organized_jobs_kz = self.organize_jobs_by_machine(best_solution_kz, job_times_kz)
            self.machine_table_data_kz = self.prepare_machine_table_data(organized_jobs_kz, jobs_list_kz)
        else:
            organized_jobs_kz = self.organize_jobs_by_machine(final_solution_kz, job_times_greedy_kz)
            self.machine_table_data_kz = self.prepare_machine_table_data(organized_jobs_kz, jobs_list_kz)


        best_solution_erl, job_times_erl, tardiness_erl = genetic_algorithm(population_size, mutation_rate, max_generations,
                                                             num_machines_erl,
                                                             jobs_erl, calculate_setup_time_change_ERL)
        final_solution_erl, job_times_greedy_erl, total_tardiness_erl = greedy_algorithm(jobs_erl, machines_erl, calculate_setup_time_change_ERL)
        if tardiness_erl <= total_tardiness_erl:
            organized_jobs_erl = self.organize_jobs_by_machine(best_solution_erl, job_times_erl)
            self.machine_table_data_erl = self.prepare_machine_table_data(organized_jobs_erl, jobs_list_erl)
        else:
            organized_jobs_erl = self.organize_jobs_by_machine(final_solution_erl, job_times_greedy_erl)
            self.machine_table_data_erl = self.prepare_machine_table_data(organized_jobs_erl, jobs_list_erl)



    def organize_jobs_by_machine(self, solution, job_times):
        from collections import defaultdict
        machines = defaultdict(list)
        for job_id, machine, position in solution:
            start_time, end_time, job_tardiness, job_id = job_times[(machine, position)]
            machines[machine].append((job_id, start_time, end_time, job_tardiness))
        return machines

    def prepare_table_data(self, jobs, job_data):
        table_data = []
        queue_no = 1
        for job_id, start_time, end_time, job_tardiness in jobs:
            for job in job_data:

                if job.job_id == job_id:
                    if job.job_type == "TOP":
                        table_data.append([
                            queue_no, job.code, job.mold_shelf_no,
                            job.male_mold_shelf_no, "TOP",
                            job.mold_width, start_time, end_time, job_tardiness
                        ])
                        queue_no += 1
                        table_data.append([
                            queue_no, job.code, job.mold_shelf_no,
                            job.male_mold_shelf_no, "BOTTOM",
                            job.mold_width, start_time, end_time, job_tardiness
                        ])
                        queue_no += 1
                    elif job.job_type == "FRONT":
                        table_data.append([
                            queue_no, job.code, job.mold_shelf_no,
                            job.male_mold_shelf_no, "FRONT",
                            job.mold_width, start_time, end_time, job_tardiness
                        ])
                        queue_no += 1
                        table_data.append([
                            queue_no, job.code, job.mold_shelf_no,
                            job.male_mold_shelf_no, "BACK",
                            job.mold_width, start_time, end_time, job_tardiness
                        ])
                        queue_no += 1
                    else:
                        table_data.append([
                            queue_no, job.code, job.mold_shelf_no,
                            job.male_mold_shelf_no, "MIDDLE",
                            job.mold_width, start_time, end_time, job_tardiness
                        ])
                        queue_no += 1

        return table_data

    def prepare_machine_table_data(self, organized_jobs, jobs_list):
        job_data = jobs_list  # List of all Job objects created earlier
        machine_table_data = {}
        for machine, jobs in organized_jobs.items():
            table_data = self.prepare_table_data(jobs, job_data)
            machine_table_data[machine] = table_data
        return machine_table_data

    # Functions for changing pages
    def change_page_to_unplanned_orders(self):
        self.stackedWidget.setCurrentIndex(0)

    def change_page_to_planned_orders(self):
        if self.planla_btn.isChecked():
            self.planla_counter += 1
            self.stackedWidget.setCurrentIndex(1)
            self.menu_planned_btn_2.setChecked(True)
        elif self.planla_counter == 0:
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
        return text

    def get_search_input(self):
        text = self.search_input.text()
        print("Searching for: ", text)
        return text

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
        return selected_checkboxes

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
        return selected_checkboxes

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
        return selected_checkboxes


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

        if self.type_checkBox_front_2.isChecked():
            selected_checkboxes.append(self.type_checkBox_front_2.text())

        if self.type_checkBox_back_2.isChecked():
            selected_checkboxes.append(self.type_checkBox_back_2.text())

        print("Selected Type Checkboxes:", selected_checkboxes)
        return selected_checkboxes

    def get_selected_type_checkboxes(self):
        # Getting values as string
        selected_checkboxes = []

        if self.type_checkBox_top.isChecked():
            selected_checkboxes.append(self.type_checkBox_top.text())

        if self.type_checkBox_bottom.isChecked():
            selected_checkboxes.append(self.type_checkBox_bottom.text())

        if self.type_checkBox_middle.isChecked():
            selected_checkboxes.append(self.type_checkBox_middle.text())

        if self.type_checkBox_front.isChecked():
            selected_checkboxes.append(self.type_checkBox_front.text())

        if self.type_checkBox_back.isChecked():
            selected_checkboxes.append(self.type_checkBox_back.text())

        print("Selected Type Checkboxes:", selected_checkboxes)
        return selected_checkboxes

    def filter_machine_table_data(self, machine_table_data, selected_checkboxes_kalıp_genisligi, selected_checkboxes_type, searched_parca_kodu):
        filtered_machine_table_data = {}
        for machine, jobs in machine_table_data.items():
            filtered_jobs = jobs  # Start with all jobs

            if selected_checkboxes_kalıp_genisligi:
                filtered_jobs = [job for job in filtered_jobs if job[5] in selected_checkboxes_kalıp_genisligi]

            if selected_checkboxes_type:
                filtered_jobs = [job for job in filtered_jobs if job[4] in selected_checkboxes_type]

            if searched_parca_kodu:
                print("Searching for part code:", searched_parca_kodu)
            # Filter jobs that contain the searched part code in any part of the job data
                filtered_jobs = [job for job in filtered_jobs if searched_parca_kodu in job[1]]
                print("Filtered jobs after part code search:", filtered_jobs)

            filtered_machine_table_data[machine] = filtered_jobs
        return filtered_machine_table_data
    def update_table_models(self):
        if self.machine_table_data_xl is None:
            print("Error: machine_table_data_xl is not initialized properly.")
            return
        selected_checkboxes_kalıp_genisligi = self.get_selected_kalip_genisligi_checkboxes()
        selected_checkboxes_type = self.get_selected_type_checkboxes()
        selected_checkboxes_machine = self.get_selected_makineler_checkboxes()
        searched_parca_kodu = self.get_search_input()

        # Filter the data
        filtered_machine_table_data_xl = self.filter_machine_table_data(self.machine_table_data_xl,
                                                                    selected_checkboxes_kalıp_genisligi,
                                                                    selected_checkboxes_type,
                                                                    searched_parca_kodu
                                                                    )
        filtered_machine_table_data_kz = self.filter_machine_table_data(self.machine_table_data_kz,
                                                                        selected_checkboxes_kalıp_genisligi,
                                                                        selected_checkboxes_type,
                                                                        searched_parca_kodu
                                                                        )
        filtered_machine_table_data_erl = self.filter_machine_table_data(self.machine_table_data_erl,
                                                                         selected_checkboxes_kalıp_genisligi,
                                                                         selected_checkboxes_type,
                                                                         searched_parca_kodu
                                                                         )
        all_kz_views = [
            self.KZ_1_table_view, self.KZ_2_table_view, self.KZ_3_table_view, self.KZ_4_table_view,
            self.KZ_5_table_view, self.KZ_6_table_view, self.KZ_7_table_view, self.KZ_8_table_view
        ]
        all_xl_views = [
            self.KZ_XL_1_table_view, self.KZ_XL_2_table_view, self.KZ_XL_3_table_view, self.KZ_XL_4_table_view
        ]
        all_erl_views = [
            self.ERL_1_table_view, self.ERL_2_table_view, self.ERL_3_table_view
        ]

        all_kz_labels = [
            self.KZ_1_label, self.KZ_2_label, self.KZ_3_label, self.KZ_4_label,
            self.KZ_5_label, self.KZ_6_label, self.KZ_7_label, self.KZ_8_label
        ]
        all_xl_labels = [
            self.KZ_XL_1_label, self.KZ_XL_2_label, self.KZ_XL_3_label, self.KZ_XL_4_label
        ]
        all_erl_labels = [
            self.ERL_1_label, self.ERL_2_label, self.ERL_3_label
        ]

        for view, label in zip(all_kz_views, all_kz_labels):
            label_text = label.text()
            if label_text in selected_checkboxes_machine:
                view.setVisible(True)
                label.setVisible(True)
            else:
                view.setVisible(False)
                label.setVisible(False)

        for view, label in zip(all_xl_views, all_xl_labels):
            label_text = label.text()
            if label_text in selected_checkboxes_machine:
                view.setVisible(True)
                label.setVisible(True)
            else:
                view.setVisible(False)
                label.setVisible(False)

        for view, label in zip(all_erl_views, all_erl_labels):
            label_text = label.text()
            if label_text in selected_checkboxes_machine:
                view.setVisible(True)
                label.setVisible(True)
            else:
                view.setVisible(False)
                label.setVisible(False)
        # Update table models
        self.kz_1_model = Custom_SQL_Table_Model(filtered_machine_table_data_kz.get(0, []),
                                                 self.planlanmis_table_column_names)
        self.KZ_1_table_view.setModel(self.kz_1_model)

        self.kz_2_model = Custom_SQL_Table_Model(filtered_machine_table_data_kz.get(1, []),
                                                 self.planlanmis_table_column_names)
        self.KZ_2_table_view.setModel(self.kz_2_model)

        self.kz_3_model = Custom_SQL_Table_Model(filtered_machine_table_data_kz.get(2, []),
                                                 self.planlanmis_table_column_names)
        self.KZ_3_table_view.setModel(self.kz_3_model)

        self.kz_4_model = Custom_SQL_Table_Model(filtered_machine_table_data_kz.get(3, []),
                                                 self.planlanmis_table_column_names)
        self.KZ_4_table_view.setModel(self.kz_4_model)

        self.kz_5_model = Custom_SQL_Table_Model(filtered_machine_table_data_kz.get(4, []),
                                                 self.planlanmis_table_column_names)
        self.KZ_5_table_view.setModel(self.kz_5_model)

        self.kz_6_model = Custom_SQL_Table_Model(filtered_machine_table_data_kz.get(5, []),
                                                 self.planlanmis_table_column_names)
        self.KZ_6_table_view.setModel(self.kz_6_model)

        self.kz_7_model = Custom_SQL_Table_Model(filtered_machine_table_data_kz.get(6, []),
                                                 self.planlanmis_table_column_names)
        self.KZ_7_table_view.setModel(self.kz_7_model)

        self.kz_8_model = Custom_SQL_Table_Model(filtered_machine_table_data_kz.get(7, []),
                                                 self.planlanmis_table_column_names)
        self.KZ_8_table_view.setModel(self.kz_8_model)

        self.kz_XL_1_model = Custom_SQL_Table_Model(filtered_machine_table_data_xl.get(0, []),
                                                    self.planlanmis_table_column_names)
        self.KZ_XL_1_table_view.setModel(self.kz_XL_1_model)

        self.kz_XL_2_model = Custom_SQL_Table_Model(filtered_machine_table_data_xl.get(1, []),
                                                    self.planlanmis_table_column_names)
        self.KZ_XL_2_table_view.setModel(self.kz_XL_2_model)

        self.kz_XL_3_model = Custom_SQL_Table_Model(filtered_machine_table_data_xl.get(2, []),
                                                    self.planlanmis_table_column_names)
        self.KZ_XL_3_table_view.setModel(self.kz_XL_3_model)

        self.kz_XL_4_model = Custom_SQL_Table_Model(filtered_machine_table_data_xl.get(1, []),
                                                    self.planlanmis_table_column_names)
        self.KZ_XL_4_table_view.setModel(self.kz_XL_4_model)

        self.ERL_1_model = Custom_SQL_Table_Model(filtered_machine_table_data_erl.get(0, []),
                                                  self.planlanmis_table_column_names)
        self.ERL_1_table_view.setModel(self.ERL_1_model)

        self.ERL_2_model = Custom_SQL_Table_Model(filtered_machine_table_data_erl.get(1, []),
                                                  self.planlanmis_table_column_names)
        self.ERL_2_table_view.setModel(self.ERL_2_model)

        self.ERL_3_model = Custom_SQL_Table_Model(filtered_machine_table_data_erl.get(2, []),
                                                  self.planlanmis_table_column_names)
        self.ERL_3_table_view.setModel(self.ERL_3_model)

    def get_unplanned_filter_results(self):
        entered_input = self.get_search_input_2()
        selected_kalip_genisligi = self.get_selected_kalip_genisligi_2_checkboxes()
        selected_type = self.get_selected_type_2_checkboxes()
        selected_montaj_ihtiyac_tarihi = self.selected_dates_2

        # Initialize empty lists to hold individual WHERE clauses
        where_clauses = []

        parca_kodu_count = 0
        # Check if lists are empty
        if entered_input != '':
            cursor.execute('''SELECT COUNT(CAST(m.PARCA_KODU AS varchar(50))) AS PARCA_KODU
FROM SAP_URT_SIP s
INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))
WHERE (CAST(m.PARCA_KODU AS varchar(50)) = {}'''.format(entered_input))
            parca_kodu_count = cursor.fetchall()
            if parca_kodu_count != 0:
                where_clause_input = " AND ".join(
                    ["(CAST(m.PARCA_KODU AS varchar(50))) = '{}'".format(entered_input)])
                where_clauses.append("(" + where_clause_input + ")")

        if selected_kalip_genisligi:
            where_clause_kalip_genisligi = " AND ".join(
                ["(CAST(m.KALIP_GENISLIGI AS varchar(50))) = '{}'".format(value) for value in selected_kalip_genisligi])
            where_clauses.append("(" + where_clause_kalip_genisligi + ")")

        # Check if selected_type list is not empty
        if selected_type:
            where_clause_type = " AND ".join(["(CAST(m.TYPE AS varchar(50))) = '{}'".format(value) for value in selected_type])
            where_clauses.append("(" + where_clause_type + ")")

        if selected_montaj_ihtiyac_tarihi:
            self.get_selected_dates_2()  # To print selected dates
            where_clause_montaj_ihtiyac_tarihi = " OR ".join(
                ["s.PTARIH  = '{}'".format(value) for value in selected_montaj_ihtiyac_tarihi])
            # where_clauses.append("(" + where_clause_montaj_ihtiyac_tarihi + ")")

        # Join all WHERE clauses with 'AND' to ensure all conditions must be met
        full_where_clause = " AND ".join(where_clauses)

        # Construct the full SQL query
        sql_query = '''SELECT TOP 50 CAST(m.PARCA_KODU AS varchar(50)) AS PARCA_KODU, s.PTARIH, m.CYCLE_TIME, m.KALIP_RAF_NO, m.ERKEK_KALIP_RAF_NO, m.TYPE,  m.KALIP_GENISLIGI
FROM SAP_URT_SIP s
INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))'''
        if full_where_clause:
            sql_query += " WHERE {}".format(full_where_clause)

        cursor.execute(sql_query)
        row_count = cursor.rowcount
        if row_count != 0:
            unordered_table_data = cursor.fetchall()

        else:
            unordered_table_data = [
                ["No Result", "No Result", "No Result", "No Result", "No Result", "No Result", "No Result"]]

        for row in unordered_table_data:
            print(row)

        planlanmamis_table_column_names = ["Parça Kodu", "Sipariş Teslim Tarihi", "Cycle Time", "Kalıp Raf No.",
                                           "Erkek Kalıp Raf No.", "Type", "Kalıp Genişliği"]

        self.unordered_model = Custom_SQL_Table_Model(unordered_table_data, planlanmamis_table_column_names)
        self.tableView.setModel(self.unordered_model)


    def export_to_excel(self):
        # Get data from the table model
        data = []
        for row in range(self.arranged_table_model.rowCount()):
            row_data = []
            for column in range(self.arranged_table_model.columnCount()):
                item = self.arranged_table_model.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append('')  # Handle empty cells
            data.append(row_data)

        # Convert data to DataFrame
        df = pd.DataFrame(data, columns=self.arranged_table_column_names)

        # Export DataFrame to Excel
        excel_file_path = 'output.xlsx'  # Path to save the Excel file
        df.to_excel(excel_file_path, index=False)

        print("Data exported to Excel successfully!")