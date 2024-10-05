import sys
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QGridLayout

# Класс калькулятора, наследующий от QWidget
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # Инициализация пользовательского интерфейса
    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 400, 400)

        # Память для хранения значений
        self.memory = [0, 0, 0]

        # Основной вертикальный макет
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Поле для отображения ввода и результата
        self.display = QLineEdit()
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
            ('Re', 7, 0), ('Im', 7, 1), ('abs', 7, 2), ('arg', 7, 3),
            ('mean', 8, 0), ('median', 8, 1), ('std', 8, 2), ('var', 8, 3),
            ('det', 9, 0), ('inv', 9, 1), ('T', 9, 2), ('prob', 9, 3),
            ('plot', 10, 0), ('reset', 10, 1)
        ]

        # Создание кнопок и добавление их в макет
        for btnText, x, y in buttons:
            button = QPushButton(btnText)
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
            elif sender == 'Re':
                # Получение действительной части комплексного числа
                self.display.setText(str(cmath.polar(complex(self.display.text()))[0]))
            elif sender == 'Im':
                # Получение мнимой части комплексного числа
                self.display.setText(str(cmath.polar(complex(self.display.text()))[1]))
            elif sender == 'abs':
                # Вычисление модуля комплексного числа
                self.display.setText(str(abs(complex(self.display.text()))))
            elif sender == 'arg':
                # Вычисление аргумента комплексного числа
                self.display.setText(str(cmath.phase(complex(self.display.text()))))
            elif sender == 'mean':
                # Вычисление среднего значения
                self.display.setText(str(np.mean(eval(self.display.text()))))
            elif sender == 'median':
                # Вычисление медианы
                self.display.setText(str(np.median(eval(self.display.text()))))
            elif sender == 'std':
                # Вычисление стандартного отклонения
                self.display.setText(str(np.std(eval(self.display.text()))))
            elif sender == 'var':
                # Вычисление дисперсии
                self.display.setText(str(np.var(eval(self.display.text()))))
            elif sender == 'det':
                # Вычисление определителя матрицы
                self.display.setText(str(np.linalg.det(eval(self.display.text()))))
            elif sender == 'inv':
                # Вычисление обратной матрицы
                self.display.setText(str(np.linalg.inv(eval(self.display.text()))))
            elif sender == 'T':
                # Транспонирование матрицы
                self.display.setText(str(np.transpose(eval(self.display.text()))))
            elif sender == 'plot':
                # Построение графика
                self.plotGraph()
            elif sender == 'reset':
                # Сброс дисплея
                self.display.clear()
            else:
                # Добавление текста кнопки к дисплею
                self.display.setText(self.display.text() + sender)
        except Exception as e:
            self.display.setText('Error')

    # Функция для построения графика
    def plotGraph(self):
        try:
            x = np.linspace(-10, 10, 400)
            y = eval(self.display.text())
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Graph')
            plt.grid(True)
            plt.show()
        except Exception as e:
            self.display.setText('Error')

# Основная часть программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())