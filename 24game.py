from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox, QPushButton, QLineEdit, QGridLayout
from PyQt5 import QtCore, QtGui
import random
# app = QApplication([])
# window = QWidget()
# window.setGeometry(0, 0, 400, 400)
# window.setWindowTitle('24 game')
# window.setWindowIcon(QtGui.QIcon("title.jpg"))
# layout = QGridLayout()
# num_fields = []
# for i in range(4):
#     num = QLineEdit()
#     num.setMinimumWidth(100)
#     num.setMinimumHeight(100)
#     font = num.font()   
#     font.setPointSize(40)              
#     num.setFont(font)
#     num.setAlignment(QtCore.Qt.AlignCenter) 
#     num_fields.append(num)
#     layout.addWidget(num, 0, i)

# def on_button_clicked():
#     alert = QMessageBox()
#     alert.setText('You clicked the button!')
#     alert.exec()
# button = QPushButton('Click')
# button.clicked.connect(on_button_clicked)

# layout.addWidget(button,1,0)
# window.setLayout(layout)
# window.show()
# app.exec()

class Game():
    def __init__(self):
        self.app = self.init_app()
        self.window = self.init_window()
        self.num_fields = self.create_num_boxes()
        self.gen_button = self.create_gen_button()
        self.layout = self.create_layout(self.num_fields, self.gen_button)
        self.window.setLayout(self.layout)

    def init_app(self):
        return QApplication([])

    def init_window(self):
        window = QWidget()
        window.setGeometry(0, 0, 400, 400)
        window.setWindowTitle('24 game')
        window.setWindowIcon(QtGui.QIcon("title.jpg"))
        return window

    def create_layout(self, num_fields, gen_button):
        layout = QGridLayout()
        for i in range(4):
            layout.addWidget(num_fields[i],0, i)
        layout.addWidget(gen_button, 1,1)
        return layout
    
    def create_num_boxes(self):
        num_fields = []
        for _ in range(4):
            num = QLineEdit()
            num.setMinimumWidth(100)
            num.setMinimumHeight(100)
            font = num.font()   
            font.setPointSize(40)              
            num.setFont(font)
            num.setAlignment(QtCore.Qt.AlignCenter) 
            num_fields.append(num)
        return num_fields

    def create_gen_button(self):
        button = QPushButton('Generate a problem')
        button.clicked.connect(self.on_gen_clicked)
        return button
    
    def on_gen_clicked(self):
        for i in range(4):
            self.num_fields[i].setText(str(random.randint(1,9)))

        

if __name__ == "__main__":
    game = Game()
    game.window.show()
    game.app.exec()