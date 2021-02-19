from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import subprocess
import time


class MainWindow(QMainWindow):

	def __init__(self):
		super(MainWindow, self).__init__()
		self.title = "Image Viewer"
		self.x = 10;
		self.setWindowTitle(self.title)
		self.setGeometry(100, 100, 500, 400)
		label = QLabel(self)
		pixmap = QPixmap('proxy.png')
		label.setPixmap(pixmap)
		self.setCentralWidget(label)
		self.button = QPushButton("A", self)
		self.button.move(10,230)
		self.button.clicked.connect(lambda: self.move(label,self.x))
		
	
	def move(self,label,x):
		time.sleep(1)
		label.move(x,x)
		x+=1
			\
		

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())