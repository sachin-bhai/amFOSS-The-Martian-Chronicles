import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QFileDialog, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window dimensions
        self.setGeometry(250, 250, 250, 250)

        # Set window title
        self.setWindowTitle("MARS_ROVER")

        # Create a label for the date input
        text_label=QLabel('Enter Text:',self)
        text_label.move(50,50)

        self.text_input = QLineEdit(self)
        self.text_input.move(150, 50)
        self.text_input.resize(300, 25)


        date_label = QLabel("Enter Date:", self)
        date_label.move(50, 50)

        # Create a text input field for the date
        self.date_input = QLineEdit(self)
        self.date_input.move(150, 50)
        self.date_input.resize(300, 25)
        
        # Create buttons
        self.button1 = QPushButton("FETCH")
        self.button1.clicked.connect(self.button1.clicked)
        self.button2 = QPushButton("PREV")
        self.button3 = QPushButton("NEXT")
        self.button4 = QPushButton("SEND MAIL")
        self.button5 = QPushButton("RANDOM")
       

        
        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)
        button_layout.addWidget(self.button4)
        button_layout.addWidget(self.button5)

        # Create a graphics view for the image
        self.image_view = QGraphicsView()
        self.image_scene = QGraphicsScene()
        self.image_view.setScene(self.image_scene)

        # Create a label for the image display
        image_label = QLabel(self)
        image_label.setGeometry(50, 150, 150, 150)


        # Set an image from a file as the label's pixmap
        image = QtGui.QPixmap(r'/home/programmer/The-Martian-Chronicles/rover_images/attachments0.jpg')
        image_label.setPixmap(image)

        # Create a vertical layout to hold the calendar, label, text input, buttons, and image view
        layout = QVBoxLayout()
        layout.addWidget(self.text_input)
        layout.addWidget(self.date_input)
        # layout.addWidget(self.date_label)
        # layout.addWidget(self.


    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


