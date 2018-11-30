import sys, csv

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_SavePeople
#      ^^^^^^^^^^^ Change this!

#CHANGE THE SECOND PARAMETER (Ui_ChangeMe) TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_SavePeople.Ui_MainWindow):
#                         ^^^^^^^^^^^   Change this!

    memoryListOfPeople = []

    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY

        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
        self.UpdatePersonButton.clicked.connect(self.LoadPeopleMenu_Triggered)
        self.listWidgetFileList.currentRowChanged.connect(self.ListRow_Changed)
        self.UpdatePersonButton.clicked.connect(self.UpdatePersonButton_Clicked)
        self.actionSave_to_File.triggered.connect(self.SaveAction_Triggered)

    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)
    try:
        def SaveAction_Triggered(self):
            self.SaveToFile

        def UpdateButton_Clicked(self):
            name = self.NameField.text()
            age = self.AgeField.text()

            selectedRowIndex = self.listWidgetFileList.currentRow()

            self.memoryListOfPeople[selectedRowIndex][0] = name
            self.memoryListOfPeople[selectedRowIndex][1] = age

            self.LoadPeopleMenu_Triggered()

        def LoadPeopleMenu_Triggered(self):
            self.loadFromFile()
            self.LoadintoListWidget()
            self.LoadPeopleButton.setEnabled(False)
            
        def ListRow_Changed(self, newIndex):
            name = self.memoryListOfPeople[newIndex][0]
            age = self.memoryListOfPeople[newIndex][1]

            self.lineEditName(name)
            self.lineEditAge(age)

        def SaveToFile(self):
            with open("People.txt", "w") as FileConnection:
                for row in self.memoryListOfPeople:
                    rowString = ",".join(row) + "\n"
                    FileConnection.write(rowString)

            QMessageBox.information(self, "Save Window","Message to User",QMessageBox.Ok)
    except:
        QMessageBox.information(self, "Error!","An error occured save aborted!", QMessageBox.Ok)

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
            peopleData = csv.reader(myFile)
            for row in peopleData:
                self.memoryListOfPeople.append(row)

    def LoadintoListWidget(self):
        self.listWidgetFileList.clear()
        for personrow in self.memoryListOfPeople:
            self.listWidgetFileList.addItem(personrow[0])


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