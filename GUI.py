

import sys,requests,json,os,ezgmail
from PIL import Image
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QFileDialog, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QPixmap
import threading


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(250, 250, 250, 250)


        self.setWindowTitle("MARS_ROVER")

  
        text_label=QLabel('Enter Text:',self)
        text_label.move(50,50)

        self.text1_input = QLineEdit("Rover",self)
        self.text1_input.move(150, 50)
        self.text1_input.resize(300, 25)

        self.text2_input = QLineEdit("Camera",self)
        self.text2_input.move(150, 50)
        self.text2_input.resize(300, 25)

        self.text3_input = QLineEdit('Email addresses',self)
        self.text3_input.move(150, 50)
        self.text3_input.resize(300, 25)


        self.date_input = QLineEdit("Date",self)
        self.date_input.move(150, 50)
        self.date_input.resize(300, 25)
        self.date_input = QLineEdit("SOL",self)
        
    
        # self.button1 = QPushButton("DOWNLOAD")
        # self.button1.clicked.connect(self.button1_clicked)
        # self.button2 = QPushButton("FETCH")
        # self.button2.clicked.connect(self.)
        # self.button2.clicked.connect(self.c)
        # self.button3 = QPushButton("PREV")
        # self.button3.clicked.connect(self.button3_clicked)
        # self.button4 = QPushButton("NEXT")
        # self.button4.clicked.connect(self.button4_clicked)
        # self.button5 = QPushButton("SEND MAIL")
       
        
        
        # button_layout = QHBoxLayout()
        # button_layout.addWidget(self.button1)
        # button_layout.addWidget(self.button2)
        # button_layout.addWidget(self.button3)
        # button_layout.addWidget(self.button4)
        # button_layout.addWidget(self.button5)

       
        self.image_view = QGraphicsView()
        self.image_scene = QGraphicsScene()
        self.image_view.setScene(self.image_scene)

        
        global image_label
        image_label = QLabel(self)
        # self.button2.clicked.connect(self.image_scene)

        image_label.setGeometry(50, 150, 150, 150)


        
        image = QtGui.QPixmap(r'/home/programmer/The-Martian-Chronicles/rover_images/loading.jpg')
        image_label.setPixmap(image)



        
        self.button1 = QPushButton("DOWNLOAD")
        self.button1.clicked.connect(self.download_thread)
        self.button2 = QPushButton("FETCH")
        self.button2.clicked.connect(self.change1_image)
        self.button3 = QPushButton("PREV")
        self.button3.clicked.connect(self.change2_image)
        self.button4 = QPushButton("NEXT")
        self.button4.clicked.connect(self.change3_image)
        self.button5 = QPushButton("SEND MAIL")
        self.button5.clicked.connect(self.mail_thread)
       
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)
        button_layout.addWidget(self.button4)
        button_layout.addWidget(self.button5)


        
        layout = QVBoxLayout()
        layout.addWidget(self.text1_input)
        layout.addWidget(self.text2_input)
        layout.addWidget(self.date_input)
        layout.addWidget(self.text3_input)
        layout.addLayout(button_layout)
        layout.addWidget(self.image_view)
        layout.addWidget(image_label)        

        
        central_widget = QWidget()
        central_widget.setLayout(layout)

        
        self.setCentralWidget(central_widget)
    def button1_clicked(self):
        # print('Hello World')
        rover_name=(self.text1_input.text()).lower()
        camera_name=(self.text2_input.text()).lower()
        date_text = self.date_input.text()
        print(date_text)
        os.makedirs('rover_images',exist_ok=True)
        res=requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/'+rover_name+'/photos?sol='+date_text+'&camera='+camera_name+'&api_key=qWngT2sHFzb7K2WW9Kwzor1xs7w10rkDu6LDXfNX')
        res.raise_for_status()
        rover_data=json.loads(res.text)

        images=rover_data['photos']

        sources=[]
        for i in images:
            for j in i:
                if j=='img_src':
                    sources.append(i[j])

        print(sources)
        global n
        n=0
        if len(sources)==0:
            print("bruh")

        for x in sources:
            img=Image.open(requests.get(x,stream=True).raw)
            os.chdir(r'/home/programmer/The-Martian-Chronicles/rover_images')
            img.save(f'attachments{n}.jpg')
            n+=1
        files=os.listdir(r'/home/programmer/The-Martian-Chronicles/rover_images')
        global n_max
        n_max=len(files)


    def change1_image(self):
        
        image = QtGui.QPixmap(r'/home/programmer/The-Martian-Chronicles/rover_images/eminem.jpg')
        image_label.setPixmap(image)
        print('Bruh')
        global counting
        counting=0
        print(counting)
    def change2_image(self,counting):
        counting=0
        def something(self,counting):
                    image = QtGui.QPixmap(r'/home/programmer/The-Martian-Chronicles/rover_images/attachments'+str(counting)+'.jpg')
                    image_label.setPixmap(image)
                    counting-=1
                    print(counting)
        
        something(self,counting)
        counting+=1

        # os.chdir(r'/home/programmer/The-Martian-Chronicles/rover_images')
        # directory=r'/home/programmer/The-Martian-Chronicles/rover_images'


    def change3_image(self,counting):
        counting=1
        def something(self,counting):
                image = QtGui.QPixmap(r'/home/programmer/The-Martian-Chronicles/rover_images/attachments'+str(counting)+'.jpg')
                image_label.setPixmap(image)
                counting+=1
                print(counting)
        
        something(self,counting)
        counting+=1
    def button5_clicked(self):
        attach=os.listdir(r'/home/programmer/The-Martian-Chronicles/rover_images')
        os.chdir(r'/home/programmer/The-Martian-Chronicles/rover_images')
        email=(self.text3_input.text()).lower()
        sending=email.split(',')
        for i in sending:
            ezgmail.send(str(i),"Rover Images","These are the images I retrieved today...",attach)
        print('Done')


    def download_thread(self) :
        thread = threading.Thread(target=self.button1_clicked)
        thread.start()

    def mail_thread(self):
        thread = threading.Thread(target=self.button5_clicked)
        thread.start()

   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



       