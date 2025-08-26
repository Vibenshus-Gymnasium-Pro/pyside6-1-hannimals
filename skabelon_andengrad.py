import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QPixmap, QIntValidator, QPalette
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
    QWidget,
    QVBoxLayout,
    QMenu,
    QPushButton,
    QHBoxLayout,
    QBoxLayout,
)


def quad_solver_solutions(a, b, c): 
    d = b**2 - 4*a*c
    if d < 0:
        return "There are no real solutions"
    elif d == 0:
        x = x1 = x2 = -b / (2*a)
        return (x)
    else:
        x1 = (-b + d**0.5) / (2*a) #to find d square root we use **0.5 wich is the same as ^0,5
        x2 = (-b - d**0.5) / (2*a)
        return (x1, x2) #returning a tuple with both solutions

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.start()


    def start(self):

        self.setWindowTitle("Cuadratic Equation Solver")
        
        self.label = QLabel("Cuadratic Equation Solver! :)") #constant label
        font = self.label.font()
        font.setPointSize(12)
        self.label.setFont(font) # Set font size for label

        self.label_1 = QLabel("a :  ") #input labels
        self.label_2 = QLabel("b :  ")
        self.label_3 = QLabel("c :  ")

        self.label_4 = QLabel("Solutions: ")
        font = self.label_4.font()
        font.setPointSize(12)
        self.label_4.setFont(font) # Set font size for label 

        self.input_a = QDoubleSpinBox()
        self.input_a.setRange(-100, 100)
        self.input_b = QDoubleSpinBox()
        self.input_b.setRange(-100, 100) #allowing negative numbers for b
        self.input_c = QDoubleSpinBox()
        self.input_c.setRange(-100, 100) #we could have used sys.maxsize but for simplicity we use 100.
        #spinbox detects changes automatically and accepts only integers :)

        self.input_a.setFixedWidth(70)
        self.input_b.setFixedWidth(70)
        self.input_c.setFixedWidth(70)
        #we set the size so it looks nice :3

        self.calculate_knap = QPushButton("Calculate")
        self.calculate_knap.setStyleSheet("background-color: lightblue; font-size: 16px;")
        self.calculate_knap.setCheckable(True)
        self.calculate_knap.toggled.connect(lambda: self.calculate_knap.setStyleSheet("background-color: lightpink; font-size: 16px;") 
                                            if self.calculate_knap.isChecked() 
                                            else self.calculate_knap.setStyleSheet("background-color: lightblue; font-size: 16px;"))
        #we used lambda because we needed an anonimous function in a short period of time to change the color of the button when pressed
        # we use the if statement to check the button state and the else statement to set the color back and with the lambda function 
        # we can have it all in one function

        self.calculate_knap.clicked.connect(self.calculate) # Connect button click to calculate method
        self.calculate_knap.setFixedWidth(100)
        self.calculate_knap.setFixedHeight(40)
        #set the size of the button  

        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom) # Create a vertical layout

        layout.addWidget(self.label_1, alignment=Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.input_a, alignment=Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignLeft) # Add input field to layout

        layout.addWidget(self.label_2, alignment=Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignVCenter) # Add labels to layout
        layout.addWidget(self.input_b, alignment=Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignVCenter) # Add input field to layout

        layout.addWidget(self.label_3, alignment=Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignLeft) # Add labels to layout
        layout.addWidget(self.input_c, alignment=Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignLeft) # Add input field to layout

        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter) # Add labels to layout
        layout.addWidget(self.calculate_knap) # Add button to layout
        layout.addWidget(self.label_4, alignment=Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.setFixedSize(600, 400)


    def calculate(self): #we define our calculate function 

        a = self.input_a.value()
        b = self.input_b.value()
        c = self.input_c.value()
        if a == 0:
            self.label_4.setText("Error: 'a' cannot be zero.") # if a is 0 we detect it before its procesed in the quad solver function
            return "Error: 'a' cannot be zero."
        
        solutions = quad_solver_solutions(a, b, c) #we call our solver function
         # Update the label with the solutions
        self.label_4.setText(f"Solutions: {solutions}")
        return solutions



my_app = QApplication(sys.argv)

window = Mainwindow()
window.show()

my_app.exec()