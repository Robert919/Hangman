from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, random, time 

class Window(QMainWindow):
    def __init__(self):#constructor
        super(Window,self).__init__()
        self.setStyleSheet("background-color: #0ABAA9;")
        self.setGeometry(600,350,600,300)
        self.setWindowTitle("Hangman")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setMaximumSize(600,300)
        self.setMinimumSize(600,300)
        self.initUI()
        self.initializer()
    def indexer(self,letter):
        for i in range(0,len(self.word)):
            if self.word[i]==letter and self.your_guess[i]=="_":
                return i 
                
    def initializer(self):
        file=open("words.txt","r")
        l=file.readlines()
        self.word=l[random.randint(0,len(l)-1)]
        self.word=self.word[:len(self.word)-1]
        self.tries=random.randint(len(self.word)+2,len(self.word)+6)
        self.your_guess=["_"]*len(self.word)
        self.your_guess[len(self.word)//2+1]=self.word[len(self.word)//2+1]
        self.your_guess[1]=self.word[1]
        self.count=0
        self.WordText.setText("".join(self.your_guess))
        self.AttemptsLabel.setText("Attempts:{}/{}".format(self.count,self.tries))
        self.InsertButton.setVisible(True)
        self.Letter.setVisible(True)
    def guess(self):
        letter=self.Letter.toPlainText()
        if self.count<self.tries:
            if len(letter)==0 or len(letter)>1:
                self.Warning=QtWidgets.QMessageBox(self) 
                self.Warning.setGeometry(280,100,150,80)
                self.Warning.about(self,"Warning","Introduce a single letter")
                
                self.Letter.clear()
            if letter in self.word:
                  
                if self.indexer(letter)!=None:
                    self.your_guess[self.indexer(letter)]=letter
                    self.WordText.setText("".join(self.your_guess))
                    self.AttemptsLabel.setText("Attempts:{}/{}".format(self.count,self.tries))
                else:
                    self.count+=1
                    self.AttemptsLabel.setText("Attempts:{}/{}".format(self.count,self.tries))
            else:
                self.count+=1
                self.AttemptsLabel.setText("Attempts:{}/{}".format(self.count,self.tries))
            if "".join(self.your_guess)==self.word:
                
                self.WordText.setText("You've guessed the word, it was {}".format(self.word))
                self.InsertButton.setVisible(False)
                self.Letter.setVisible(False)
        if self.count==self.tries:
            self.WordText.setText("You're done, the word was {}".format(self.word))
            self.InsertButton.setVisible(False)
            self.Letter.setVisible(False)
        self.Letter.clear()
    def initUI(self):#uiSetup
        self.AttemptsLabel=QtWidgets.QLabel(self)
        self.AttemptsLabel.setText("Attempts: / ")
        self.AttemptsLabel.setGeometry(230,36,140,40)  
        self.AttemptsLabel.setFont(QFont('Arial',12))
        self.AttemptsLabel.setStyleSheet("border: 1px solid black;")
        #######
        self.WordLabel=QtWidgets.QLabel(self)
        self.WordLabel.setText("Word")
        self.WordLabel.setGeometry(45,90,66,40)
        self.WordLabel.setFont(QFont('Arial',12))
        self.WordLabel.setStyleSheet("border: 1px solid black;")
        #######
        self.WordText=QtWidgets.QLabel(self)
        self.WordText.setText("________________")
        self.WordText.setGeometry(130,90,440,40)
        self.WordText.setFont(QFont('Arial',12))
        self.WordText.setStyleSheet("border: 1px solid black;")
        #######
        self.LetterLabel=QtWidgets.QLabel(self)
        self.LetterLabel.setText("Letter")
        self.LetterLabel.setGeometry(45,140,66,40)
        self.LetterLabel.setFont(QFont('Arial',12))
        self.LetterLabel.setStyleSheet("border: 1px solid black;")
        #######
        self.Letter=QPlainTextEdit(self)
        self.Letter.setGeometry(130,140,50,40)
        self.Letter.setFont(QFont('Arial',12))
        #######
        self.InsertButton=QtWidgets.QPushButton(self)
        self.InsertButton.setGeometry(192,140,80,40)
        self.InsertButton.setStyleSheet('QPushButton {background-color: #0ABA66; color: black; border: 1px solid black;}')
        self.InsertButton.setText("Insert letter")
        self.InsertButton.clicked.connect(self.guess)
        #######
        self.TryButton=QtWidgets.QPushButton(self)
        self.TryButton.setGeometry(285,140,80,40)
        self.TryButton.setStyleSheet('QPushButton {background-color: #0ABA66; color: black; border: 1px solid black;}')
        self.TryButton.setText("Try again")
        self.TryButton.clicked.connect(self.initializer)
        #######
        


def MainWindow():
    app=QApplication(sys.argv)
    mainwindow=Window()
    mainwindow.show()
    sys.exit(app.exec_())

MainWindow()