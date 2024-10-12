import sys
import math
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

# Класс калькулятора, наследующий от QWidget
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # Инициализация пользовательского интерфейса
    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 600, 600)  # Увеличиваем размер окна

        # Память для хранения значений
        self.memory = [0, 0, 0]

        # Основной вертикальный макет
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Поле для отображения ввода и результата
        self.display = QLineEdit()
        self.display.setFixedHeight(50)  # Увеличиваем высоту поля ввода
        self.layout.addWidget(self.display)

        # Создание кнопок
        self.createButtons()

    # Создание кнопок калькулятора
    def createButtons(self):
        buttonsLayout = QGridLayout()

        # Определение кнопок и их расположения
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3),
            ('sin', 4, 0), ('cos', 4, 1), ('tan', 4, 2), ('sqrt', 4, 3),
            ('log', 5, 0), ('ln', 5, 1), ('exp', 5, 2), ('^', 5, 3),
            ('M1', 6, 0), ('M2', 6, 1), ('M3', 6, 2), ('MC', 6, 3),
            ('abs', 7, 0), ('mean', 7, 1), ('reset', 7, 3)
        ]

        # Создание кнопок и добавление их в макет
        for btnText, x, y in buttons:
            button = QPushButton(btnText)
            button.setFixedSize(100, 50)  # Увеличиваем размер кнопок
            button.clicked.connect(self.onButtonClick)
            buttonsLayout.addWidget(button, x, y)

        self.layout.addLayout(buttonsLayout)

    # Обработка нажатий кнопок
    def onButtonClick(self):
        sender = self.sender().text()

        try:
            if sender == '=':
                # Вычисление выражения
                result = eval(self.display.text())
                self.display.setText(str(result))
            elif sender == 'sin':
                self.display.setText(str(math.sin(float(self.display.text()))))
            elif sender == 'cos':
                self.display.setText(str(math.cos(float(self.display.text()))))
            elif sender == 'tan':
                self.display.setText(str(math.tan(float(self.display.text()))))
            elif sender == 'sqrt':
                self.display.setText(str(math.sqrt(float(self.display.text()))))
            elif sender == 'log':
                self.display.setText(str(math.log10(float(self.display.text()))))
            elif sender == 'ln':
                self.display.setText(str(math.log(float(self.display.text()))))
            elif sender == 'exp':
                self.display.setText(str(math.exp(float(self.display.text()))))
            elif sender == '^':
                base, exp = self.display.text().split('^')
                self.display.setText(str(math.pow(float(base), float(exp))))
            elif sender == 'M1':
                # Сохранение значения в память M1
                self.memory[0] = float(self.display.text())
            elif sender == 'M2':
                # Сохранение значения в память M2
                self.memory[1] = float(self.display.text())
            elif sender == 'M3':
                # Сохранение значения в память M3
                self.memory[2] = float(self.display.text())
            elif sender == 'MC':
                # Очистка памяти
                self.memory = [0, 0, 0]
            elif sender == 'abs':
                # Вычисление модуля числа
                self.display.setText(str(abs(complex(self.display.text()))))
            elif sender == 'mean':
                # Вычисление среднего значения
                self.display.setText(str(np.mean(eval(self.display.text()))))
            elif sender == 'reset':
                # Сброс дисплея
                self.display.clear()
            else:
                # Добавление текста кнопки к дисплею
                self.display.setText(self.display.text() + sender)
        except Exception as e:
            self.display.setText('Error')


# Основная часть программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())