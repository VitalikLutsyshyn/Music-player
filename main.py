
import random
from PySide6.QtCore import Qt,QUrl
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QVBoxLayout, QWidget,QFileDialog
from PySide6.QtMultimedia import *
from ui_window import Ui_MainWindow
from qt_material import apply_stylesheet
from datetime import* 


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
        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.ui.timeline_slider.valueChanged.connect(self.player.setPosition)
        self.ui.addFolder.clicked.connect(self.choose_files)
        self.ui.songlist.currentRowChanged.connect(self.open_song)
        self.ui.play_btn.clicked.connect(self.play_song)
        

    def choose_files(self):
        try:
                self.files = QFileDialog.getOpenFileNames(self,"Обреіть пісні",filter= "All files(*.mp3 *.wav)")
        except:
             print("спробуй ще раз")
        self.ui.songlist.addItems(self.files[0])

    def open_song(self):
        if self.ui.songlist.currentRow() >= 0:#повертає номер рядка
            self.current_song = self.ui.songlist.currentItem().text()#вибір поточної пісні
            self.player.stop()
            self.player.setSource(QUrl.fromLocalFile(self.current_song))
            self.audioOutput.setVolume(50)
            self.player.play()

    def play_song(self):
        if self.player.isPlaying():
            self.player.pause()
        else:
             self.player.play()
    def update_duration(self,duration):
        self.ui.timeline_slider.setMaximum(duration)#загальна тривалість пісні
        self.ui.total_time.setText(self.get_time(duration))

    def get_time(self,time_in_ms):
        seconds= time_in_ms/1000
        minutes,seconds = divmod(seconds,60)

        return  f"{int(minutes)}:{int(seconds)}"

    def update_position(self,position):
         if position > 0:
              self.ui.current_time.setText(self.get_time(position))
              self.ui.timeline_slider.blockSignals(True)
              self.ui.timeline_slider.setValue(position)
              self.ui.timeline_slider.blockSignals(False)

         
app = QApplication([])#створення
window = MusicPlayer()#створення вікна
apply_stylesheet(app, theme='dark_blue.xml')
window.show()
app.exec()#запуск