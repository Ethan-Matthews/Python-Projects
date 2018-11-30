import sys, csv

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_loadpeople
#      ^^^^^^^^^^^ Change this!

#CHANGE THE SECOND PARAMETER (Ui_ChangeMe) TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_loadpeople.Ui_MainWindow):
#                         ^^^^^^^^^^^   Change this!

    memoryListOfPeople = []

    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY

        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
        self.LoadPeopleButton.clicked.connect(self.LoadPeopleButton_clicked)
        self.listWidget.currentRowChanged.connect(self.ListRow_Changed)

    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)
    def LoadPeopleButton_clicked(self):
        self.loadFromFile()
        self.LoadintoListWidget()
        self.LoadPeopleButton.setEnabled(False)
        
    def ListRow_Changed(self, newIndex):
        name = self.memoryListOfPeople[newIndex][0]
        age = self.memoryListOfPeople[newIndex][1]

        self.lineEditName(name)
        self.lineEditAge(age)

#Example Slot Function
#   def SaveButton_Clicked(self):
#       Make a call to the Save() helper function here

    #ADD HELPER FUNCTIONS HERE
    # These are the functions the slot functions will call, to 
    # contain the custom code that you'll write to make your progam work.
    # Indent to this level (ie. inside the class, at same level as def __init__)
    def loadFromFile(self):
        fileName = "People.txt"
        accessMode = "r"
        with open(fileName, accessMode) as myFile:
            poepleData = csv.reader(myFile)
            for row in poepleData:
                self.memoryListOfPeople.append(row)

    def LoadintoListWidget(self):
        self.listWidget.clear()
        for personrow in self.memoryListOfPeople:
            self.listWidget.additem(personrow[0])


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