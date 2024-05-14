
import random
from PySide6.QtCore import Qt,QUrl
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QVBoxLayout, QWidget,QFileDialog
from PySide6.QtMultimedia import *
from ui_window import Ui_MainWindow
from qt_material import apply_stylesheet



 

class MusicPlayer(QMainWindow):
    def __init__(self):
        super(MusicPlayer,self).__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 300, 150)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #ВІДТВОРЕННЯ МУЗИКИ
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)

        self.connects()
        self.files = None
        self.current_song = None

    def connects(self):
        self.ui.addFolder.clicked.connect(self.choose_files)
        self.ui.songlist.currentRowChanged.connect(self.open_song)

    def choose_files(self):
        try:
                self.files = QFileDialog.getOpenFileNames(self,"Обреіть пісні",filter= "All files(*.mp3 *.wav)")
        except:
             print("спробуй ще раз")
        self.ui.songlist.addItems(self.files[0])

    def open_song(self):
         if self.ui.songlist.currentRow() >= 0:#повертає номер рядка
              self.current_song = self.ui.songlist.currentItem().text()#вибір поточної пісні
              self.player.setSource(QUrl.fromLocalFile(self.current_song))
              self.audioOutput.setVolume(50)
              self.player.play()
              



app = QApplication([])#створення
window = MusicPlayer()#створення вікна
apply_stylesheet(app, theme='dark_blue.xml')
window.show()
app.exec()#запуск