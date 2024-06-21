
import random
from PySide6.QtCore import Qt,QUrl,Slot,QTime
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QVBoxLayout, QWidget,QFileDialog,
from PySide6.QtMultimedia import *
from ui_window import Ui_MainWindow
from qt_material import apply_stylesheet
from PySide6.QtGui import QPixmap,QIcon
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
        self.current_index = 0
        self.song_names = []
        self.play_icon = QIcon("imagion/player-play.png")
        self.pause_icon = QIcon("imagion/pause.png")

    def connects(self):
        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.ui.timeline_slider.valueChanged.connect(self.player.setPosition)
        self.ui.addFolder.clicked.connect(self.choose_files)
        self.ui.songlist.currentRowChanged.connect(self.open_song)
        self.ui.play_btn.clicked.connect(self.play_song)
        self.ui.prev_btn.clicked.connect(self.prev_song)
        self.ui.next_btn.clicked.connect(self.next_song)
        self.player.metaDataChanged.connect(self.get_metadata)
        

    def choose_files(self):
        try:
            self.files = QFileDialog.getOpenFileNames(self,"Обреіть пісні",filter= "All files(*.mp3 *.wav)")
            self.song_list = self.files[0]
        except:
            print("спробуй ще раз")
        for song in self.song_list:
            name = song.split("/")[-1]
            self.song_names.append(name)
        self.ui.songlist.addItems(self.song_names)

    def load_song(self,index):
            if index >= 0 and index < len(self.song_list):
                self.player.stop()
                self.player.setPosition(0)
                self.update_duration(self.player.duration())
                self.update_position(0)
                self.current_index = index  
                self.ui.songlist.setCurrentRow(self.current_index)

                try:
                    self.player.setSource(QUrl.fromLocalFile(self.song_list[self.current_index]))
                    self.player.play()
                except:
                    print("can't load song")

    def open_song(self):
        if self.ui.songlist.currentRow() >= 0:#повертає номер рядка
            self.current_index = self.ui.songlist.currentRow()
            self.current_song = self.ui.songlist.currentItem().text()#вибір поточної пісні
            self.load_song(self.current_index)
            

    def play_song(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.ui.play_btn.setIcon(self.pause_icon)
        else:
            self.player.play()
            self.ui.play_btn.setIcon(self.play_icon)

    def update_duration(self,duration):
        self.ui.timeline_slider.setMaximum(duration)#загальна тривалість пісні
        self.ui.total_time.setText(self.get_time(duration))

    def get_time(self,time_in_ms):
        seconds= time_in_ms/1000
        minutes,seconds = divmod(seconds,60)
        time = QTime(0,minutes,seconds)

        return  time.toString()[3:]

    def update_position(self,position):
         if position > 0:
              self.ui.current_time.setText(self.get_time(position))
              self.ui.timeline_slider.blockSignals(True)
              self.ui.timeline_slider.setValue(position)
              self.ui.timeline_slider.blockSignals(False)

    @Slot()
    def prev_song(self):
        position = self.player.position()
        if position > 5000:
            self.player.setPosition(0)
            self.update_position(0)
        else:
            if self.current_index > 0:
                self.load_song(self.current_index - 1)
            else:
                self.load_song(len(self.song_list)-1)

    @Slot()
    def next_song(self):
        if self.current_index < len(self.song_list)-1:
            self.load_song(self.current_index + 1)
        else:
            self.load_song(0)

    def get_metadata(self):
        title = self.player.metaData().value(QMediaMetaData.Title) or self.song_names[self.current_index]
        self.ui.song_name.setText(title)

        artist = self.player.metaData().value(QMediaMetaData.Author) or self.player.metaData().value(QMediaMetaData.AlbumArtist) or self.player.metaData().value(QMediaMetaData.ContributingArtist or "")
        if isinstance(artist,list) and len(artist) > 0:
            artist = artist[0]
        self.ui.artist.setText(str(artist))

        album = self.player.metaData().value(QMediaMetaData.AlbumTitle) or ""
        genre = self.player.metaData().value(QMediaMetaData.Genre) 
        self.ui.album_year.setText(f'{album} - {", ".join(genre)}') 
        
         
   


app = QApplication([])#створення
window = MusicPlayer()#створення вікна
apply_stylesheet(app, theme='dark_blue.xml')
window.show()
app.exec()#запуск