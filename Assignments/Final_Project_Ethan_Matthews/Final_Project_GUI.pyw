"""
Student Name:   Ethan Matthews
Program Title:  GRAPHICAL USER INTERFACE (GUI) PROGRAMMING - Final Project
Description:    Use PyQT and Visual Studio Code to create a graphical application
                (.pyw and supporting .py files) in which you’ll code the solution to this program. 
"""

"""
 1. Create muliple objects in pyqt5. List Widget x1, list labels x8, push buton x1,
    scroll bar x1, menu actions x2, line edit x1, radio buttons x2, combo box x1, group box x1 
    and one label for flag display. 
 2. Add slots for all objects that have actions when program runs.
    Some lables are static and won't need any slots.
 3. Connect slots with appropriate functions.  Any Object that has an action when the program is
    running will have there own functions.
 4. Add Helper functions for reusable calculations I.E percent of world population, conversions between miles and KM, 
    loading and saving from files and when the line changes in the list widget.
 5. Flags folder will need to be in same folder as final project.
 6. Countries.txt needs to be in main directory (Same as workspace file).
 7. When adding functions use function naming convension provided in assignment document.
 8. Opaque object will need to be loaded automatically to cover all controls until user loads a file. 
 9. Add button prompts to program. Will prompt user when data has been loaded into memory.
    When data entered is invalid, and if the user trys to exit before saving any changes made to
    country data. That box will need more than one button. (Yes, No).
10. Use __Contains__ to search flag picture name for underscores.
11. Use {0:,}.format to insert commas every three digits.  Will need to remove commas agian before 
    saving to file.
12. CSS will need to be applied to GUI interface for nice look. (Done in pyqt5 itself.)
13. Add comments to code when program is almost complete, or through-out development.
14. BACKUP ALL WORK ON ONEDRIVE/GITHUB!!!!!
15. Upload phases to git hub and bright space as they're due.
""" 

# Import Libraries
import sys, csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_Final_Project
#      ^^^^^^^^^^^ Change this!

#CHANGE THE SECOND PARAMETER (Ui_ChangeMe) TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_Final_Project.Ui_MainWindow):
#                         ^^^^^^^^^^^   Change this!
# Memory list for country Data
    CountriesList = []
# Global Variable for check unsaved changes
    unSavedChanges = True
    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY

        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
        # Hides all objects before file load.
        self.frame_hider.hide()
        # Greys out save button in file menu.
        self.actionSave_File.setEnabled(False)
        # Slot for load file trigger.
        self.actionLoad_File.triggered.connect(self.LoadCountryMenu_Triggered)
        # Slot for save file trigger.
        self.actionSave_File.triggered.connect(self.SaveCountryMenu_Triggered)
        # Slot for activating functions when list row is changed.
        self.listWidgetCountry.currentRowChanged.connect(self.ListRow_Changed)
        # Slot triggers when radio button miles is clicked.
        self.radioButtonSquareMile.clicked.connect(self.radioButtonMiles)
        # Slot triggers when radio button KM is clicked.
        self.radioButtonSquareKM.clicked.connect(self.radioButtonKM)
        # Slot creates combobox opations miles KM.
        self.comboBoxMilesToKM.currentIndexChanged.connect(self.comboBoxMilesToKM_Switched)
        # Slot triggers when population button is clicked.
        self.pushButtonUpdatePopulation.clicked.connect(self.updateList_Triggered)
        # Slot triggers when Exit id triggered.
        self.actionExit.triggered.connect(self.changesCheck_Check)

    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)

    # Slot fuction that calls helper functions when load File is actived.
    def LoadCountryMenu_Triggered(self):
        self.LoadCountriesFromFile()
        self.LoadCountriesListBox()
        # Changes state of of load and save menu items.
        self.actionLoad_File.setEnabled(False)
        self.actionSave_File.setEnabled(True)

    # Slot fuction that calls helper functions when save File is actived.
    def SaveCountryMenu_Triggered(self):
        self.SaveCountriesToFile()

    # Slot fuction that calls helper functions when list row is changed.
    def ListRow_Changed(self):
        newIndex = self.listWidgetCountry.currentRow()
        # Hides 'hider' frame.
        self.frame_hider.show()
        self.ListRow_ChangedAction(newIndex)
        self.flagImageAction(newIndex)
        # Generates Combo buttons
        self.ComoboBox_Mile_KM_Gen()
        # Actives radio button in miles (default).
        self.radioButtonSquareMile.setChecked(True)
        self.radioButtonMiles(newIndex)
    
    # Function that adds comboBox items.
    def ComoboBox_Mile_KM_Gen(self):
        self.comboBoxMilesToKM.clear()
        self.comboBoxMilesToKM.addItem("Sq. Miles")
        self.comboBoxMilesToKM.addItem("Sq. KM")

    # Slot function that triggers updateList helper function.
    def updateList_Triggered(self):
        self.updateListPop()

    # Changes Displayed calculations of comboBoxes.
    def comboBoxMilesToKM_Switched(self, enabled):
        if enabled:
            self.comoboBoxKM()
        else:
            self.comboBoxMiles()

    # Checks if there are unsaved changes in the file. Prompts user with QMessage if there are any.
    def changesCheck_Check(self):
        if self.unSavedChanges == True:
            message = "Save changes to file before closing?"
            prompt = QMessageBox.question(self, 'Save?', message, QMessageBox.Yes, QMessageBox.No)
            if prompt == QMessageBox.Yes:
                self.SaveCountryMenu_Triggered()
                QApplication.closeAllWindows()
        else:
            QApplication.closeAllWindows()

    #  Checks if there are unsaved changes in the file when user uses close box top right X.
    def closeEvent(self, event):
        if self.unSavedChanges == True:
            self.changesCheck_Check()


#Example Slot Function
#   def SaveButton_Clicked(self):
#       Make a call to the Save() helper function here

    #ADD HELPER FUNCTIONS HERE
    # These are the functions the slot functions will call, to 
    # contain the custom code that you'll write to make your progam work.
    # Indent to this level (ie. inside the class, at same level as def __init__)
    # Loads the country file into memory list with CVS reader.
    def LoadCountriesFromFile(self):
        fileName = "countries.txt"
        accessMode = "r"
        with open(fileName, accessMode) as myFile:
            countryData = csv.reader(myFile)
            for row in countryData:
                self.CountriesList.append(row)

    # Saves updated list to external file.
    def SaveCountriesToFile(self):
        fileName = "countries.txt"
        accessMode = "w"
        with open(fileName, accessMode) as myFile:
            for row in range(len(self.CountriesList)):
                    myFile.write(",".join(self.CountriesList[row]) + "\n")
        # sets global variable unSavedChanges to False.
        self.unSavedChanges = False

    # Loads text lines into list widget.
    def LoadCountriesListBox(self):
        self.listWidgetCountry.clear()
        for row in self.CountriesList:
            self.listWidgetCountry.addItem(row[0])

    # Runs when list row is changed.  Displays Country information.
    def ListRow_ChangedAction(self, newIndex):
        newIndex = self.listWidgetCountry.currentRow()
        countryName = self.CountriesList[newIndex][0]
        totalPopulation = self.CountriesList[newIndex][1]
        totalAreaCountry = self.CountriesList[newIndex][2]

        countryPercent = self.CalculateTotalWorldPopulation(totalPopulation, self.CountriesList)

        self.labelVarCountryName.setText(countryName)
        self.lineEditPopulation.setText("{:,}".format(int(totalPopulation)))
        self.labelVarTotalAreaIn.setText("{0:,}".format(int(totalAreaCountry)))
        self.labelPercentPopDisplay.setText("{0:.4f}%".format(float(countryPercent)))

    # Changes Flag image displayed when row in list widget is changed.
    def flagImageAction(self, newIndex):
        newIndex = self.listWidgetCountry.currentRow()
        flagName = self.CountriesList[newIndex][0]
        space = " "
        underscore = "_"
        if flagName.__contains__(space):
            flagName = flagName.replace(space, underscore)
            countryflag = QPixmap("Flags\{0}.png".format(flagName))
            self.labelFlagImage.setPixmap(countryflag)
        else:
            countryflag = QPixmap("Flags\{0}.png".format(flagName))
            self.labelFlagImage.setPixmap(countryflag)

    # Calculates the total world population from countries.txt with loop. No Google required.
    def CalculateTotalWorldPopulation(self, totalPopulation, CountriesList):
        totalWorld = 0
        for counter in range(len(CountriesList)):
            countryPop = float(CountriesList[counter][1])
            totalWorld += countryPop
        countryPercent = int(totalPopulation) / totalWorld * 100
        return countryPercent

    # Activates when radio button is clicked. Displays Miles.
    def radioButtonMiles(self, enabled):
        newIndex = self.listWidgetCountry.currentRow()
        totalPopulation = self.CountriesList[newIndex][1]
        totalAreaCountry = self.CountriesList[newIndex][2]
            
        popPerSqrMile = float(totalPopulation) / float(totalAreaCountry)

        self.labelSquareAreaDisplay.setText("{0:.2f}".format(popPerSqrMile))

    # Activates when radio button is clicked. Displays KMs.
    def radioButtonKM(self, enabled):
        newIndex = self.listWidgetCountry.currentRow()
        totalPopulation = self.CountriesList[newIndex][1]
        totalAreaCountry = self.CountriesList[newIndex][2]
        KMs = float(totalAreaCountry) * 2.59
        popPerSqrKM = float(totalPopulation) / KMs
        self.labelSquareAreaDisplay.setText("{0:.2f}".format(popPerSqrKM))

    # Activates when combo box is actived. Displays population per Square Mile.
    def comboBoxMiles(self):
        newIndex = self.listWidgetCountry.currentRow()
        totalAreaCountryMI = self.CountriesList[newIndex][2]
        self.labelVarTotalAreaIn.setText("{0:,}".format(int(totalAreaCountryMI)))

    # Activates when combo box is actived. Displays population per Square KM.
    def comoboBoxKM(self):
        newIndex = self.listWidgetCountry.currentRow()
        totalAreaCountry = self.CountriesList[newIndex][2]
        totalAreaCountryKM = int(totalAreaCountry) * 2.59
        self.labelVarTotalAreaIn.setText("{0:,}".format(int(totalAreaCountryKM)))

    # Activates when update population button is clicked. Saves value to memory list.
    def updateListPop(self):
        popString = self.lineEditPopulation.text()
        newIndex = self.listWidgetCountry.currentRow()
        comma = ","
        null = ""
        if popString.__contains__(comma):
            popString = popString.replace(comma, null)
        if popString.isnumeric() == True:
            self.CountriesList[newIndex][1] = self.lineEditPopulation.text()
            # QBox tells user if data has been updated to memory list, or if data is invalid.
            QMessageBox.information(self, "Updated","Data has been updated in memory, but hasn't been updated in the file yet", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Invalid","Data is invalid so not updated in memory.", QMessageBox.Ok)

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