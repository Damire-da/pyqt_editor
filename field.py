import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QTextEdit, QMenu,QProgressBar
from PySide6.QtGui import QIcon

class Window(QMainWindow):

	def __init__(self):
		super().__init__()
	
		self.initUI()




	def initUI(self):

		textEdit = QTextEdit()
		self.setCentralWidget(textEdit)#places the text 
									   #field over the entire free space
		self.statusBar()

		menubar = self.menuBar()
		fileMenu = QMenu("&Menu",self)
		menubar.addMenu(fileMenu)
		
		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Editor+')
		self.show()

	def action(self):
		self.save = QProgressBar("&Save",self)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    with open("main.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    ex = Window()
    sys.exit(app.exec_())