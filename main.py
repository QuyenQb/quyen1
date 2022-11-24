import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from maytinh import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        self.uic.Button_0.clicked.connect(lambda: self.pressed_it("0"))
        self.uic.Button_1.clicked.connect(lambda: self.pressed_it("1"))
        self.uic.Button_2.clicked.connect(lambda: self.pressed_it("2"))
        self.uic.Button_3.clicked.connect(lambda: self.pressed_it("3"))
        self.uic.Button_4.clicked.connect(lambda: self.pressed_it("4"))
        self.uic.Button_5.clicked.connect(lambda: self.pressed_it("5"))
        self.uic.Button_6.clicked.connect(lambda: self.pressed_it("6"))
        self.uic.Button_7.clicked.connect(lambda: self.pressed_it("7"))
        self.uic.Button_8.clicked.connect(lambda: self.pressed_it("8"))
        self.uic.Button_9.clicked.connect(lambda: self.pressed_it("9"))
        self.uic.Add_Button.clicked.connect(lambda: self.pressed_it("+"))
        self.uic.Minus_Button.clicked.connect(lambda: self.pressed_it("-"))
        self.uic.Muhai_Button.clicked.connect(lambda: self.pressed_it("^2"))
        self.uic.Percent_Button.clicked.connect(lambda: self.pressed_it("%"))
        self.uic.C_Button.clicked.connect(lambda: self.pressed_it("C"))
        self.uic.Devide_Button.clicked.connect(lambda: self.pressed_it("/"))
        self.uic.Canbachai_Button.clicked.connect(lambda: self.pressed_it())
        self.uic.Multiply_Button.clicked.connect(lambda: self.pressed_it("*"))
        self.uic.CE_Button.clicked.connect(lambda: self.pressed_it("CE"))
        self.uic.Motich_Button.clicked.connect(lambda: self.pressed_it("1/x"))
        self.uic.Plus_Minus_Button.clicked.connect(lambda: self.pressed_Plus_Minus())
        self.uic.Decimal_Button.clicked.connect(lambda: self.pressed_it("."))
        self.uic.Equal_Button.clicked.connect(lambda: self.pressed_Equal())
        self.uic.DEL_Button.clicked.connect(lambda: self.pressed_DEL())


    def action_Muhai(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " **2 ")


    #ham tinh toan don gian
    def pressed_Equal(self):
        screen_1 = self.uic.Screen.text()
        try:
            result = eval(screen_1)
            self.uic.Screen.setText(str(result))
        except:
            self.uic.Screen.setText("에러")

    #chuyen doi am, duong
    def pressed_Plus_Minus(self):
        screen_1 = self.uic.Screen.text()
        if "-" in screen_1:
            self.uic.Screen.setText(screen_1.replace("-", ""))
        else:
            self.uic.Screen.setText(f'-{screen_1}')

    #nut del tung so mot
    def pressed_DEL(self):
        screen_1 = self.uic.Screen.text()
        screen_1 = screen_1[:-1]
        self.uic.Screen.setText(screen_1)

    #del tat ca
    def pressed_it(self, pressed):
        if pressed == "C":
            self.uic.Screen.setText("0")
        elif pressed == "CE":
            self.uic.Screen.setText("0")
        else:
            if self.uic.Screen.text() == "0":
                self.uic.Screen.setText("")
            self.uic.Screen.setText(f'{self.uic.Screen.text()}{pressed}')

    def show(self):
            self.main_win.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
