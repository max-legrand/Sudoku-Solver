import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel
from text_solver import solve, valid, print_board
from board import Grid, Cube, make_board
import random
from mainui import UiForm
import data


class StartGame(object):
    """
    Class for difficulty selection
    """
    def __init__(self):
        self.difficulty = None

    # noinspection PyAttributeOutsideInit,PyArgumentList
    def setupui(self, form):
        # super().__init__()
        self.Dialog = None
        self.ui = None
        self.form = form
        form.setObjectName("Form")
        form.resize(400, 300)
        self.easy = QtWidgets.QPushButton(form)
        self.easy.setGeometry(QtCore.QRect(20, 110, 113, 32))
        self.easy.setObjectName("easy")
        self.easy.setFocusPolicy(QtCore.Qt.NoFocus)
        self.medium = QtWidgets.QPushButton(form)
        self.medium.setGeometry(QtCore.QRect(140, 110, 113, 32))
        self.medium.setObjectName("medium")
        self.medium.setFocusPolicy(QtCore.Qt.NoFocus)
        self.hard = QtWidgets.QPushButton(form)
        self.hard.setGeometry(QtCore.QRect(260, 110, 113, 32))
        self.hard.setObjectName("hard")
        self.hard.setFocusPolicy(QtCore.Qt.NoFocus)
        self.easy.clicked.connect(self.seteasy)
        self.medium.clicked.connect(self.setmed)
        self.hard.clicked.connect(self.sethard)
        self.retranslateui(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def seteasy(self):
        """
        Sets difficulty on easy button click
        """
        print(self)
        self.difficulty = "easy"
        print("EASY")
        self.setup()

    def setmed(self):
        """
        Sets difficulty on medium button click
        """
        self.difficulty = "medium"
        print("MED")
        self.setup()

    def sethard(self):
        """
        Sets difficulty on hard button click
        """
        self.difficulty = "hard"
        print("HARD")
        self.setup()

    # noinspection PyAttributeOutsideInit,PyArgumentList
    def setup(self):
        """
        Setup and start game window
        """
        print("Starting setup")

        given = 0
        if self.difficulty == "easy":
            given = random.randint(36, 40)
        if self.difficulty == "medium":
            given = random.randint(30, 34)
        if self.difficulty == "hard":
            given = random.randint(19, 27)
        print(given)
        board_array = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        print("Generating board")
        print_board(board_array)

        board_array = make_board()
        print_board(board_array)
        for counter in range(81-given):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while board_array[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            board_array[row][col] = 0
        print(given)
        print("Board finished")
        data.gridobj = Grid(board_array, 9, 9)
        self.Dialog = QtWidgets.QDialog()
        self.ui = UiForm()
        self.ui.setup_ui(self.Dialog)

        labelslist = []
        rowcounter = 0
        itemcounter = 1
        data.labels = [[], [], [], [], [], [], [], [], []]

        for child in self.Dialog.findChildren(QLabel):
            if child.objectName() != "strikes":
                labelslist.append(child)
        labelslist.sort(key=lambda x: int(x.objectName()))

        for item in labelslist:
            data.labels[rowcounter].append(item)
            if itemcounter % 9 == 0:
                rowcounter += 1
                itemcounter = 0
            itemcounter += 1

        for rowcounter in range(0, 9):
            for colcounter in range(0, 9):
                if board_array[rowcounter][colcounter] != 0:
                    data.labels[rowcounter][colcounter].setText(str(board_array[rowcounter][colcounter]))
                    data.labels[rowcounter][colcounter].setStyleSheet("color: rgb(40, 255, 6); border: "
                                                                 "2px solid white !important")

        self.Dialog.show()
        # self.form.close()

    # noinspection PyArgumentList
    def retranslateui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Select Difficulty"))
        self.easy.setText(_translate("Form", "Easy"))
        self.medium.setText(_translate("Form", "Medium"))
        self.hard.setText(_translate("Form", "Hard"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # noinspection PyArgumentList
    dialog = QtWidgets.QDialog()
    ui = StartGame()
    ui.setupui(dialog)
    dialog.show()
    sys.exit(app.exec_())
