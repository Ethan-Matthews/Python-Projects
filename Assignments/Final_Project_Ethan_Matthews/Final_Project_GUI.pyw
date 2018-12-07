"""
Student Name:   Ethan Matthews
Program Title:  GRAPHICAL USER INTERFACE (GUI) PROGRAMMING - Final Project
Description:    Use PyQT and Visual Studio Code to create a graphical application
                (.pyw and supporting .py files) in which you’ll code the solution to this program. 
"""

"""
 1. Create muliple objects in pyqt5. List Widget x1, list labels x8, push buton x1, scroll bar x1, menu actions x2, line edit x1,
    radio buttons x2, combo box x1, group box x1 and one object for flag display (not sure what that will be yet).
 2. Add slots for all objects that hav actions when program runs. Some lables are static and won't need any slots.
 3. Connect slots with appropriate functions.  Any Object that has an action when the program is running will have there own functions.
 4. Add Helper functions for reusable calculations I.E percent of world population, conversions between miles and KM, loading and saving from files
    and when the line changes in the list widget.
 5. Opaque object will need to be loaded automatically to cover all controls until user loads a file. 
 6. CSS will need to be applied to GUI interface for nice look. (Done in pyqt5 itself.)
 7. Add comments to code when program is almost complete, or through-out development.
 8. BACKUP ALL WORK ON ONEDRIVE/GITHUB!!!!!
 9. Upload phases to git hub and bright space as they're due.
10. Pray to PC gods that your hard drive doesn't buy the Farm. (Sacrifice at the very least, one goat and three chickens per week.)   
""" 

import sys, csv

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from PyQt5.QtGui import QPixmap

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_Final_Project
#      ^^^^^^^^^^^ Change this!

#CHANGE THE SECOND PARAMETER (Ui_ChangeMe) TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_Final_Project.Ui_MainWindow):
#                         ^^^^^^^^^^^   Change this!

    CountriesList = []

    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY

    

        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
        self.actionLoad_File.triggered.connect(self.LoadCountryMenu_Triggered)
        self.actionSave_File.triggered.connect(self.SaveCountryMenu_Triggered)
        self.listWidgetCountry.currentRowChanged.connect(self.ListRow_Changed)
        self.listWidgetCountry.currentRowChanged.connect(self.flagImage)
        self.listWidgetCountry.currentRowChanged.connect(self.radioButton_Miles)
        self.listWidgetCountry.currentRowChanged.connect(self.ComoboBox_Mile_KM)
        self.radioButtonSquareMile.clicked.connect(self.radioButton_Miles)
        self.radioButtonSquareKM.clicked.connect(self.radioButton_KM)
        self.pushButtonUpdatePopulation.clicked.connect(self.upDateFile)
        self.verticalScrollBarCountryLists.sliderMoved.connect(self.listScroll)

    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)

    def LoadCountryMenu_Triggered(self):
        self.loadFromFile()
        self.LoadintoListWidget()
        self.actionLoad_File.setEnabled(False)

    def SaveCountryMenu_Triggered(self):
        pass

    def ListRow_Changed(self, Index):
        countryName = self.CountriesList[Index][0]
        totalPopulation = self.CountriesList[Index][1]
        totalAreaCountry = self.CountriesList[Index][2]

        countryPercent = self.countryPercentPop(totalPopulation, self.CountriesList)

        self.labelVarCountryName.setText(countryName)
        self.lineEditPopulation.setText(totalPopulation)
        self.labelVarTotalAreaIn.setText("{0:.1f}".format(float(totalAreaCountry)))
        self.labelPercentPopDisplay.setText(countryPercent)
        
    def radioButton_Miles(self, Index):
        self.radioButtonSquareMile.setText("")
        self.radioButtonSquareMile.setChecked(True)
        totalPopulation = self.CountriesList[Index][1]
        totalAreaCountry = self.CountriesList[Index][2]
        
        popPerSqrMile = float(totalPopulation) / float(totalAreaCountry)

        self.labelSquareAreaDisplay.setText("{0:.2f}".format(popPerSqrMile))

    def radioButton_KM(self, Index):
        self.radioButtonSquareKM.setText("")
        self.radioButtonSquareKM.setChecked(True)
        totalPopulation = self.CountriesList[Index][1]
        totalAreaCountry = self.CountriesList[Index][2]

        KMs = float(totalAreaCountry) * 2.59
        
        popPerSqrKM = float(totalPopulation) / KMs

        self.labelSquareAreaDisplay.setText("{0:.2f}".format(popPerSqrKM))

    def ComoboBox_Mile_KM(self):
        self.comboBoxMilesToKM.addItem("Sq. Miles")
        self.comboBoxMilesToKM.addItem("Sq. KM")

    def upDateFile(self):
        pass

    def listScroll(self):
        pass

    def CheckedBox_Changed(self, state):
        pass

    def flagImage(self, Index):
        flagName = self.CountriesList[Index][0]
        space = " "
        underscore = "_"
        if flagName.__contains__(space):
            flagName = flagName.replace(space, underscore)
            countryflag = QPixmap("Flags\{0}.png".format(flagName))
            self.labelImage.setQPixmap(countryflag)
        else:
            countryflag = QPixmap("Flags\{0}.png".format(flagName))
            self.labelImage.setQPixmap(countryflag)


#Example Slot Function
#   def SaveButton_Clicked(self):
#       Make a call to the Save() helper function here

    #ADD HELPER FUNCTIONS HERE
    # These are the functions the slot functions will call, to 
    # contain the custom code that you'll write to make your progam work.
    # Indent to this level (ie. inside the class, at same level as def __init__)
    def loadFromFile(self):
        fileName = "countries.txt"
        accessMode = "r"
        with open(fileName, accessMode) as myFile:
            countryData = csv.reader(myFile)
            for row in countryData:
                self.CountriesList.append(row)

    def LoadintoListWidget(self):
        self.listWidgetCountry.clear()
        for personrow in self.CountriesList:
            self.listWidgetCountry.addItem(personrow[0])

    def countryPercentPop(self, totalPopulation, CountriesList):
        totalWorld = 0
        for counter in range(len(CountriesList)):
            countryPop = int(CountriesList[counter][1])
            totalWorld += countryPop
        countryPercent = float(totalPopulation) / totalWorld
        return str("{0:.4f}%".format(countryPercent))

    def ToggleImage(self, state, Index):
        countryName = self.CountriesList[Index][0]
        if state == 2:
            image = QPixmap("images\{0}.png".format(countryName))
        else:
            image = QPixmap()

        self.labelImage.setPixmap(image)


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