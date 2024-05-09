
import random
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QVBoxLayout, QWidget
from ui_window import Ui_MainWindow
from qt_material import apply_stylesheet


class MusicPlayer(QMainWindow):
    def __init__(self):
        super(MusicPlayer,self).__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 300, 150)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QApplication([])#створення
window = MusicPlayer()#створення вікна
apply_stylesheet(app, theme='dark_blue.xml')
window.show()
app.exec()#запуск