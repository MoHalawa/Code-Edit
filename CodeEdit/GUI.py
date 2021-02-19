from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import subprocess


class Window(QMainWindow):

	def __init__(self):
		super().__init__()
 
        	# setting title
		self.setWindowTitle("Python")

        	# setting geometry
		self.setGeometry(100, 100, 500, 400)
 
        	# calling method
		self.text = QPlainTextEdit(self)
		self.text.resize(400,200)
		self.text.move(10,10)

		
		self.button = QPushButton("A", self)
		self.button.move(10,230)
		self.button.clicked.connect(self.buttonPress)
		self.show()
		
		
	def buttonPress(self):
		f = open("code.c", "w")
		f.write(self.text.toPlainText())
		f.close()
		result = subprocess.call(["g++","-S","code.c"])
		f = open("code.s","r")
		print(f.read())


		

App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())

