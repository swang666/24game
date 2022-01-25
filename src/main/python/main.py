from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox, QPushButton, QLineEdit, QGridLayout
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore, QtGui
import random
import algorithm
import sys

class Game():
    def __init__(self):
        self.solver = algorithm.Solution()
        self.app = self.init_app()
        self.window = self.init_window()
        self.num_fields = self.create_num_boxes()
        self.gen_button = self.create_gen_button()
        self.answer_field = self.create_answer_box()
        self.eval_button = self.create_eval_button()
        self.sol_button = self.create_sol_button()
        self.layout = self.create_layout(self.num_fields, self.gen_button, self.answer_field, self.eval_button, self.sol_button)
        self.window.setLayout(self.layout)

    def init_app(self):
        return QApplication([])

    def init_window(self):
        window = QWidget()
        window.resize(400, 400)
        window.setWindowTitle('24 game')
        window.setWindowIcon(QtGui.QIcon("title.jpg"))
        return window

    def create_layout(self, num_fields, gen_button, answer_field, eval_button, sol_button):
        layout = QGridLayout()
        for i in range(4):
            layout.addWidget(num_fields[i],0, i)
        layout.addWidget(gen_button, 2,1,1,2)
        layout.addWidget(answer_field, 3,0,1,4)
        layout.addWidget(eval_button, 4,0,1,2)
        layout.addWidget(sol_button, 4,2,1,2)
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

    def create_eval_button(self):
        button = QPushButton('Submit your answer')
        button.clicked.connect(self.on_eval_clicked)
        return button
    
    def on_eval_clicked(self):
        alert = QMessageBox()
        try:
            val = eval(self.answer_field.text())
            if 23.999 <= val <= 24.001:
                message = "Congratulations, you are correct!"
            else:
                message = "Not quite right, try again"
        except:
            message = "Invalid formula, checking typing"
        alert.setText(message)
        alert.setWindowTitle('24 game')
        alert.setWindowIcon(QtGui.QIcon("title.jpg"))
        alert.exec()

    def create_answer_box(self):
        answer_field = QLineEdit()
        answer_field.setMinimumHeight(50)
        font = answer_field.font()   
        font.setPointSize(25)              
        answer_field.setFont(font)
        answer_field.setAlignment(QtCore.Qt.AlignCenter) 
        return answer_field

    def create_sol_button(self):
        button = QPushButton('Look up the solution')
        button.clicked.connect(self.on_sol_clicked)
        return button
    
    def on_sol_clicked(self):
        try:
            cards = [int(x.text()) for x in self.num_fields]
            out = self.solver.judgePoint24(cards)
        except:
            out = "Something wrong happened"
        self.answer_field.setText(out)

if __name__ == "__main__":
    appctxt = ApplicationContext() 
    game = Game()
    game.window.show()
    exit_code = appctxt.app.exec()      # 2. Invoke appctxt.app.exec()
    sys.exit(exit_code)