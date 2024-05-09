# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(733, 827)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background:rgb(77, 74, 73);\n"
"color:white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabs = QTabWidget(self.frame_2)
        self.tabs.setObjectName(u"tabs")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.now_playing = QWidget()
        self.now_playing.setObjectName(u"now_playing")
        self.verticalLayout_4 = QVBoxLayout(self.now_playing)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.song_img = QLabel(self.now_playing)
        self.song_img.setObjectName(u"song_img")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.song_img.sizePolicy().hasHeightForWidth())
        self.song_img.setSizePolicy(sizePolicy1)
        self.song_img.setMaximumSize(QSize(700, 700))
        self.song_img.setPixmap(QPixmap(u"imagion/music.png"))
        self.song_img.setScaledContents(True)

        self.verticalLayout.addWidget(self.song_img)

        self.song_name = QLabel(self.now_playing)
        self.song_name.setObjectName(u"song_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.song_name.sizePolicy().hasHeightForWidth())
        self.song_name.setSizePolicy(sizePolicy2)
        self.song_name.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.song_name)

        self.artist = QLabel(self.now_playing)
        self.artist.setObjectName(u"artist")
        sizePolicy2.setHeightForWidth(self.artist.sizePolicy().hasHeightForWidth())
        self.artist.setSizePolicy(sizePolicy2)
        self.artist.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setBold(False)
        self.artist.setFont(font1)

        self.verticalLayout.addWidget(self.artist)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.tabs.addTab(self.now_playing, "")
        self.all_song = QWidget()
        self.all_song.setObjectName(u"all_song")
        self.tabs.addTab(self.all_song, "")

        self.verticalLayout_2.addWidget(self.tabs)

        self.timeline = QHBoxLayout()
        self.timeline.setObjectName(u"timeline")
        self.total_time = QLabel(self.frame_2)
        self.total_time.setObjectName(u"total_time")
        sizePolicy2.setHeightForWidth(self.total_time.sizePolicy().hasHeightForWidth())
        self.total_time.setSizePolicy(sizePolicy2)
        self.total_time.setMaximumSize(QSize(16777215, 50))

        self.timeline.addWidget(self.total_time)

        self.timeline_slider = QSlider(self.frame_2)
        self.timeline_slider.setObjectName(u"timeline_slider")
        self.timeline_slider.setOrientation(Qt.Horizontal)

        self.timeline.addWidget(self.timeline_slider)

        self.current_time = QLabel(self.frame_2)
        self.current_time.setObjectName(u"current_time")
        sizePolicy2.setHeightForWidth(self.current_time.sizePolicy().hasHeightForWidth())
        self.current_time.setSizePolicy(sizePolicy2)
        self.current_time.setMaximumSize(QSize(16777215, 50))

        self.timeline.addWidget(self.current_time)


        self.verticalLayout_2.addLayout(self.timeline)

        self.control_btn = QHBoxLayout()
        self.control_btn.setObjectName(u"control_btn")
        self.control_btn.setSizeConstraint(QLayout.SetMinimumSize)
        self.prev_btn = QPushButton(self.frame_2)
        self.prev_btn.setObjectName(u"prev_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.prev_btn.sizePolicy().hasHeightForWidth())
        self.prev_btn.setSizePolicy(sizePolicy3)
        self.prev_btn.setMaximumSize(QSize(50, 50))
        self.prev_btn.setStyleSheet(u"background:rgb(97, 89, 89);\n"
"border:3px solidrgb(255, 255, 255);\n"
"color:white;\n"
"border-radius:10px;")
        icon = QIcon()
        icon.addFile(u"imagion/player-skip-back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_btn.setIcon(icon)

        self.control_btn.addWidget(self.prev_btn)

        self.play_btn = QPushButton(self.frame_2)
        self.play_btn.setObjectName(u"play_btn")
        sizePolicy3.setHeightForWidth(self.play_btn.sizePolicy().hasHeightForWidth())
        self.play_btn.setSizePolicy(sizePolicy3)
        self.play_btn.setMaximumSize(QSize(200, 50))
        self.play_btn.setStyleSheet(u"background:rgb(97, 89, 89);\n"
"border:3px solidrgb(255, 255, 255);\n"
"color:white;\n"
"border-radius:5px;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"imagion/player-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_btn.setIcon(icon1)
        self.play_btn.setIconSize(QSize(30, 30))

        self.control_btn.addWidget(self.play_btn)

        self.next_btn = QPushButton(self.frame_2)
        self.next_btn.setObjectName(u"next_btn")
        sizePolicy3.setHeightForWidth(self.next_btn.sizePolicy().hasHeightForWidth())
        self.next_btn.setSizePolicy(sizePolicy3)
        self.next_btn.setMaximumSize(QSize(50, 50))
        self.next_btn.setStyleSheet(u"background:rgb(97, 89, 89);\n"
"border:3px solidrgb(255, 255, 255);\n"
"color:white;\n"
"border-radius:10px;")
        icon2 = QIcon()
        icon2.addFile(u"imagion/player-skip-forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_btn.setIcon(icon2)

        self.control_btn.addWidget(self.next_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.control_btn.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.control_btn)


        self.verticalLayout_3.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.song_img.setText("")
        self.song_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430 \u043f\u0456\u0441\u043d\u0456", None))
        self.artist.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u043a\u043e\u043d\u0430\u0432\u0435\u0446\u044c:", None))
        self.tabs.setTabText(self.tabs.indexOf(self.now_playing), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0430\u0437 \u0433\u0440\u0430\u0454", None))
        self.tabs.setTabText(self.tabs.indexOf(self.all_song), QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0456 \u043f\u0456\u0441\u043d\u0456", None))
        self.total_time.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.current_time.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.prev_btn.setText("")
        self.play_btn.setText("")
        self.next_btn.setText("")
    # retranslateUi

