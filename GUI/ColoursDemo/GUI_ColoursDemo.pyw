import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_ColoursDemo
#      ^^^^^^^^^^^ Change this!

#CHANGE THE SECOND PARAMETER (Ui_ChangeMe) TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_ColoursDemo.Ui_MainWindow):
#                         ^^^^^^^^^^^   Change this!

    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY

        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
        self.PushButtonDisplay.clicked.connect(self.PushButtonDisplay_Clicked)
        self.radioButtonRed.clicked.connect(self.radioRed_Clicked)
        self.radioButtonBlue.clicked.connect(self.radioBlue_Clicked)
        self.radioButtonGreen.clicked.connect(self.radioGreen_Clicked)

    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)
    def PushButtonDisplay_Clicked(self):
        msg = self.lineEdit.text()
        self.labeluserLabel.setText(msg)

    def radioRed_Clicked(self):
        self.setBackgroundColour("red")

    def radioBlue_Clicked(self):
        self.setBackgroundColour("blue")

    def radioGreen_Clicked(self):
        self.setBackgroundColour("green")
        
    def setBackgroundColour(self, colour):
        self.groupBoxColours.setStyleSheet("background-color: {0}".format(colour))

#Example Slot Function
#   def SaveButton_Clicked(self):
#       Make a call to the Save() helper function here

    #ADD HELPER FUNCTIONS HERE
    # These are the functions the slot functions will call, to 
    # contain the custom code that you'll write to make your progam work.
    # Indent to this level (ie. inside the class, at same level as def __init__)

#Example Helper Function
#    def Save(self):
#       Implement the save functionality here

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY