# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceNCUUsV.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1065, 692)
        MainWindow.setStyleSheet(u"*{\n"
"	background-color: #fff;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QScrollBar:vertical{\n"
"border: none;\n"
"background-color: #EEEEEE;\n"
"width: 12px;\n"
"margin: 15px 0 15px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background-color: #222831;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background-color: #31363F;\n"
"}\n"
"\n"
"QScrollBar{\n"
"border: none;\n"
"height: 12px;\n"
"background-color: #EEEEEE;\n"
"}\n"
"\n"
"QScrollBar::handle{\n"
"background-color: #222831;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:hover{\n"
"background-color: #31363F;\n"
"}\n"
"\n"
"QTableWidget{\n"
"min-height:300px;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section{\n"
"background-color: #EEEEEE;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"*{\n"
"	background-color: #222831;\n"
"	width: 60px;\n"
"}\n"
"\n"
"QPushButton, QLabel{\n"
"	width: 60px;\n"
"	height: 60px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #31363f;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo_img = QLabel(self.icon_only_widget)
        self.logo_img.setObjectName(u"logo_img")
        self.logo_img.setMinimumSize(QSize(50, 50))
        self.logo_img.setMaximumSize(QSize(50, 50))
        self.logo_img.setStyleSheet(u"padding: 5px;")
        self.logo_img.setPixmap(QPixmap(u":/icons/icons/logo.png"))
        self.logo_img.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo_img)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.menu_unplanned_btn = QPushButton(self.icon_only_widget)
        self.menu_unplanned_btn.setObjectName(u"menu_unplanned_btn")
        self.menu_unplanned_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_unplanned_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/unplanned-white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/icons/unplanned-red.png", QSize(), QIcon.Normal, QIcon.On)
        self.menu_unplanned_btn.setIcon(icon)
        self.menu_unplanned_btn.setIconSize(QSize(20, 20))
        self.menu_unplanned_btn.setCheckable(True)
        self.menu_unplanned_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.menu_unplanned_btn)

        self.menu_planned_btn = QPushButton(self.icon_only_widget)
        self.menu_planned_btn.setObjectName(u"menu_planned_btn")
        self.menu_planned_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_planned_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/planned-white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/icons/planned-red.png", QSize(), QIcon.Normal, QIcon.On)
        self.menu_planned_btn.setIcon(icon1)
        self.menu_planned_btn.setIconSize(QSize(20, 20))
        self.menu_planned_btn.setCheckable(True)
        self.menu_planned_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.menu_planned_btn)

        self.menu_stock_btn = QPushButton(self.icon_only_widget)
        self.menu_stock_btn.setObjectName(u"menu_stock_btn")
        self.menu_stock_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_stock_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/stock-status.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/icons/stock-status-red.png", QSize(), QIcon.Normal, QIcon.On)
        self.menu_stock_btn.setIcon(icon2)
        self.menu_stock_btn.setIconSize(QSize(20, 20))
        self.menu_stock_btn.setCheckable(True)
        self.menu_stock_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.menu_stock_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.vestel_logo = QPushButton(self.icon_only_widget)
        self.vestel_logo.setObjectName(u"vestel_logo")
        self.vestel_logo.setStyleSheet(u"*:hover{\n"
"background-color: #222831;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/vestel_logo_cropped.png", QSize(), QIcon.Normal, QIcon.Off)
        self.vestel_logo.setIcon(icon3)
        self.vestel_logo.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.vestel_logo)


        self.horizontalLayout_9.addWidget(self.icon_only_widget)

        self.full_menu_widget = QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName(u"full_menu_widget")
        self.full_menu_widget.setStyleSheet(u"*{\n"
"	background-color: #222831;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"	border-radius: 3px;\n"
"	height: 30px;\n"
"	text-align: left;\n"
"	padding: 8px 2px 8px 15px;\n"
"	color: #EEEEEE;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #31363f;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	color: #df2027;\n"
"}\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 9, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 5)
        self.logo_img_2 = QLabel(self.full_menu_widget)
        self.logo_img_2.setObjectName(u"logo_img_2")
        self.logo_img_2.setMinimumSize(QSize(40, 40))
        self.logo_img_2.setMaximumSize(QSize(40, 40))
        self.logo_img_2.setStyleSheet(u"padding: 5px;\n"
"color: #EEEEEE;")
        self.logo_img_2.setPixmap(QPixmap(u":/icons/icons/logo.png"))
        self.logo_img_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo_img_2)

        self.logo_name = QLabel(self.full_menu_widget)
        self.logo_name.setObjectName(u"logo_name")
        font = QFont()
        font.setPointSize(15)
        self.logo_name.setFont(font)
        self.logo_name.setStyleSheet(u"padding_right: 10px;\n"
"color: #EEEEEE;")

        self.horizontalLayout.addWidget(self.logo_name)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.menu_unplanned_btn_2 = QPushButton(self.full_menu_widget)
        self.menu_unplanned_btn_2.setObjectName(u"menu_unplanned_btn_2")
        font1 = QFont()
        font1.setPointSize(10)
        self.menu_unplanned_btn_2.setFont(font1)
        self.menu_unplanned_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_unplanned_btn_2.setStyleSheet(u"")
        self.menu_unplanned_btn_2.setIcon(icon)
        self.menu_unplanned_btn_2.setIconSize(QSize(14, 14))
        self.menu_unplanned_btn_2.setCheckable(True)
        self.menu_unplanned_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.menu_unplanned_btn_2)

        self.menu_planned_btn_2 = QPushButton(self.full_menu_widget)
        self.menu_planned_btn_2.setObjectName(u"menu_planned_btn_2")
        self.menu_planned_btn_2.setFont(font1)
        self.menu_planned_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_planned_btn_2.setStyleSheet(u"")
        self.menu_planned_btn_2.setIcon(icon1)
        self.menu_planned_btn_2.setIconSize(QSize(14, 14))
        self.menu_planned_btn_2.setCheckable(True)
        self.menu_planned_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.menu_planned_btn_2)

        self.menu_stock_btn_2 = QPushButton(self.full_menu_widget)
        self.menu_stock_btn_2.setObjectName(u"menu_stock_btn_2")
        self.menu_stock_btn_2.setFont(font1)
        self.menu_stock_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_stock_btn_2.setStyleSheet(u"")
        self.menu_stock_btn_2.setIcon(icon2)
        self.menu_stock_btn_2.setIconSize(QSize(14, 14))
        self.menu_stock_btn_2.setCheckable(True)
        self.menu_stock_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.menu_stock_btn_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.vestel_logo_2 = QPushButton(self.full_menu_widget)
        self.vestel_logo_2.setObjectName(u"vestel_logo_2")
        self.vestel_logo_2.setStyleSheet(u"*:hover{\n"
"background-color: #222831;\n"
"}\n"
"")
        self.vestel_logo_2.setIcon(icon3)
        self.vestel_logo_2.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.vestel_logo_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_9.addWidget(self.full_menu_widget)

        self.body_widget = QWidget(self.centralwidget)
        self.body_widget.setObjectName(u"body_widget")
        self.verticalLayout_7 = QVBoxLayout(self.body_widget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.body_widget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setStyleSheet(u"background-color: #F9FAFD;\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, -1, -1)
        self.change_btn = QPushButton(self.header_widget)
        self.change_btn.setObjectName(u"change_btn")
        self.change_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.change_btn.setStyleSheet(u"padding: 2px 2px 2px 0;\n"
"border: none;\n"
"width: 30px;\n"
"height: 30px;\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.change_btn.setIcon(icon4)
        self.change_btn.setIconSize(QSize(20, 20))
        self.change_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.change_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.body_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.unplanned_orders = QWidget()
        self.unplanned_orders.setObjectName(u"unplanned_orders")
        self.unplanned_orders.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.unplanned_orders)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, -1, 5, -1)
        self.planlanmamis_siparis_label = QLabel(self.unplanned_orders)
        self.planlanmamis_siparis_label.setObjectName(u"planlanmamis_siparis_label")
        font2 = QFont()
        font2.setPointSize(13)
        self.planlanmamis_siparis_label.setFont(font2)
        self.planlanmamis_siparis_label.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.planlanmamis_siparis_label)

        self.tarihler_label_2 = QLabel(self.unplanned_orders)
        self.tarihler_label_2.setObjectName(u"tarihler_label_2")
        font3 = QFont()
        font3.setPointSize(11)
        self.tarihler_label_2.setFont(font3)
        self.tarihler_label_2.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.tarihler_label_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tableView = QTableView(self.unplanned_orders)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"")
        self.tableView.horizontalHeader().setMinimumSectionSize(250)
        self.tableView.horizontalHeader().setDefaultSectionSize(250)

        self.horizontalLayout_7.addWidget(self.tableView)

        self.unplanned_fltr_scroll_area = QScrollArea(self.unplanned_orders)
        self.unplanned_fltr_scroll_area.setObjectName(u"unplanned_fltr_scroll_area")
        self.unplanned_fltr_scroll_area.setStyleSheet(u"")
        self.unplanned_fltr_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 228, 602))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"padding: 0;")
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, -1, 5, -1)
        self.filters_label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.filters_label_2.setObjectName(u"filters_label_2")
        font4 = QFont()
        font4.setPointSize(12)
        self.filters_label_2.setFont(font4)
        self.filters_label_2.setStyleSheet(u"")

        self.verticalLayout_15.addWidget(self.filters_label_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.search_input_2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.search_input_2.setObjectName(u"search_input_2")
        self.search_input_2.setCursor(QCursor(Qt.IBeamCursor))
        self.search_input_2.setStyleSheet(u"*{\n"
"border: 1px solid #EEEEEE;\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"}\n"
"\n"
"*:focus{\n"
"background-color: #EEEEEE;\n"
"}")
        self.search_input_2.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.search_input_2)

        self.search_btn_2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.search_btn_2.setObjectName(u"search_btn_2")
        self.search_btn_2.setCursor(QCursor(Qt.ArrowCursor))
        self.search_btn_2.setMouseTracking(True)
        self.search_btn_2.setStyleSheet(u"*{\n"
"border: 1px solid #EEEEEE;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"}\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/search-red.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn_2.setIcon(icon5)
        self.search_btn_2.setIconSize(QSize(20, 20))
        self.search_btn_2.setCheckable(False)

        self.horizontalLayout_10.addWidget(self.search_btn_2)


        self.verticalLayout_15.addLayout(self.horizontalLayout_10)


        self.verticalLayout_17.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 5, -1, 5)
        self.kalip_genisligi_widget_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.kalip_genisligi_widget_2.setObjectName(u"kalip_genisligi_widget_2")
        self.kalip_genisligi_widget_2.setMinimumSize(QSize(0, 40))
        self.kalip_genisligi_widget_2.setStyleSheet(u"*{\n"
"border:none;\n"
"padding: 10px 5px;\n"
"height: 40px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color: #EEEEEE;\n"
"}")
        self.horizontalLayout_33 = QHBoxLayout(self.kalip_genisligi_widget_2)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.kalip_genisligi_fltr_label_btn_2 = QPushButton(self.kalip_genisligi_widget_2)
        self.kalip_genisligi_fltr_label_btn_2.setObjectName(u"kalip_genisligi_fltr_label_btn_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kalip_genisligi_fltr_label_btn_2.sizePolicy().hasHeightForWidth())
        self.kalip_genisligi_fltr_label_btn_2.setSizePolicy(sizePolicy)
        self.kalip_genisligi_fltr_label_btn_2.setFont(font3)
        self.kalip_genisligi_fltr_label_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.kalip_genisligi_fltr_label_btn_2.setStyleSheet(u"*{\n"
"border: none;\n"
"text-align: left;\n"
"padding-left: 5px;\n"
"height: 30px;\n"
"}")
        self.kalip_genisligi_fltr_label_btn_2.setCheckable(True)

        self.horizontalLayout_32.addWidget(self.kalip_genisligi_fltr_label_btn_2)

        self.horizontalSpacer_19 = QSpacerItem(0, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_19)

        self.kalip_genisligi_fltr_icon_btn_2 = QPushButton(self.kalip_genisligi_widget_2)
        self.kalip_genisligi_fltr_icon_btn_2.setObjectName(u"kalip_genisligi_fltr_icon_btn_2")
        self.kalip_genisligi_fltr_icon_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.kalip_genisligi_fltr_icon_btn_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.kalip_genisligi_fltr_icon_btn_2.setStyleSheet(u"border: none;\n"
"height: 30px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/plus-red.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icons/icons/minus-red.png", QSize(), QIcon.Normal, QIcon.On)
        self.kalip_genisligi_fltr_icon_btn_2.setIcon(icon6)
        self.kalip_genisligi_fltr_icon_btn_2.setCheckable(True)

        self.horizontalLayout_32.addWidget(self.kalip_genisligi_fltr_icon_btn_2)


        self.horizontalLayout_33.addLayout(self.horizontalLayout_32)


        self.verticalLayout_16.addWidget(self.kalip_genisligi_widget_2)

        self.kalip_genisligi_check_boxes_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.kalip_genisligi_check_boxes_2.setObjectName(u"kalip_genisligi_check_boxes_2")
        self.kalip_genisligi_check_boxes_2.setMinimumSize(QSize(0, 60))
        self.kalip_genisligi_check_boxes_2.setStyleSheet(u"background-color: #EEEEEE;")
        self.gridLayout_2 = QGridLayout(self.kalip_genisligi_check_boxes_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.kalip_genisligi_checkBox_S_2 = QCheckBox(self.kalip_genisligi_check_boxes_2)
        self.kalip_genisligi_checkBox_S_2.setObjectName(u"kalip_genisligi_checkBox_S_2")

        self.gridLayout_2.addWidget(self.kalip_genisligi_checkBox_S_2, 0, 0, 1, 1)

        self.kalip_genisligi_checkBox_M_2 = QCheckBox(self.kalip_genisligi_check_boxes_2)
        self.kalip_genisligi_checkBox_M_2.setObjectName(u"kalip_genisligi_checkBox_M_2")

        self.gridLayout_2.addWidget(self.kalip_genisligi_checkBox_M_2, 0, 1, 1, 1)

        self.kalip_genisligi_checkBox_L_2 = QCheckBox(self.kalip_genisligi_check_boxes_2)
        self.kalip_genisligi_checkBox_L_2.setObjectName(u"kalip_genisligi_checkBox_L_2")

        self.gridLayout_2.addWidget(self.kalip_genisligi_checkBox_L_2, 1, 0, 1, 1)

        self.kalip_genisligi_checkBox_ERL_2 = QCheckBox(self.kalip_genisligi_check_boxes_2)
        self.kalip_genisligi_checkBox_ERL_2.setObjectName(u"kalip_genisligi_checkBox_ERL_2")

        self.gridLayout_2.addWidget(self.kalip_genisligi_checkBox_ERL_2, 1, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.kalip_genisligi_check_boxes_2)

        self.montaj_ihtiyac_widget_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.montaj_ihtiyac_widget_2.setObjectName(u"montaj_ihtiyac_widget_2")
        self.montaj_ihtiyac_widget_2.setMinimumSize(QSize(0, 40))
        self.montaj_ihtiyac_widget_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.montaj_ihtiyac_widget_2.setStyleSheet(u"*{\n"
"border:none;\n"
"padding: 10px 5px;\n"
"height: 40px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color: #EEEEEE;\n"
"}")
        self.horizontalLayout_35 = QHBoxLayout(self.montaj_ihtiyac_widget_2)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.montaj_ihtiyac_fltr_label_btn_2 = QPushButton(self.montaj_ihtiyac_widget_2)
        self.montaj_ihtiyac_fltr_label_btn_2.setObjectName(u"montaj_ihtiyac_fltr_label_btn_2")
        sizePolicy.setHeightForWidth(self.montaj_ihtiyac_fltr_label_btn_2.sizePolicy().hasHeightForWidth())
        self.montaj_ihtiyac_fltr_label_btn_2.setSizePolicy(sizePolicy)
        self.montaj_ihtiyac_fltr_label_btn_2.setFont(font3)
        self.montaj_ihtiyac_fltr_label_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.montaj_ihtiyac_fltr_label_btn_2.setStyleSheet(u"*{\n"
"border: none;\n"
"text-align: left;\n"
"padding-left: 5px;\n"
"height: 30px;\n"
"}")
        self.montaj_ihtiyac_fltr_label_btn_2.setCheckable(True)

        self.horizontalLayout_34.addWidget(self.montaj_ihtiyac_fltr_label_btn_2)

        self.horizontalSpacer_20 = QSpacerItem(0, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_20)

        self.montaj_ihtiyac_fltr_icon_btn_2 = QPushButton(self.montaj_ihtiyac_widget_2)
        self.montaj_ihtiyac_fltr_icon_btn_2.setObjectName(u"montaj_ihtiyac_fltr_icon_btn_2")
        self.montaj_ihtiyac_fltr_icon_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.montaj_ihtiyac_fltr_icon_btn_2.setStyleSheet(u"border: none;\n"
"height: 30px;")
        self.montaj_ihtiyac_fltr_icon_btn_2.setIcon(icon6)
        self.montaj_ihtiyac_fltr_icon_btn_2.setCheckable(True)

        self.horizontalLayout_34.addWidget(self.montaj_ihtiyac_fltr_icon_btn_2)


        self.horizontalLayout_35.addLayout(self.horizontalLayout_34)


        self.verticalLayout_16.addWidget(self.montaj_ihtiyac_widget_2)

        self.montaj_ihtiyac_calendar_widget_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.montaj_ihtiyac_calendar_widget_2.setObjectName(u"montaj_ihtiyac_calendar_widget_2")
        self.montaj_ihtiyac_calendar_widget_2.setMinimumSize(QSize(0, 200))
        self.montaj_ihtiyac_calendar_widget_2.setStyleSheet(u"background-color: #EEEEEE;")
        self.horizontalLayout_44 = QHBoxLayout(self.montaj_ihtiyac_calendar_widget_2)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, 5, -1, 5)
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_29)

        self.calendarWidget_2 = QCalendarWidget(self.montaj_ihtiyac_calendar_widget_2)
        self.calendarWidget_2.setObjectName(u"calendarWidget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.calendarWidget_2.sizePolicy().hasHeightForWidth())
        self.calendarWidget_2.setSizePolicy(sizePolicy1)
        self.calendarWidget_2.setStyleSheet(u"background-color: #fff;\n"
"color: black;")
        self.calendarWidget_2.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)

        self.horizontalLayout_43.addWidget(self.calendarWidget_2)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_30)


        self.horizontalLayout_44.addLayout(self.horizontalLayout_43)


        self.verticalLayout_16.addWidget(self.montaj_ihtiyac_calendar_widget_2)

        self.type_widget_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.type_widget_2.setObjectName(u"type_widget_2")
        self.type_widget_2.setMinimumSize(QSize(0, 40))
        self.type_widget_2.setStyleSheet(u"*{\n"
"border:none;\n"
"padding: 10px 5px;\n"
"height: 40px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color: #EEEEEE;\n"
"}")
        self.horizontalLayout_13 = QHBoxLayout(self.type_widget_2)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.type_fltr_label_btn_2 = QPushButton(self.type_widget_2)
        self.type_fltr_label_btn_2.setObjectName(u"type_fltr_label_btn_2")
        sizePolicy.setHeightForWidth(self.type_fltr_label_btn_2.sizePolicy().hasHeightForWidth())
        self.type_fltr_label_btn_2.setSizePolicy(sizePolicy)
        self.type_fltr_label_btn_2.setFont(font3)
        self.type_fltr_label_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.type_fltr_label_btn_2.setStyleSheet(u"*{\n"
"border: none;\n"
"text-align: left;\n"
"padding-left: 5px;\n"
"height: 30px;\n"
"}")
        self.type_fltr_label_btn_2.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.type_fltr_label_btn_2)

        self.horizontalSpacer_6 = QSpacerItem(0, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)

        self.type_fltr_icon_btn_2 = QPushButton(self.type_widget_2)
        self.type_fltr_icon_btn_2.setObjectName(u"type_fltr_icon_btn_2")
        self.type_fltr_icon_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.type_fltr_icon_btn_2.setStyleSheet(u"border: none;\n"
"height: 30px;")
        self.type_fltr_icon_btn_2.setIcon(icon6)
        self.type_fltr_icon_btn_2.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.type_fltr_icon_btn_2)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)


        self.verticalLayout_16.addWidget(self.type_widget_2)

        self.type_check_boxes_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.type_check_boxes_2.setObjectName(u"type_check_boxes_2")
        self.type_check_boxes_2.setMinimumSize(QSize(0, 80))
        self.type_check_boxes_2.setStyleSheet(u"background-color: #EEEEEE;")
        self.gridLayout_4 = QGridLayout(self.type_check_boxes_2)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 9, 9, 9)
        self.type_checkBox_bottom_2 = QCheckBox(self.type_check_boxes_2)
        self.type_checkBox_bottom_2.setObjectName(u"type_checkBox_bottom_2")

        self.gridLayout_4.addWidget(self.type_checkBox_bottom_2, 0, 1, 1, 1)

        self.type_checkBox_top_2 = QCheckBox(self.type_check_boxes_2)
        self.type_checkBox_top_2.setObjectName(u"type_checkBox_top_2")

        self.gridLayout_4.addWidget(self.type_checkBox_top_2, 0, 0, 1, 1)

        self.type_checkBox_middle_2 = QCheckBox(self.type_check_boxes_2)
        self.type_checkBox_middle_2.setObjectName(u"type_checkBox_middle_2")

        self.gridLayout_4.addWidget(self.type_checkBox_middle_2, 2, 0, 1, 2)

        self.type_checkBox_front_2 = QCheckBox(self.type_check_boxes_2)
        self.type_checkBox_front_2.setObjectName(u"type_checkBox_front_2")

        self.gridLayout_4.addWidget(self.type_checkBox_front_2, 1, 0, 1, 1)

        self.type_checkBox_back_2 = QCheckBox(self.type_check_boxes_2)
        self.type_checkBox_back_2.setObjectName(u"type_checkBox_back_2")

        self.gridLayout_4.addWidget(self.type_checkBox_back_2, 1, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.type_check_boxes_2)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)

        self.verticalSpacer_3 = QSpacerItem(20, 167, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_3)

        self.uygula_widget_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.uygula_widget_2.setObjectName(u"uygula_widget_2")
        self.uygula_widget_2.setMinimumSize(QSize(0, 30))
        self.uygula_widget_2.setStyleSheet(u"")
        self.horizontalLayout_19 = QHBoxLayout(self.uygula_widget_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, -1, -1, 3)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_10)

        self.uygula_btn_2 = QPushButton(self.uygula_widget_2)
        self.uygula_btn_2.setObjectName(u"uygula_btn_2")
        self.uygula_btn_2.setMinimumSize(QSize(0, 30))
        self.uygula_btn_2.setFont(font1)
        self.uygula_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.uygula_btn_2.setStyleSheet(u"*{\n"
"border: none;\n"
"border-radius:  4px;\n"
"width: 90px;\n"
"height: 30px;\n"
"background-color: #222831;\n"
"color: #fff;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color: #31363f;\n"
"}")
        self.uygula_btn_2.setCheckable(True)

        self.horizontalLayout_18.addWidget(self.uygula_btn_2)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_11)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_18)


        self.verticalLayout_17.addWidget(self.uygula_widget_2)

        self.unplanned_fltr_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_7.addWidget(self.unplanned_fltr_scroll_area)

        self.horizontalLayout_7.setStretch(0, 3)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 10, -1, 10)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.planla_btn = QPushButton(self.unplanned_orders)
        self.planla_btn.setObjectName(u"planla_btn")
        self.planla_btn.setFont(font1)
        self.planla_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.planla_btn.setStyleSheet(u"*{\n"
"border: none;\n"
"border-radius:  4px;\n"
"width: 90px;\n"
"height: 30px;\n"
"background-color: #222831;\n"
"color: #fff;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color: #31363f;\n"
"}")
        self.planla_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.planla_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.stackedWidget.addWidget(self.unplanned_orders)
        self.planned_orders = QWidget()
        self.planned_orders.setObjectName(u"planned_orders")
        self.verticalLayout_9 = QVBoxLayout(self.planned_orders)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, -1, 5, -1)
        self.planlanmis_siparis_label = QLabel(self.planned_orders)
        self.planlanmis_siparis_label.setObjectName(u"planlanmis_siparis_label")
        self.planlanmis_siparis_label.setFont(font2)
        self.planlanmis_siparis_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.planlanmis_siparis_label.setStyleSheet(u"")
        self.planlanmis_siparis_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.planlanmis_siparis_label)

        self.tarihler_label = QLabel(self.planned_orders)
        self.tarihler_label.setObjectName(u"tarihler_label")
        self.tarihler_label.setFont(font3)
        self.tarihler_label.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.tarihler_label)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.planned_table_scroll_area = QScrollArea(self.planned_orders)
        self.planned_table_scroll_area.setObjectName(u"planned_table_scroll_area")
        self.planned_table_scroll_area.setStyleSheet(u"QLabel{\n"
"margin-left: 3px;\n"
"}\n"
"")
        self.planned_table_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 563, 5296))
        self.scrollAreaWidgetContents_5.setStyleSheet(u"")
        self.verticalLayout_56 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setSpacing(25)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setSpacing(8)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(-1, 5, -1, -1)
        self.KZ_1_label = QLabel(self.scrollAreaWidgetContents_5)
        self.KZ_1_label.setObjectName(u"KZ_1_label")
        self.KZ_1_label.setFont(font3)
        self.KZ_1_label.setStyleSheet(u"")
        self.KZ_1_label.setMargin(0)

        self.verticalLayout_41.addWidget(self.KZ_1_label)

        self.KZ_1_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.KZ_1_table_view.setObjectName(u"KZ_1_table_view")
        self.KZ_1_table_view.setMinimumSize(QSize(0, 300))
        self.KZ_1_table_view.setStyleSheet(u"")
        self.KZ_1_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.KZ_1_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_41.addWidget(self.KZ_1_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_41)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setSpacing(6)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(-1, 0, -1, -1)
        self.KZ_2_label = QLabel(self.scrollAreaWidgetContents_5)
        self.KZ_2_label.setObjectName(u"KZ_2_label")
        self.KZ_2_label.setFont(font3)

        self.verticalLayout_42.addWidget(self.KZ_2_label)

        self.KZ_2_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.KZ_2_table_view.setObjectName(u"KZ_2_table_view")
        self.KZ_2_table_view.setMinimumSize(QSize(0, 300))
        self.KZ_2_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.KZ_2_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_42.addWidget(self.KZ_2_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_42)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.KZ_3_label = QLabel(self.scrollAreaWidgetContents_5)
        self.KZ_3_label.setObjectName(u"KZ_3_label")
        self.KZ_3_label.setFont(font3)

        self.verticalLayout_43.addWidget(self.KZ_3_label)

        self.KZ_3_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.KZ_3_table_view.setObjectName(u"KZ_3_table_view")
        self.KZ_3_table_view.setMinimumSize(QSize(0, 300))
        self.KZ_3_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.KZ_3_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_43.addWidget(self.KZ_3_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_43)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.KZ_4_label = QLabel(self.scrollAreaWidgetContents_5)
        self.KZ_4_label.setObjectName(u"KZ_4_label")
        self.KZ_4_label.setFont(font3)

        self.verticalLayout_44.addWidget(self.KZ_4_label)

        self.KZ_4_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.KZ_4_table_view.setObjectName(u"KZ_4_table_view")
        self.KZ_4_table_view.setMinimumSize(QSize(0, 300))
        self.KZ_4_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.KZ_4_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_44.addWidget(self.KZ_4_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_44)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.KZ_5_label = QLabel(self.scrollAreaWidgetContents_5)
        self.KZ_5_label.setObjectName(u"KZ_5_label")
        self.KZ_5_label.setFont(font3)

        self.verticalLayout_45.addWidget(self.KZ_5_label)

        self.KZ_5_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.KZ_5_table_view.setObjectName(u"KZ_5_table_view")
        self.KZ_5_table_view.setMinimumSize(QSize(0, 300))
        self.KZ_5_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.KZ_5_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_45.addWidget(self.KZ_5_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_45)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.KZ_6_label = QLabel(self.scrollAreaWidgetContents_5)
        self.KZ_6_label.setObjectName(u"KZ_6_label")
        self.KZ_6_label.setFont(font3)

        self.verticalLayout_46.addWidget(self.KZ_6_label)

        self.KZ_6_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.KZ_6_table_view.setObjectName(u"KZ_6_table_view")
        self.KZ_6_table_view.setMinimumSize(QSize(0, 300))
        self.KZ_6_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.KZ_6_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_46.addWidget(self.KZ_6_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_46)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.KZ_7_label = QLabel(self.scrollAreaWidgetContents_5)
        self.KZ_7_label.setObjectName(u"KZ_7_label")
        self.KZ_7_label.setFont(font3)

        self.verticalLayout_47.addWidget(self.KZ_7_label)

        self.KZ_7_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.KZ_7_table_view.setObjectName(u"KZ_7_table_view")
        self.KZ_7_table_view.setMinimumSize(QSize(0, 300))
        self.KZ_7_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.KZ_7_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_47.addWidget(self.KZ_7_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_47)

        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.KZ_8_label = QLabel(self.scrollAreaWidgetContents_5)
        self.KZ_8_label.setObjectName(u"KZ_8_label")
        self.KZ_8_label.setFont(font3)

        self.verticalLayout_48.addWidget(self.KZ_8_label)

        self.KZ_8_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.KZ_8_table_view.setObjectName(u"KZ_8_table_view")
        self.KZ_8_table_view.setMinimumSize(QSize(0, 300))
        self.KZ_8_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.KZ_8_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_48.addWidget(self.KZ_8_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_48)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.KZ_XL_1_label = QLabel(self.scrollAreaWidgetContents_5)
        self.KZ_XL_1_label.setObjectName(u"KZ_XL_1_label")
        self.KZ_XL_1_label.setFont(font3)

        self.verticalLayout_49.addWidget(self.KZ_XL_1_label)

        self.KZ_XL_1_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.KZ_XL_1_table_view.setObjectName(u"KZ_XL_1_table_view")
        self.KZ_XL_1_table_view.setMinimumSize(QSize(0, 300))
        self.KZ_XL_1_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.KZ_XL_1_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_49.addWidget(self.KZ_XL_1_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_49)

        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.KZ_XL_2_label = QLabel(self.scrollAreaWidgetContents_5)
        self.KZ_XL_2_label.setObjectName(u"KZ_XL_2_label")
        self.KZ_XL_2_label.setFont(font3)

        self.verticalLayout_50.addWidget(self.KZ_XL_2_label)

        self.KZ_XL_2_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.KZ_XL_2_table_view.setObjectName(u"KZ_XL_2_table_view")
        self.KZ_XL_2_table_view.setMinimumSize(QSize(0, 300))
        self.KZ_XL_2_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.KZ_XL_2_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_50.addWidget(self.KZ_XL_2_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_50)

        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.KZ_XL_3_label = QLabel(self.scrollAreaWidgetContents_5)
        self.KZ_XL_3_label.setObjectName(u"KZ_XL_3_label")
        self.KZ_XL_3_label.setFont(font3)

        self.verticalLayout_51.addWidget(self.KZ_XL_3_label)

        self.KZ_XL_3_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.KZ_XL_3_table_view.setObjectName(u"KZ_XL_3_table_view")
        self.KZ_XL_3_table_view.setMinimumSize(QSize(0, 300))
        self.KZ_XL_3_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.KZ_XL_3_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_51.addWidget(self.KZ_XL_3_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_51)

        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.KZ_XL_4_label = QLabel(self.scrollAreaWidgetContents_5)
        self.KZ_XL_4_label.setObjectName(u"KZ_XL_4_label")
        self.KZ_XL_4_label.setFont(font3)

        self.verticalLayout_52.addWidget(self.KZ_XL_4_label)

        self.KZ_XL_4_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.KZ_XL_4_table_view.setObjectName(u"KZ_XL_4_table_view")
        self.KZ_XL_4_table_view.setMinimumSize(QSize(0, 300))
        self.KZ_XL_4_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.KZ_XL_4_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_52.addWidget(self.KZ_XL_4_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_52)

        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.ERL_1_label = QLabel(self.scrollAreaWidgetContents_5)
        self.ERL_1_label.setObjectName(u"ERL_1_label")
        self.ERL_1_label.setFont(font3)

        self.verticalLayout_53.addWidget(self.ERL_1_label)

        self.ERL_1_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.ERL_1_table_view.setObjectName(u"ERL_1_table_view")
        self.ERL_1_table_view.setMinimumSize(QSize(0, 300))
        self.ERL_1_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.ERL_1_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_53.addWidget(self.ERL_1_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_53)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.ERL_2_label = QLabel(self.scrollAreaWidgetContents_5)
        self.ERL_2_label.setObjectName(u"ERL_2_label")
        self.ERL_2_label.setFont(font3)

        self.verticalLayout_54.addWidget(self.ERL_2_label)

        self.ERL_2_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.ERL_2_table_view.setObjectName(u"ERL_2_table_view")
        self.ERL_2_table_view.setMinimumSize(QSize(0, 300))
        self.ERL_2_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.ERL_2_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_54.addWidget(self.ERL_2_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_54)

        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.ERL_3_label = QLabel(self.scrollAreaWidgetContents_5)
        self.ERL_3_label.setObjectName(u"ERL_3_label")
        self.ERL_3_label.setFont(font3)

        self.verticalLayout_55.addWidget(self.ERL_3_label)

        self.ERL_3_table_view = QTableView(self.scrollAreaWidgetContents_5)
        self.ERL_3_table_view.setObjectName(u"ERL_3_table_view")
        self.ERL_3_table_view.setMinimumSize(QSize(0, 300))
        self.ERL_3_table_view.horizontalHeader().setMinimumSectionSize(200)
        self.ERL_3_table_view.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_55.addWidget(self.ERL_3_table_view)


        self.verticalLayout_40.addLayout(self.verticalLayout_55)


        self.verticalLayout_56.addLayout(self.verticalLayout_40)

        self.planned_table_scroll_area.setWidget(self.scrollAreaWidgetContents_5)

        self.horizontalLayout_6.addWidget(self.planned_table_scroll_area)

        self.planned_fltr_scroll_area = QScrollArea(self.planned_orders)
        self.planned_fltr_scroll_area.setObjectName(u"planned_fltr_scroll_area")
        self.planned_fltr_scroll_area.setStyleSheet(u"")
        self.planned_fltr_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -111, 178, 602))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, -1, 5, -1)
        self.filters_label = QLabel(self.scrollAreaWidgetContents)
        self.filters_label.setObjectName(u"filters_label")
        self.filters_label.setFont(font4)
        self.filters_label.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.filters_label)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.search_input = QLineEdit(self.scrollAreaWidgetContents)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setStyleSheet(u"*{\n"
"border: 1px solid #EEEEEE;\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"}\n"
"\n"
"*:focus{\n"
"background-color: #EEEEEE;\n"
"}\n"
"")
        self.search_input.setClearButtonEnabled(True)

        self.horizontalLayout_11.addWidget(self.search_input)

        self.search_btn = QPushButton(self.scrollAreaWidgetContents)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setCursor(QCursor(Qt.ArrowCursor))
        self.search_btn.setStyleSheet(u"*{\n"
"border: 1px solid #EEEEEE;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"}\n"
"\n"
"")
        self.search_btn.setIcon(icon5)
        self.search_btn.setIconSize(QSize(20, 20))
        self.search_btn.setCheckable(False)

        self.horizontalLayout_11.addWidget(self.search_btn)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 5, -1, 5)
        self.makineler_widget = QWidget(self.scrollAreaWidgetContents)
        self.makineler_widget.setObjectName(u"makineler_widget")
        self.makineler_widget.setMinimumSize(QSize(0, 40))
        self.makineler_widget.setStyleSheet(u"*{\n"
"border:none;\n"
"padding: 10px 5px;\n"
"height: 40px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color: #EEEEEE;\n"
"}")
        self.horizontalLayout_27 = QHBoxLayout(self.makineler_widget)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.makineler_fltr_label_btn = QPushButton(self.makineler_widget)
        self.makineler_fltr_label_btn.setObjectName(u"makineler_fltr_label_btn")
        sizePolicy.setHeightForWidth(self.makineler_fltr_label_btn.sizePolicy().hasHeightForWidth())
        self.makineler_fltr_label_btn.setSizePolicy(sizePolicy)
        self.makineler_fltr_label_btn.setFont(font3)
        self.makineler_fltr_label_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.makineler_fltr_label_btn.setStyleSheet(u"*{\n"
"border: none;\n"
"text-align: left;\n"
"padding-left: 5px;\n"
"height: 30px;\n"
"}")
        self.makineler_fltr_label_btn.setCheckable(True)

        self.horizontalLayout_26.addWidget(self.makineler_fltr_label_btn)

        self.horizontalSpacer_16 = QSpacerItem(0, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_16)

        self.makineler_fltr_icon_btn = QPushButton(self.makineler_widget)
        self.makineler_fltr_icon_btn.setObjectName(u"makineler_fltr_icon_btn")
        self.makineler_fltr_icon_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.makineler_fltr_icon_btn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.makineler_fltr_icon_btn.setStyleSheet(u"border: none;\n"
"height: 30px;")
        self.makineler_fltr_icon_btn.setIcon(icon6)
        self.makineler_fltr_icon_btn.setCheckable(True)

        self.horizontalLayout_26.addWidget(self.makineler_fltr_icon_btn)


        self.horizontalLayout_27.addLayout(self.horizontalLayout_26)


        self.verticalLayout_13.addWidget(self.makineler_widget)

        self.makineler_check_boxes = QWidget(self.scrollAreaWidgetContents)
        self.makineler_check_boxes.setObjectName(u"makineler_check_boxes")
        self.makineler_check_boxes.setMinimumSize(QSize(0, 200))
        self.makineler_check_boxes.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.makineler_check_boxes.setStyleSheet(u"background-color: #EEEEEE;")
        self.gridLayout = QGridLayout(self.makineler_check_boxes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.makineler_checkBox_KZ_1 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_KZ_1.setObjectName(u"makineler_checkBox_KZ_1")

        self.gridLayout.addWidget(self.makineler_checkBox_KZ_1, 0, 0, 1, 1)

        self.makineler_checkBox_KZ_XL_1 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_KZ_XL_1.setObjectName(u"makineler_checkBox_KZ_XL_1")

        self.gridLayout.addWidget(self.makineler_checkBox_KZ_XL_1, 0, 1, 1, 1)

        self.makineler_checkBox_KZ_2 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_KZ_2.setObjectName(u"makineler_checkBox_KZ_2")

        self.gridLayout.addWidget(self.makineler_checkBox_KZ_2, 1, 0, 1, 1)

        self.makineler_checkBox_KZ_XL_2 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_KZ_XL_2.setObjectName(u"makineler_checkBox_KZ_XL_2")

        self.gridLayout.addWidget(self.makineler_checkBox_KZ_XL_2, 1, 1, 1, 1)

        self.makineler_checkBox_KZ_3 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_KZ_3.setObjectName(u"makineler_checkBox_KZ_3")

        self.gridLayout.addWidget(self.makineler_checkBox_KZ_3, 2, 0, 1, 1)

        self.makineler_checkBox_KZ_XL_3 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_KZ_XL_3.setObjectName(u"makineler_checkBox_KZ_XL_3")

        self.gridLayout.addWidget(self.makineler_checkBox_KZ_XL_3, 2, 1, 1, 1)

        self.makineler_checkBox_KZ_4 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_KZ_4.setObjectName(u"makineler_checkBox_KZ_4")

        self.gridLayout.addWidget(self.makineler_checkBox_KZ_4, 3, 0, 1, 1)

        self.makineler_checkBox_KZ_XL_4 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_KZ_XL_4.setObjectName(u"makineler_checkBox_KZ_XL_4")

        self.gridLayout.addWidget(self.makineler_checkBox_KZ_XL_4, 3, 1, 1, 1)

        self.makineler_checkBox_KZ_5 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_KZ_5.setObjectName(u"makineler_checkBox_KZ_5")

        self.gridLayout.addWidget(self.makineler_checkBox_KZ_5, 4, 0, 1, 1)

        self.makineler_checkBox_ERL_1 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_ERL_1.setObjectName(u"makineler_checkBox_ERL_1")

        self.gridLayout.addWidget(self.makineler_checkBox_ERL_1, 4, 1, 1, 1)

        self.makineler_checkBox_KZ_6 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_KZ_6.setObjectName(u"makineler_checkBox_KZ_6")

        self.gridLayout.addWidget(self.makineler_checkBox_KZ_6, 5, 0, 1, 1)

        self.makineler_checkBox_ERL_2 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_ERL_2.setObjectName(u"makineler_checkBox_ERL_2")

        self.gridLayout.addWidget(self.makineler_checkBox_ERL_2, 5, 1, 1, 1)

        self.makineler_checkBox_KZ_7 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_KZ_7.setObjectName(u"makineler_checkBox_KZ_7")

        self.gridLayout.addWidget(self.makineler_checkBox_KZ_7, 6, 0, 1, 1)

        self.makineler_checkBox_ERL_3 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_ERL_3.setObjectName(u"makineler_checkBox_ERL_3")

        self.gridLayout.addWidget(self.makineler_checkBox_ERL_3, 6, 1, 1, 1)

        self.makineler_checkBox_KZ_8 = QCheckBox(self.makineler_check_boxes)
        self.makineler_checkBox_KZ_8.setObjectName(u"makineler_checkBox_KZ_8")

        self.gridLayout.addWidget(self.makineler_checkBox_KZ_8, 7, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.makineler_check_boxes)

        self.kalip_genisligi_widget = QWidget(self.scrollAreaWidgetContents)
        self.kalip_genisligi_widget.setObjectName(u"kalip_genisligi_widget")
        self.kalip_genisligi_widget.setMinimumSize(QSize(0, 40))
        self.kalip_genisligi_widget.setStyleSheet(u"*{\n"
"border:none;\n"
"padding: 10px 5px;\n"
"height: 40px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color: #EEEEEE;\n"
"}")
        self.horizontalLayout_29 = QHBoxLayout(self.kalip_genisligi_widget)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.kalip_genisligi_fltr_label_btn = QPushButton(self.kalip_genisligi_widget)
        self.kalip_genisligi_fltr_label_btn.setObjectName(u"kalip_genisligi_fltr_label_btn")
        sizePolicy.setHeightForWidth(self.kalip_genisligi_fltr_label_btn.sizePolicy().hasHeightForWidth())
        self.kalip_genisligi_fltr_label_btn.setSizePolicy(sizePolicy)
        self.kalip_genisligi_fltr_label_btn.setFont(font3)
        self.kalip_genisligi_fltr_label_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.kalip_genisligi_fltr_label_btn.setStyleSheet(u"*{\n"
"border: none;\n"
"text-align: left;\n"
"padding-left: 5px;\n"
"height: 30px;\n"
"}")
        self.kalip_genisligi_fltr_label_btn.setCheckable(True)

        self.horizontalLayout_28.addWidget(self.kalip_genisligi_fltr_label_btn)

        self.horizontalSpacer_17 = QSpacerItem(0, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_17)

        self.kalip_genisligi_fltr_icon_btn = QPushButton(self.kalip_genisligi_widget)
        self.kalip_genisligi_fltr_icon_btn.setObjectName(u"kalip_genisligi_fltr_icon_btn")
        self.kalip_genisligi_fltr_icon_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.kalip_genisligi_fltr_icon_btn.setStyleSheet(u"border: none;\n"
"height: 30px;")
        self.kalip_genisligi_fltr_icon_btn.setIcon(icon6)
        self.kalip_genisligi_fltr_icon_btn.setCheckable(True)

        self.horizontalLayout_28.addWidget(self.kalip_genisligi_fltr_icon_btn)


        self.horizontalLayout_29.addLayout(self.horizontalLayout_28)


        self.verticalLayout_13.addWidget(self.kalip_genisligi_widget)

        self.kalip_genisligi_check_boxes = QWidget(self.scrollAreaWidgetContents)
        self.kalip_genisligi_check_boxes.setObjectName(u"kalip_genisligi_check_boxes")
        self.kalip_genisligi_check_boxes.setMinimumSize(QSize(0, 60))
        self.kalip_genisligi_check_boxes.setStyleSheet(u"background-color: #EEEEEE;")
        self.gridLayout_3 = QGridLayout(self.kalip_genisligi_check_boxes)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.kalip_genisligi_checkBox_S = QCheckBox(self.kalip_genisligi_check_boxes)
        self.kalip_genisligi_checkBox_S.setObjectName(u"kalip_genisligi_checkBox_S")

        self.gridLayout_3.addWidget(self.kalip_genisligi_checkBox_S, 0, 0, 1, 1)

        self.kalip_genisligi_checkBox_M = QCheckBox(self.kalip_genisligi_check_boxes)
        self.kalip_genisligi_checkBox_M.setObjectName(u"kalip_genisligi_checkBox_M")

        self.gridLayout_3.addWidget(self.kalip_genisligi_checkBox_M, 0, 1, 1, 1)

        self.kalip_genisligi_checkBox_L = QCheckBox(self.kalip_genisligi_check_boxes)
        self.kalip_genisligi_checkBox_L.setObjectName(u"kalip_genisligi_checkBox_L")

        self.gridLayout_3.addWidget(self.kalip_genisligi_checkBox_L, 1, 0, 1, 1)

        self.kalip_genisligi_checkBox_ERL = QCheckBox(self.kalip_genisligi_check_boxes)
        self.kalip_genisligi_checkBox_ERL.setObjectName(u"kalip_genisligi_checkBox_ERL")

        self.gridLayout_3.addWidget(self.kalip_genisligi_checkBox_ERL, 1, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.kalip_genisligi_check_boxes)

        self.type_widget = QWidget(self.scrollAreaWidgetContents)
        self.type_widget.setObjectName(u"type_widget")
        self.type_widget.setMinimumSize(QSize(0, 40))
        self.type_widget.setStyleSheet(u"*{\n"
"border:none;\n"
"padding: 10px 5px;\n"
"height: 40px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color: #EEEEEE;\n"
"}")
        self.horizontalLayout_15 = QHBoxLayout(self.type_widget)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.type_fltr_label_btn = QPushButton(self.type_widget)
        self.type_fltr_label_btn.setObjectName(u"type_fltr_label_btn")
        sizePolicy.setHeightForWidth(self.type_fltr_label_btn.sizePolicy().hasHeightForWidth())
        self.type_fltr_label_btn.setSizePolicy(sizePolicy)
        self.type_fltr_label_btn.setFont(font3)
        self.type_fltr_label_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.type_fltr_label_btn.setStyleSheet(u"*{\n"
"border: none;\n"
"text-align: left;\n"
"padding-left: 5px;\n"
"height: 30px;\n"
"}")
        self.type_fltr_label_btn.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.type_fltr_label_btn)

        self.horizontalSpacer_7 = QSpacerItem(0, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.type_fltr_icon_btn = QPushButton(self.type_widget)
        self.type_fltr_icon_btn.setObjectName(u"type_fltr_icon_btn")
        self.type_fltr_icon_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.type_fltr_icon_btn.setStyleSheet(u"border: none;\n"
"height: 30px;")
        self.type_fltr_icon_btn.setIcon(icon6)
        self.type_fltr_icon_btn.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.type_fltr_icon_btn)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)


        self.verticalLayout_13.addWidget(self.type_widget)

        self.type_check_boxes = QWidget(self.scrollAreaWidgetContents)
        self.type_check_boxes.setObjectName(u"type_check_boxes")
        self.type_check_boxes.setMinimumSize(QSize(0, 80))
        self.type_check_boxes.setStyleSheet(u"background-color: #EEEEEE;")
        self.gridLayout_5 = QGridLayout(self.type_check_boxes)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.type_checkBox_top = QCheckBox(self.type_check_boxes)
        self.type_checkBox_top.setObjectName(u"type_checkBox_top")

        self.gridLayout_5.addWidget(self.type_checkBox_top, 0, 0, 1, 1)

        self.type_checkBox_bottom = QCheckBox(self.type_check_boxes)
        self.type_checkBox_bottom.setObjectName(u"type_checkBox_bottom")

        self.gridLayout_5.addWidget(self.type_checkBox_bottom, 0, 1, 1, 1)

        self.type_checkBox_middle = QCheckBox(self.type_check_boxes)
        self.type_checkBox_middle.setObjectName(u"type_checkBox_middle")

        self.gridLayout_5.addWidget(self.type_checkBox_middle, 2, 0, 1, 1)

        self.type_checkBox_front = QCheckBox(self.type_check_boxes)
        self.type_checkBox_front.setObjectName(u"type_checkBox_front")

        self.gridLayout_5.addWidget(self.type_checkBox_front, 1, 0, 1, 1)

        self.type_checkBox_back = QCheckBox(self.type_check_boxes)
        self.type_checkBox_back.setObjectName(u"type_checkBox_back")

        self.gridLayout_5.addWidget(self.type_checkBox_back, 1, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.type_check_boxes)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.verticalSpacer_4 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_4)

        self.uygula_widget = QWidget(self.scrollAreaWidgetContents)
        self.uygula_widget.setObjectName(u"uygula_widget")
        self.uygula_widget.setMinimumSize(QSize(0, 30))
        self.uygula_widget.setStyleSheet(u"")
        self.horizontalLayout_21 = QHBoxLayout(self.uygula_widget)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, -1, -1, 3)
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_12)

        self.uygula_btn = QPushButton(self.uygula_widget)
        self.uygula_btn.setObjectName(u"uygula_btn")
        self.uygula_btn.setMinimumSize(QSize(0, 30))
        self.uygula_btn.setFont(font1)
        self.uygula_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.uygula_btn.setStyleSheet(u"*{\n"
"border: none;\n"
"border-radius:  4px;\n"
"width: 90px;\n"
"height: 30px;\n"
"background-color: #222831;\n"
"color: #fff;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color: #31363f;\n"
"}")
        self.uygula_btn.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.uygula_btn)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_13)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_20)


        self.verticalLayout_14.addWidget(self.uygula_widget)

        self.planned_fltr_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_6.addWidget(self.planned_fltr_scroll_area)

        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, 10)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.arrange_table_btn = QPushButton(self.planned_orders)
        self.arrange_table_btn.setObjectName(u"arrange_table_btn")
        self.arrange_table_btn.setFont(font1)
        self.arrange_table_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.arrange_table_btn.setStyleSheet(u"*{\n"
"border: none;\n"
"border-radius:  4px;\n"
"width: 110px;\n"
"height: 30px;\n"
"background-color: #222831;\n"
"color: #fff;\n"
"padding-right: 5px;\n"
"padding-left: 5px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color: #31363f;\n"
"}")
        self.arrange_table_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.arrange_table_btn)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.planned_orders)
        self.no_planned_order_page = QWidget()
        self.no_planned_order_page.setObjectName(u"no_planned_order_page")
        self.horizontalLayout_37 = QHBoxLayout(self.no_planned_order_page)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_21)

        self.no_planned_order_label = QLabel(self.no_planned_order_page)
        self.no_planned_order_label.setObjectName(u"no_planned_order_label")
        font5 = QFont()
        font5.setPointSize(14)
        self.no_planned_order_label.setFont(font5)

        self.horizontalLayout_36.addWidget(self.no_planned_order_label)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_22)


        self.horizontalLayout_37.addLayout(self.horizontalLayout_36)

        self.stackedWidget.addWidget(self.no_planned_order_page)
        self.arrange_tables_page = QWidget()
        self.arrange_tables_page.setObjectName(u"arrange_tables_page")
        self.verticalLayout_58 = QVBoxLayout(self.arrange_tables_page)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setSpacing(10)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(5, -1, 5, -1)
        self.arrange_table_label = QLabel(self.arrange_tables_page)
        self.arrange_table_label.setObjectName(u"arrange_table_label")
        self.arrange_table_label.setFont(font2)

        self.verticalLayout_57.addWidget(self.arrange_table_label)

        self.arranged_table = QTableView(self.arrange_tables_page)
        self.arranged_table.setObjectName(u"arranged_table")
        self.arranged_table.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.arranged_table.horizontalHeader().setMinimumSectionSize(225)
        self.arranged_table.horizontalHeader().setDefaultSectionSize(250)
        self.arranged_table.verticalHeader().setVisible(False)
        self.arranged_table.verticalHeader().setDefaultSectionSize(24)

        self.verticalLayout_57.addWidget(self.arranged_table)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, 10, -1, 10)
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_23)

        self.kaydet_btn = QPushButton(self.arrange_tables_page)
        self.kaydet_btn.setObjectName(u"kaydet_btn")
        self.kaydet_btn.setFont(font1)
        self.kaydet_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.kaydet_btn.setStyleSheet(u"*{\n"
"border: none;\n"
"border-radius:  4px;\n"
"width: 90px;\n"
"height: 30px;\n"
"background-color: #222831;\n"
"color: #fff;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color: #31363f;\n"
"}")
        self.kaydet_btn.setCheckable(True)

        self.horizontalLayout_38.addWidget(self.kaydet_btn)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_24)


        self.verticalLayout_57.addLayout(self.horizontalLayout_38)


        self.verticalLayout_58.addLayout(self.verticalLayout_57)

        self.stackedWidget.addWidget(self.arrange_tables_page)
        self.stok_raporlari = QWidget()
        self.stok_raporlari.setObjectName(u"stok_raporlari")
        self.stok_raporlari.setStyleSheet(u"")
        self.verticalLayout_60 = QVBoxLayout(self.stok_raporlari)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setSpacing(10)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(5, -1, 5, -1)
        self.label = QLabel(self.stok_raporlari)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")

        self.verticalLayout_59.addWidget(self.label)

        self.stok_tablosu = QTableView(self.stok_raporlari)
        self.stok_tablosu.setObjectName(u"stok_tablosu")
        self.stok_tablosu.setStyleSheet(u"")
        self.stok_tablosu.horizontalHeader().setMinimumSectionSize(150)

        self.verticalLayout_59.addWidget(self.stok_tablosu)


        self.verticalLayout_60.addLayout(self.verticalLayout_59)

        self.stackedWidget.addWidget(self.stok_raporlari)
        self.deneme_page = QWidget()
        self.deneme_page.setObjectName(u"deneme_page")
        self.deneme_page.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.deneme_page)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.horizontalLayout_9.addWidget(self.body_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.change_btn.toggled.connect(self.icon_only_widget.setVisible)
        self.change_btn.toggled.connect(self.full_menu_widget.setHidden)
        self.menu_unplanned_btn.toggled.connect(self.menu_unplanned_btn_2.setChecked)
        self.menu_stock_btn.toggled.connect(self.menu_stock_btn_2.setChecked)
        self.menu_unplanned_btn_2.toggled.connect(self.menu_unplanned_btn.setChecked)
        self.menu_stock_btn_2.toggled.connect(self.menu_stock_btn.setChecked)
        self.menu_planned_btn.toggled.connect(self.menu_planned_btn_2.setChecked)
        self.menu_planned_btn_2.toggled.connect(self.menu_planned_btn.setChecked)
        self.makineler_fltr_label_btn.toggled.connect(self.makineler_check_boxes.setVisible)
        self.makineler_fltr_icon_btn.toggled.connect(self.makineler_check_boxes.setVisible)
        self.makineler_fltr_label_btn.toggled.connect(self.makineler_fltr_icon_btn.setChecked)
        self.makineler_fltr_icon_btn.toggled.connect(self.makineler_fltr_label_btn.setChecked)
        self.kalip_genisligi_fltr_label_btn.toggled.connect(self.kalip_genisligi_check_boxes.setVisible)
        self.kalip_genisligi_fltr_icon_btn.toggled.connect(self.kalip_genisligi_check_boxes.setVisible)
        self.kalip_genisligi_fltr_label_btn.toggled.connect(self.kalip_genisligi_fltr_icon_btn.setChecked)
        self.kalip_genisligi_fltr_icon_btn.toggled.connect(self.kalip_genisligi_fltr_label_btn.setChecked)
        self.kalip_genisligi_fltr_label_btn_2.toggled.connect(self.kalip_genisligi_check_boxes_2.setVisible)
        self.kalip_genisligi_fltr_icon_btn_2.toggled.connect(self.kalip_genisligi_check_boxes_2.setVisible)
        self.kalip_genisligi_fltr_label_btn_2.toggled.connect(self.kalip_genisligi_fltr_icon_btn_2.setChecked)
        self.kalip_genisligi_fltr_icon_btn_2.toggled.connect(self.kalip_genisligi_fltr_label_btn_2.setChecked)
        self.montaj_ihtiyac_fltr_label_btn_2.toggled.connect(self.montaj_ihtiyac_calendar_widget_2.setVisible)
        self.montaj_ihtiyac_fltr_icon_btn_2.toggled.connect(self.montaj_ihtiyac_calendar_widget_2.setVisible)
        self.montaj_ihtiyac_fltr_label_btn_2.toggled.connect(self.montaj_ihtiyac_fltr_icon_btn_2.setChecked)
        self.montaj_ihtiyac_fltr_icon_btn_2.toggled.connect(self.montaj_ihtiyac_fltr_label_btn_2.setChecked)
        self.type_fltr_label_btn_2.toggled.connect(self.type_check_boxes_2.setVisible)
        self.type_fltr_icon_btn_2.toggled.connect(self.type_check_boxes_2.setVisible)
        self.type_fltr_label_btn_2.toggled.connect(self.type_fltr_icon_btn_2.setChecked)
        self.type_fltr_icon_btn_2.toggled.connect(self.type_fltr_label_btn_2.setChecked)
        self.type_fltr_label_btn.toggled.connect(self.type_check_boxes.setVisible)
        self.type_fltr_icon_btn.toggled.connect(self.type_check_boxes.setVisible)
        self.type_fltr_label_btn.toggled.connect(self.type_fltr_icon_btn.setChecked)
        self.type_fltr_icon_btn.toggled.connect(self.type_fltr_label_btn.setChecked)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_img.setText("")
        self.menu_unplanned_btn.setText("")
        self.menu_planned_btn.setText("")
        self.menu_stock_btn.setText("")
        self.vestel_logo.setText("")
        self.logo_img_2.setText("")
        self.logo_name.setText(QCoreApplication.translate("MainWindow", u"StyroPlan", None))
        self.menu_unplanned_btn_2.setText(QCoreApplication.translate("MainWindow", u"Planlanmam\u0131\u015f Sipari\u015fler", None))
        self.menu_planned_btn_2.setText(QCoreApplication.translate("MainWindow", u"Planlanm\u0131\u015f Sipari\u015fler", None))
        self.menu_stock_btn_2.setText(QCoreApplication.translate("MainWindow", u"Stok Raporlar\u0131 ", None))
        self.vestel_logo_2.setText(QCoreApplication.translate("MainWindow", u" i\u00e7in geli\u015ftirilmi\u015ftir", None))
        self.change_btn.setText("")
        self.planlanmamis_siparis_label.setText(QCoreApplication.translate("MainWindow", u"Planlanmam\u0131\u015f Strafor Sipari\u015fleri", None))
        self.tarihler_label_2.setText(QCoreApplication.translate("MainWindow", u"Tarihler", None))
        self.filters_label_2.setText(QCoreApplication.translate("MainWindow", u"Filtreler", None))
        self.search_input_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Par\u00e7a Kodu Ara...", None))
        self.search_btn_2.setText("")
        self.kalip_genisligi_fltr_label_btn_2.setText(QCoreApplication.translate("MainWindow", u"Kal\u0131p Geni\u015fli\u011fi", None))
        self.kalip_genisligi_fltr_icon_btn_2.setText("")
        self.kalip_genisligi_checkBox_S_2.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.kalip_genisligi_checkBox_M_2.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.kalip_genisligi_checkBox_L_2.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.kalip_genisligi_checkBox_ERL_2.setText(QCoreApplication.translate("MainWindow", u"ERL", None))
        self.montaj_ihtiyac_fltr_label_btn_2.setText(QCoreApplication.translate("MainWindow", u"Montaj \u0130htiya\u00e7 Tarihi", None))
        self.montaj_ihtiyac_fltr_icon_btn_2.setText("")
        self.type_fltr_label_btn_2.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.type_fltr_icon_btn_2.setText("")
        self.type_checkBox_bottom_2.setText(QCoreApplication.translate("MainWindow", u"BOTTOM", None))
        self.type_checkBox_top_2.setText(QCoreApplication.translate("MainWindow", u"TOP", None))
        self.type_checkBox_middle_2.setText(QCoreApplication.translate("MainWindow", u"MIDDLE", None))
        self.type_checkBox_front_2.setText(QCoreApplication.translate("MainWindow", u"FRONT", None))
        self.type_checkBox_back_2.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.uygula_btn_2.setText(QCoreApplication.translate("MainWindow", u"Uygula", None))
        self.planla_btn.setText(QCoreApplication.translate("MainWindow", u"Planla", None))
        self.planlanmis_siparis_label.setText(QCoreApplication.translate("MainWindow", u"Planlanm\u0131\u015f Strafor Sipari\u015fleri", None))
        self.tarihler_label.setText(QCoreApplication.translate("MainWindow", u"Tarihler", None))
        self.KZ_1_label.setText(QCoreApplication.translate("MainWindow", u"KZ-1", None))
        self.KZ_2_label.setText(QCoreApplication.translate("MainWindow", u"KZ-2", None))
        self.KZ_3_label.setText(QCoreApplication.translate("MainWindow", u"KZ-3", None))
        self.KZ_4_label.setText(QCoreApplication.translate("MainWindow", u"KZ-4", None))
        self.KZ_5_label.setText(QCoreApplication.translate("MainWindow", u"KZ-5", None))
        self.KZ_6_label.setText(QCoreApplication.translate("MainWindow", u"KZ-6", None))
        self.KZ_7_label.setText(QCoreApplication.translate("MainWindow", u"KZ-7", None))
        self.KZ_8_label.setText(QCoreApplication.translate("MainWindow", u"KZ-8", None))
        self.KZ_XL_1_label.setText(QCoreApplication.translate("MainWindow", u"KZ-XL-1", None))
        self.KZ_XL_2_label.setText(QCoreApplication.translate("MainWindow", u"KZ-XL-2", None))
        self.KZ_XL_3_label.setText(QCoreApplication.translate("MainWindow", u"KZ-XL-3", None))
        self.KZ_XL_4_label.setText(QCoreApplication.translate("MainWindow", u"KZ-XL-4", None))
        self.ERL_1_label.setText(QCoreApplication.translate("MainWindow", u"ERL-1", None))
        self.ERL_2_label.setText(QCoreApplication.translate("MainWindow", u"ERL-2", None))
        self.ERL_3_label.setText(QCoreApplication.translate("MainWindow", u"ERL-3", None))
        self.filters_label.setText(QCoreApplication.translate("MainWindow", u"Filtreler", None))
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Par\u00e7a Kodu Ara...", None))
        self.search_btn.setText("")
        self.makineler_fltr_label_btn.setText(QCoreApplication.translate("MainWindow", u"Makineler", None))
        self.makineler_fltr_icon_btn.setText("")
        self.makineler_checkBox_KZ_1.setText(QCoreApplication.translate("MainWindow", u"KZ-1", None))
        self.makineler_checkBox_KZ_XL_1.setText(QCoreApplication.translate("MainWindow", u"KZ-XL-1", None))
        self.makineler_checkBox_KZ_2.setText(QCoreApplication.translate("MainWindow", u"KZ-2", None))
        self.makineler_checkBox_KZ_XL_2.setText(QCoreApplication.translate("MainWindow", u"KZ-XL-2", None))
        self.makineler_checkBox_KZ_3.setText(QCoreApplication.translate("MainWindow", u"KZ-3", None))
        self.makineler_checkBox_KZ_XL_3.setText(QCoreApplication.translate("MainWindow", u"KZ-XL-3", None))
        self.makineler_checkBox_KZ_4.setText(QCoreApplication.translate("MainWindow", u"KZ-4", None))
        self.makineler_checkBox_KZ_XL_4.setText(QCoreApplication.translate("MainWindow", u"KZ-XL-4", None))
        self.makineler_checkBox_KZ_5.setText(QCoreApplication.translate("MainWindow", u"KZ-5", None))
        self.makineler_checkBox_ERL_1.setText(QCoreApplication.translate("MainWindow", u"ERL-1", None))
        self.makineler_checkBox_KZ_6.setText(QCoreApplication.translate("MainWindow", u"KZ-6", None))
        self.makineler_checkBox_ERL_2.setText(QCoreApplication.translate("MainWindow", u"ERL-2", None))
        self.makineler_checkBox_KZ_7.setText(QCoreApplication.translate("MainWindow", u"KZ-7", None))
        self.makineler_checkBox_ERL_3.setText(QCoreApplication.translate("MainWindow", u"ERL-3", None))
        self.makineler_checkBox_KZ_8.setText(QCoreApplication.translate("MainWindow", u"KZ-8", None))
        self.kalip_genisligi_fltr_label_btn.setText(QCoreApplication.translate("MainWindow", u"Kal\u0131p Geni\u015fli\u011fi", None))
        self.kalip_genisligi_fltr_icon_btn.setText("")
        self.kalip_genisligi_checkBox_S.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.kalip_genisligi_checkBox_M.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.kalip_genisligi_checkBox_L.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.kalip_genisligi_checkBox_ERL.setText(QCoreApplication.translate("MainWindow", u"ERL", None))
        self.type_fltr_label_btn.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.type_fltr_icon_btn.setText("")
        self.type_checkBox_top.setText(QCoreApplication.translate("MainWindow", u"TOP", None))
        self.type_checkBox_bottom.setText(QCoreApplication.translate("MainWindow", u"BOTTOM", None))
        self.type_checkBox_middle.setText(QCoreApplication.translate("MainWindow", u"MIDDLE", None))
        self.type_checkBox_front.setText(QCoreApplication.translate("MainWindow", u"FRONT", None))
        self.type_checkBox_back.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.uygula_btn.setText(QCoreApplication.translate("MainWindow", u"Uygula", None))
        self.arrange_table_btn.setText(QCoreApplication.translate("MainWindow", u"D\u0131\u015fa Aktar", None))
        self.no_planned_order_label.setText(QCoreApplication.translate("MainWindow", u"Hen\u00fcz planlanm\u0131\u015f sipari\u015f bulunmamaktad\u0131r. ", None))
        self.arrange_table_label.setText(QCoreApplication.translate("MainWindow", u"Dilerseniz sat\u0131rlar\u0131 s\u00fcr\u00fckleyerek planda de\u011fi\u015fiklik yapabilirsiniz.", None))
        self.kaydet_btn.setText(QCoreApplication.translate("MainWindow", u"Kaydet", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stok Raporlar\u0131", None))
    # retranslateUi
