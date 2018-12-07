import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_Tech_Check_07_GUIs
#      ^^^^^^^^^^^ Change this!

#CHANGE THE SECOND PARAMETER (Ui_ChangeMe) TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_Tech_Check_07_GUIs.Ui_MainWindow):
#                         ^^^^^^^^^^^   Change this!

    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY

        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
        self.pushButton_Calculate.clicked.connect(self.CalculateTax)

    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)
    def CalculateTax(self):
        weeklySalary, dependants = self.gatherTaxInput()

        provTax = float(weeklySalary) * 0.06
        fedTax = float(weeklySalary) * 0.25
        depndpercent = float(dependants) * 0.02
        refund = float(depndpercent) * float(weeklySalary)
        totalWithHeld = float(provTax) + float(fedTax) - float(refund)
        totalTakehome = float(weeklySalary) - float(totalWithHeld)

        self.label_ProvicialTaxDisplay.setText("$ {0:.2f}".format(provTax))
        self.label_FederalTaxDisplay.setText("$ {0:.2f}".format(fedTax))
        self.label_2DependantsDisplay.setText("$ {0:.2f}".format(refund))
        self.label_TotalWithheldDisplay.setText("$ {0:.2f}".format(totalWithHeld))
        self.label_TakeHomePayDisplay.setText("$ {0:.2f}".format(totalTakehome))


#Example Slot Function
#   def SaveButton_Clicked(self):
#       Make a call to the Save() helper function here

    #ADD HELPER FUNCTIONS HERE
    # These are the functions the slot functions will call, to 
    # contain the custom code that you'll write to make your progam work.
    # Indent to this level (ie. inside the class, at same level as def __init__)
    def gatherTaxInput(self):
        weeklySalary = self.lineEditSalary.text()
        dependants = self.lineEditDependants.text()
        return weeklySalary, dependants

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