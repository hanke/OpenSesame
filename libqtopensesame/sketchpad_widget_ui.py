# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/sketchpad_widget.ui'
#
# Created: Fri Mar 25 15:35:52 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(851, 598)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(Form)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtGui.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3.addWidget(self.widget_2)
        self.widget_7 = QtGui.QWidget(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_4 = QtGui.QFrame(self.widget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtGui.QGridLayout(self.frame_4)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(4, 4, 4, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_line = QtGui.QPushButton(self.frame_4)
        self.button_line.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/line_large.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_line.setIcon(icon)
        self.button_line.setIconSize(QtCore.QSize(32, 32))
        self.button_line.setCheckable(True)
        self.button_line.setChecked(True)
        self.button_line.setFlat(True)
        self.button_line.setObjectName("button_line")
        self.gridLayout.addWidget(self.button_line, 0, 0, 1, 1)
        self.button_arrow = QtGui.QPushButton(self.frame_4)
        self.button_arrow.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/arrow_large.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_arrow.setIcon(icon1)
        self.button_arrow.setIconSize(QtCore.QSize(32, 32))
        self.button_arrow.setCheckable(True)
        self.button_arrow.setFlat(True)
        self.button_arrow.setObjectName("button_arrow")
        self.gridLayout.addWidget(self.button_arrow, 0, 1, 1, 1)
        self.button_textline = QtGui.QPushButton(self.frame_4)
        self.button_textline.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/textline_large.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_textline.setIcon(icon2)
        self.button_textline.setIconSize(QtCore.QSize(32, 32))
        self.button_textline.setCheckable(True)
        self.button_textline.setFlat(True)
        self.button_textline.setObjectName("button_textline")
        self.gridLayout.addWidget(self.button_textline, 0, 2, 1, 1)
        self.button_image = QtGui.QPushButton(self.frame_4)
        self.button_image.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/image_large.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_image.setIcon(icon3)
        self.button_image.setIconSize(QtCore.QSize(32, 32))
        self.button_image.setCheckable(True)
        self.button_image.setFlat(True)
        self.button_image.setObjectName("button_image")
        self.gridLayout.addWidget(self.button_image, 0, 3, 1, 1)
        self.button_gabor = QtGui.QPushButton(self.frame_4)
        self.button_gabor.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/gabor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_gabor.setIcon(icon4)
        self.button_gabor.setIconSize(QtCore.QSize(32, 32))
        self.button_gabor.setCheckable(True)
        self.button_gabor.setFlat(True)
        self.button_gabor.setObjectName("button_gabor")
        self.gridLayout.addWidget(self.button_gabor, 0, 4, 1, 1)
        self.button_rect = QtGui.QPushButton(self.frame_4)
        self.button_rect.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/rectangle_large.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_rect.setIcon(icon5)
        self.button_rect.setIconSize(QtCore.QSize(32, 32))
        self.button_rect.setCheckable(True)
        self.button_rect.setFlat(True)
        self.button_rect.setObjectName("button_rect")
        self.gridLayout.addWidget(self.button_rect, 1, 0, 1, 1)
        self.button_ellipse = QtGui.QPushButton(self.frame_4)
        self.button_ellipse.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/ellipse_large.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_ellipse.setIcon(icon6)
        self.button_ellipse.setIconSize(QtCore.QSize(32, 32))
        self.button_ellipse.setCheckable(True)
        self.button_ellipse.setFlat(True)
        self.button_ellipse.setObjectName("button_ellipse")
        self.gridLayout.addWidget(self.button_ellipse, 1, 1, 1, 1)
        self.button_circle = QtGui.QPushButton(self.frame_4)
        self.button_circle.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/circle_large.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_circle.setIcon(icon7)
        self.button_circle.setIconSize(QtCore.QSize(32, 32))
        self.button_circle.setCheckable(True)
        self.button_circle.setFlat(True)
        self.button_circle.setObjectName("button_circle")
        self.gridLayout.addWidget(self.button_circle, 1, 2, 1, 1)
        self.button_fixdot = QtGui.QPushButton(self.frame_4)
        self.button_fixdot.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/fixdot_large.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_fixdot.setIcon(icon8)
        self.button_fixdot.setIconSize(QtCore.QSize(32, 32))
        self.button_fixdot.setCheckable(True)
        self.button_fixdot.setFlat(True)
        self.button_fixdot.setObjectName("button_fixdot")
        self.gridLayout.addWidget(self.button_fixdot, 1, 3, 1, 1)
        self.widget_5 = QtGui.QWidget(self.frame_4)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout.addWidget(self.widget_5, 2, 1, 1, 1)
        self.button_noise_patch = QtGui.QPushButton(self.frame_4)
        self.button_noise_patch.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/noise_patch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_noise_patch.setIcon(icon9)
        self.button_noise_patch.setIconSize(QtCore.QSize(32, 32))
        self.button_noise_patch.setCheckable(True)
        self.button_noise_patch.setFlat(True)
        self.button_noise_patch.setObjectName("button_noise_patch")
        self.gridLayout.addWidget(self.button_noise_patch, 1, 4, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_4)
        self.frame_5 = QtGui.QFrame(self.widget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_2.setMargin(4)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_color = QtGui.QLabel(self.frame_5)
        self.label_color.setObjectName("label_color")
        self.gridLayout_2.addWidget(self.label_color, 2, 0, 1, 1)
        self.edit_color = QtGui.QLineEdit(self.frame_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_color.sizePolicy().hasHeightForWidth())
        self.edit_color.setSizePolicy(sizePolicy)
        self.edit_color.setObjectName("edit_color")
        self.gridLayout_2.addWidget(self.edit_color, 2, 1, 1, 1)
        self.label_penwidth = QtGui.QLabel(self.frame_5)
        self.label_penwidth.setObjectName("label_penwidth")
        self.gridLayout_2.addWidget(self.label_penwidth, 3, 0, 1, 1)
        self.spin_penwidth = QtGui.QSpinBox(self.frame_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_penwidth.sizePolicy().hasHeightForWidth())
        self.spin_penwidth.setSizePolicy(sizePolicy)
        self.spin_penwidth.setMinimum(1)
        self.spin_penwidth.setMaximum(99)
        self.spin_penwidth.setObjectName("spin_penwidth")
        self.gridLayout_2.addWidget(self.spin_penwidth, 3, 1, 1, 1)
        self.label_arrow_size = QtGui.QLabel(self.frame_5)
        self.label_arrow_size.setObjectName("label_arrow_size")
        self.gridLayout_2.addWidget(self.label_arrow_size, 4, 0, 1, 1)
        self.spin_arrow_size = QtGui.QSpinBox(self.frame_5)
        self.spin_arrow_size.setProperty("value", 10)
        self.spin_arrow_size.setObjectName("spin_arrow_size")
        self.gridLayout_2.addWidget(self.spin_arrow_size, 4, 1, 1, 1)
        self.label_scale = QtGui.QLabel(self.frame_5)
        self.label_scale.setObjectName("label_scale")
        self.gridLayout_2.addWidget(self.label_scale, 5, 0, 1, 1)
        self.spin_scale = QtGui.QDoubleSpinBox(self.frame_5)
        self.spin_scale.setDecimals(0)
        self.spin_scale.setMinimum(1.0)
        self.spin_scale.setMaximum(1000.0)
        self.spin_scale.setProperty("value", 100.0)
        self.spin_scale.setObjectName("spin_scale")
        self.gridLayout_2.addWidget(self.spin_scale, 5, 1, 1, 1)
        self.label_font_family = QtGui.QLabel(self.frame_5)
        self.label_font_family.setObjectName("label_font_family")
        self.gridLayout_2.addWidget(self.label_font_family, 6, 0, 1, 1)
        self.combobox_font_family = QtGui.QComboBox(self.frame_5)
        self.combobox_font_family.setObjectName("combobox_font_family")
        self.combobox_font_family.addItem("")
        self.combobox_font_family.addItem("")
        self.combobox_font_family.addItem("")
        self.gridLayout_2.addWidget(self.combobox_font_family, 6, 1, 1, 1)
        self.label_font_size = QtGui.QLabel(self.frame_5)
        self.label_font_size.setObjectName("label_font_size")
        self.gridLayout_2.addWidget(self.label_font_size, 7, 0, 1, 1)
        self.spin_font_size = QtGui.QSpinBox(self.frame_5)
        self.spin_font_size.setMinimum(1)
        self.spin_font_size.setProperty("value", 18)
        self.spin_font_size.setObjectName("spin_font_size")
        self.gridLayout_2.addWidget(self.spin_font_size, 7, 1, 1, 1)
        self.checkbox_fill = QtGui.QCheckBox(self.frame_5)
        self.checkbox_fill.setObjectName("checkbox_fill")
        self.gridLayout_2.addWidget(self.checkbox_fill, 8, 0, 1, 1)
        self.checkbox_center = QtGui.QCheckBox(self.frame_5)
        self.checkbox_center.setChecked(True)
        self.checkbox_center.setObjectName("checkbox_center")
        self.gridLayout_2.addWidget(self.checkbox_center, 9, 0, 1, 1)
        self.widget_4 = QtGui.QWidget(self.frame_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_2.addWidget(self.widget_4, 10, 0, 1, 1)
        self.label_options = QtGui.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_options.setFont(font)
        self.label_options.setObjectName("label_options")
        self.gridLayout_2.addWidget(self.label_options, 0, 0, 1, 2)
        self.edit_show_if = QtGui.QLineEdit(self.frame_5)
        self.edit_show_if.setObjectName("edit_show_if")
        self.gridLayout_2.addWidget(self.edit_show_if, 1, 1, 1, 1)
        self.label_show_if = QtGui.QLabel(self.frame_5)
        self.label_show_if.setObjectName("label_show_if")
        self.gridLayout_2.addWidget(self.label_show_if, 1, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_5)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.frame_9 = QtGui.QFrame(self.widget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_9)
        self.gridLayout_3.setMargin(4)
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtGui.QLabel(self.frame_9)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.spin_zoom = QtGui.QSpinBox(self.frame_9)
        self.spin_zoom.setMinimum(10)
        self.spin_zoom.setMaximum(500)
        self.spin_zoom.setProperty("value", 100)
        self.spin_zoom.setObjectName("spin_zoom")
        self.gridLayout_3.addWidget(self.spin_zoom, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame_9)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.spin_grid = QtGui.QSpinBox(self.frame_9)
        self.spin_grid.setMinimum(1)
        self.spin_grid.setProperty("value", 32)
        self.spin_grid.setObjectName("spin_grid")
        self.gridLayout_3.addWidget(self.spin_grid, 1, 1, 1, 1)
        self.checkbox_show_grid = QtGui.QCheckBox(self.frame_9)
        self.checkbox_show_grid.setChecked(True)
        self.checkbox_show_grid.setObjectName("checkbox_show_grid")
        self.gridLayout_3.addWidget(self.checkbox_show_grid, 2, 0, 1, 1)
        self.label_mouse_pos = QtGui.QLabel(self.frame_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mouse_pos.sizePolicy().hasHeightForWidth())
        self.label_mouse_pos.setSizePolicy(sizePolicy)
        self.label_mouse_pos.setMinimumSize(QtCore.QSize(100, 0))
        self.label_mouse_pos.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_mouse_pos.setObjectName("label_mouse_pos")
        self.gridLayout_3.addWidget(self.label_mouse_pos, 2, 1, 1, 1)
        self.widget_6 = QtGui.QWidget(self.frame_9)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_3.addWidget(self.widget_6, 3, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_9)
        self.verticalLayout_3.addWidget(self.widget_7)
        self.frame_notification = QtGui.QFrame(self.widget_3)
        self.frame_notification.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_notification.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_notification.setObjectName("frame_notification")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_notification)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setMargin(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtGui.QLabel(self.frame_notification)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/about_large.png"))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.label_notification = QtGui.QLabel(self.frame_notification)
        self.label_notification.setObjectName("label_notification")
        self.horizontalLayout_3.addWidget(self.label_notification)
        self.button_edit_script = QtGui.QPushButton(self.frame_notification)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_edit_script.sizePolicy().hasHeightForWidth())
        self.button_edit_script.setSizePolicy(sizePolicy)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/script.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_edit_script.setIcon(icon10)
        self.button_edit_script.setObjectName("button_edit_script")
        self.horizontalLayout_3.addWidget(self.button_edit_script)
        self.verticalLayout_3.addWidget(self.frame_notification)
        self.scrollArea = QtGui.QScrollArea(self.widget_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 849, 244))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.view = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view.sizePolicy().hasHeightForWidth())
        self.view.setSizePolicy(sizePolicy)
        self.view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.setObjectName("view")
        self.verticalLayout_5.addWidget(self.view)
        self.widget_items = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget_items.setObjectName("widget_items")
        self.verticalLayout_5.addWidget(self.widget_items)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.button_line.setToolTip(QtGui.QApplication.translate("Form", "Line tool", None, QtGui.QApplication.UnicodeUTF8))
        self.button_arrow.setToolTip(QtGui.QApplication.translate("Form", "Arrow tool", None, QtGui.QApplication.UnicodeUTF8))
        self.button_textline.setToolTip(QtGui.QApplication.translate("Form", "Text tool", None, QtGui.QApplication.UnicodeUTF8))
        self.button_image.setToolTip(QtGui.QApplication.translate("Form", "Image tool", None, QtGui.QApplication.UnicodeUTF8))
        self.button_gabor.setToolTip(QtGui.QApplication.translate("Form", "Gabor patch tool", None, QtGui.QApplication.UnicodeUTF8))
        self.button_rect.setToolTip(QtGui.QApplication.translate("Form", "Rectangle tool", None, QtGui.QApplication.UnicodeUTF8))
        self.button_ellipse.setToolTip(QtGui.QApplication.translate("Form", "Ellipse tool", None, QtGui.QApplication.UnicodeUTF8))
        self.button_circle.setToolTip(QtGui.QApplication.translate("Form", "Circle tool", None, QtGui.QApplication.UnicodeUTF8))
        self.button_fixdot.setToolTip(QtGui.QApplication.translate("Form", "Fixation dot tool", None, QtGui.QApplication.UnicodeUTF8))
        self.button_noise_patch.setToolTip(QtGui.QApplication.translate("Form", "Noise patch tool", None, QtGui.QApplication.UnicodeUTF8))
        self.label_color.setText(QtGui.QApplication.translate("Form", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_color.setToolTip(QtGui.QApplication.translate("Form", "Pen color", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_color.setText(QtGui.QApplication.translate("Form", "white", None, QtGui.QApplication.UnicodeUTF8))
        self.label_penwidth.setText(QtGui.QApplication.translate("Form", "Pen width", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_penwidth.setToolTip(QtGui.QApplication.translate("Form", "Pen width", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_penwidth.setSuffix(QtGui.QApplication.translate("Form", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.label_arrow_size.setText(QtGui.QApplication.translate("Form", "Arrowhead size", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_arrow_size.setToolTip(QtGui.QApplication.translate("Form", "Size of the arrowhead", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_arrow_size.setSuffix(QtGui.QApplication.translate("Form", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.label_scale.setText(QtGui.QApplication.translate("Form", "Image scale", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_scale.setToolTip(QtGui.QApplication.translate("Form", "Image scaling in %", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_scale.setSuffix(QtGui.QApplication.translate("Form", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.label_font_family.setText(QtGui.QApplication.translate("Form", "Font family", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_font_family.setToolTip(QtGui.QApplication.translate("Form", "Font family", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_font_family.setItemText(0, QtGui.QApplication.translate("Form", "mono", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_font_family.setItemText(1, QtGui.QApplication.translate("Form", "sans", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_font_family.setItemText(2, QtGui.QApplication.translate("Form", "serif", None, QtGui.QApplication.UnicodeUTF8))
        self.label_font_size.setText(QtGui.QApplication.translate("Form", "Font size", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_font_size.setToolTip(QtGui.QApplication.translate("Form", "Font size", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_font_size.setSuffix(QtGui.QApplication.translate("Form", "pt", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_fill.setToolTip(QtGui.QApplication.translate("Form", "Check to draw filled objects", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_fill.setText(QtGui.QApplication.translate("Form", "Fill object", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_center.setToolTip(QtGui.QApplication.translate("Form", "Center the object", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_center.setText(QtGui.QApplication.translate("Form", "Center object", None, QtGui.QApplication.UnicodeUTF8))
        self.label_options.setText(QtGui.QApplication.translate("Form", "Click on the sketchpad for options", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_show_if.setText(QtGui.QApplication.translate("Form", "always", None, QtGui.QApplication.UnicodeUTF8))
        self.label_show_if.setText(QtGui.QApplication.translate("Form", "Show if", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_zoom.setToolTip(QtGui.QApplication.translate("Form", "Zoom level in %", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_zoom.setSuffix(QtGui.QApplication.translate("Form", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_grid.setToolTip(QtGui.QApplication.translate("Form", "Grid size", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_grid.setSuffix(QtGui.QApplication.translate("Form", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_show_grid.setToolTip(QtGui.QApplication.translate("Form", "Check to display the grid and enable snap-to-grid", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_show_grid.setText(QtGui.QApplication.translate("Form", "Show grid", None, QtGui.QApplication.UnicodeUTF8))
        self.label_mouse_pos.setText(QtGui.QApplication.translate("Form", "(0, 0)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_notification.setText(QtGui.QApplication.translate("Form", "[nr] objects are not shown, because their definition contains variables.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_edit_script.setToolTip(QtGui.QApplication.translate("Form", "Edit the script to see objects defined using variables", None, QtGui.QApplication.UnicodeUTF8))
        self.button_edit_script.setText(QtGui.QApplication.translate("Form", "Edit script", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
