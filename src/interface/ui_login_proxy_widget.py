# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_login_proxy_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_LoginProxyWidget(object):
    def setupUi(self, LoginProxyWidget):
        if not LoginProxyWidget.objectName():
            LoginProxyWidget.setObjectName(u"LoginProxyWidget")
        LoginProxyWidget.resize(605, 508)
        LoginProxyWidget.setMinimumSize(QSize(450, 0))
        self.gridLayout = QGridLayout(LoginProxyWidget)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.dohBox = QCheckBox(LoginProxyWidget)
        self.dohBox.setObjectName(u"dohBox")
        self.dohBox.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_6.addWidget(self.dohBox)

        self.line_3 = QFrame(LoginProxyWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_3)

        self.label_3 = QLabel(LoginProxyWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_6.addWidget(self.label_3)

        self.dohEdit = QLineEdit(LoginProxyWidget)
        self.dohEdit.setObjectName(u"dohEdit")

        self.horizontalLayout_6.addWidget(self.dohEdit)


        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.proxy_1 = QRadioButton(LoginProxyWidget)
        self.buttonGroup_2 = QButtonGroup(LoginProxyWidget)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.proxy_1)
        self.proxy_1.setObjectName(u"proxy_1")
        self.proxy_1.setMinimumSize(QSize(90, 0))

        self.horizontalLayout.addWidget(self.proxy_1)

        self.line = QFrame(LoginProxyWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label = QLabel(LoginProxyWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.httpLine = QLineEdit(LoginProxyWidget)
        self.httpLine.setObjectName(u"httpLine")

        self.horizontalLayout.addWidget(self.httpLine)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.testSpeedButton = QPushButton(LoginProxyWidget)
        self.testSpeedButton.setObjectName(u"testSpeedButton")

        self.horizontalLayout_2.addWidget(self.testSpeedButton)

        self.label_2 = QLabel(LoginProxyWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_4 = QLabel(LoginProxyWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)


        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButton_1 = QRadioButton(LoginProxyWidget)
        self.buttonGroup = QButtonGroup(LoginProxyWidget)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_1)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setChecked(True)

        self.horizontalLayout_5.addWidget(self.radioButton_1)

        self.label1 = QLabel(LoginProxyWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label1)

        self.label2 = QLabel(LoginProxyWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label2)


        self.gridLayout.addLayout(self.horizontalLayout_5, 8, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_3 = QRadioButton(LoginProxyWidget)
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_3.addWidget(self.radioButton_3)

        self.label5 = QLabel(LoginProxyWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label5)

        self.label6 = QLabel(LoginProxyWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label6)


        self.gridLayout.addLayout(self.horizontalLayout_3, 10, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.httpsBox = QCheckBox(LoginProxyWidget)
        self.httpsBox.setObjectName(u"httpsBox")
        self.httpsBox.setChecked(True)

        self.horizontalLayout_9.addWidget(self.httpsBox)


        self.gridLayout.addLayout(self.horizontalLayout_9, 6, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.proxy_3 = QRadioButton(LoginProxyWidget)
        self.buttonGroup_2.addButton(self.proxy_3)
        self.proxy_3.setObjectName(u"proxy_3")

        self.horizontalLayout_12.addWidget(self.proxy_3)


        self.gridLayout.addLayout(self.horizontalLayout_12, 4, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton_2 = QRadioButton(LoginProxyWidget)
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_4.addWidget(self.radioButton_2)

        self.label3 = QLabel(LoginProxyWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label3)

        self.label4 = QLabel(LoginProxyWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label4)


        self.gridLayout.addLayout(self.horizontalLayout_4, 9, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 12, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.radioButton_4 = QRadioButton(LoginProxyWidget)
        self.buttonGroup.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_7.addWidget(self.radioButton_4)

        self.label7 = QLabel(LoginProxyWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label7)

        self.label8 = QLabel(LoginProxyWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label8)


        self.gridLayout.addLayout(self.horizontalLayout_7, 11, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.proxy_2 = QRadioButton(LoginProxyWidget)
        self.buttonGroup_2.addButton(self.proxy_2)
        self.proxy_2.setObjectName(u"proxy_2")
        self.proxy_2.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_10.addWidget(self.proxy_2)

        self.line_2 = QFrame(LoginProxyWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_2)

        self.label_5 = QLabel(LoginProxyWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_10.addWidget(self.label_5)

        self.sockEdit = QLineEdit(LoginProxyWidget)
        self.sockEdit.setObjectName(u"sockEdit")

        self.horizontalLayout_10.addWidget(self.sockEdit)


        self.gridLayout.addLayout(self.horizontalLayout_10, 3, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.proxy_0 = QRadioButton(LoginProxyWidget)
        self.buttonGroup_2.addButton(self.proxy_0)
        self.proxy_0.setObjectName(u"proxy_0")

        self.horizontalLayout_11.addWidget(self.proxy_0)


        self.gridLayout.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)


        self.retranslateUi(LoginProxyWidget)

        QMetaObject.connectSlotsByName(LoginProxyWidget)
    # setupUi

    def retranslateUi(self, LoginProxyWidget):
        LoginProxyWidget.setWindowTitle(QCoreApplication.translate("LoginProxyWidget", u"\u4ee3\u7406\u8bbe\u7f6e", None))
        self.dohBox.setText(QCoreApplication.translate("LoginProxyWidget", u"\u542f\u7528Doh", None))
        self.label_3.setText(QCoreApplication.translate("LoginProxyWidget", u"\u5730\u5740", None))
        self.proxy_1.setText(QCoreApplication.translate("LoginProxyWidget", u"HTTP\u4ee3\u7406", None))
        self.label.setText(QCoreApplication.translate("LoginProxyWidget", u"\u4ee3\u7406\u5730\u5740", None))
#if QT_CONFIG(tooltip)
        self.httpLine.setToolTip(QCoreApplication.translate("LoginProxyWidget", u"http://127.0.0.1:10809", None))
#endif // QT_CONFIG(tooltip)
        self.httpLine.setPlaceholderText("")
        self.testSpeedButton.setText(QCoreApplication.translate("LoginProxyWidget", u"\u6d4b\u901f", None))
        self.label_2.setText(QCoreApplication.translate("LoginProxyWidget", u"\u76f4\u8fde", None))
        self.label_4.setText(QCoreApplication.translate("LoginProxyWidget", u"\u4ee3\u7406", None))
        self.radioButton_1.setText(QCoreApplication.translate("LoginProxyWidget", u"\u5206\u6d411", None))
        self.label1.setText("")
        self.label2.setText("")
        self.radioButton_3.setText(QCoreApplication.translate("LoginProxyWidget", u"\u5206\u6d413", None))
        self.label5.setText("")
        self.label6.setText("")
        self.httpsBox.setText(QCoreApplication.translate("LoginProxyWidget", u"\u542f\u7528Https\uff08\u5982\u679c\u51fa\u73b0\u8fde\u63a5\u88ab\u91cd\u7f6e\uff0c\u5efa\u8bae\u5173\u95ed\u8bd5\u8bd5\uff09", None))
        self.proxy_3.setText(QCoreApplication.translate("LoginProxyWidget", u"\u4f7f\u7528\u7cfb\u7edf\u4ee3\u7406", None))
        self.radioButton_2.setText(QCoreApplication.translate("LoginProxyWidget", u"\u5206\u6d412", None))
        self.label3.setText("")
        self.label4.setText("")
        self.radioButton_4.setText(QCoreApplication.translate("LoginProxyWidget", u"\u5206\u6d414", None))
        self.label7.setText("")
        self.label8.setText("")
        self.proxy_2.setText(QCoreApplication.translate("LoginProxyWidget", u"Sock5\u4ee3\u7406", None))
        self.label_5.setText(QCoreApplication.translate("LoginProxyWidget", u"\u4ee3\u7406\u5730\u5740", None))
#if QT_CONFIG(tooltip)
        self.sockEdit.setToolTip(QCoreApplication.translate("LoginProxyWidget", u"127.0.0.1:10808", None))
#endif // QT_CONFIG(tooltip)
        self.sockEdit.setPlaceholderText("")
        self.proxy_0.setText(QCoreApplication.translate("LoginProxyWidget", u"\u65e0\u4ee3\u7406", None))
    # retranslateUi

