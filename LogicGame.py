from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import *
from GuiGame import *

class Logic (QMainWindow, Ui_MainWindow):
    list_answers = [
        5, 9, 7, 4, 2, 3,
        2, 1, 8, 5, 7,
        4, 7, 2, 3, 5,
        1, 5, 7, 4, 2,
        6, 1, 8, 5,
        3, 9, 4, 6, 1,
        6, 8, 3, 9, 7,
        4, 9, 1, 6, 8,
        6, 7, 8, 4, 9, 3
    ]

    def __init__(self) -> None:
        '''
        This function just sets up the Gui
        :returns: None
        '''
        super().__init__()
        self.setupUi(self)

    def submit(self) -> None:
        '''
        This function is the single validation function for the user's
        inputted sudoku numbers and displays a win
        :return: None
        '''
        list_inputs = [
            self.spinBox_01.value(), self.spinBox_02.value(), self.spinBox_03.value(),
            self.spinBox_04.value(), self.spinBox_05.value(), self.spinBox_06.value(),
            self.spinBox_07.value(), self.spinBox_08.value(),
            self.spinBox_09.value(), self.spinBox_10.value(), self.spinBox_11.value(),
            self.spinBox_12.value(), self.spinBox_13.value(), self.spinBox_14.value(),
            self.spinBox_15.value(), self.spinBox_16.value(), self.spinBox_17.value(),
            self.spinBox_18.value(), self.spinBox_19.value(), self.spinBox_20.value(),
            self.spinBox_21.value(), self.spinBox_22.value(), self.spinBox_23.value(),
            self.spinBox_24.value(), self.spinBox_25.value(), self.spinBox_26.value(),
            self.spinBox_27.value(), self.spinBox_28.value(), self.spinBox_29.value(),
            self.spinBox_30.value(), self.spinBox_31.value(), self.spinBox_32.value(),
            self.spinBox_33.value(), self.spinBox_34.value(), self.spinBox_35.value(),
            self.spinBox_36.value(), self.spinBox_37.value(), self.spinBox_38.value(),
            self.spinBox_39.value(), self.spinBox_40.value(), self.spinBox_41.value(),
            self.spinBox_42.value(), self.spinBox_43.value(), self.spinBox_44.value(),
            self.spinBox_45.value()
        ]

        answers_correct = 0
        counter = 0
        for answer in list_inputs:
            if answer == Logic.list_answers[counter]:
                answers_correct += 1
                counter += 1
            else:
                counter += 1

        if answers_correct == 46:
            self.label_win.setText("You Win! Congrats!")
        else:
            self.label_win.setText(f"You Lose! Correct answers: {answers_correct}")

    def timer(self) -> None:
        '''
        This function contains the timer itself and all the timer
        qualities and values.  It also starts the timer and calls
        the timer_lose function when time is up.
        :return: None
        '''
        self.timer = QTimer(self)
        self.timer.setInterval(300000)
        self.timer.timeout.connect(self.timer_lose)
        self.timer.start()
        self.pushButton_startTimer.hide()
        self.label_win.setText("Timer started, good luck!")


    def timer_lose(self) -> None:
        '''
        This function hides the submit button when time is up
        and displays a loss message.
        :return: None
        '''
        self.pushButton_submit.hide()
        self.label_win.setText(f"Time's up!  You Lose!")