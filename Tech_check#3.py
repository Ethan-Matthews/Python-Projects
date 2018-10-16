#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Ethan Matthews
Program Title:   GPA Calculator
Description:     Take a letter grade and convert it to a GPA.
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    letterModMinus = -0.3
    letterModPlus = 0.3
    gradeA = 4.0
    gradeB = 3.0
    gradeC = 2.0
    gradeD = 1.0
    gradeF = 0.0
    gpa = ""

    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades exept F can include a + or - symbol.")
    print("Calculated grade point values cannot exceed 4.0.")

    letterGrade = input("\nPlease enter your letter grade: ").lower()
    letterMod = input("Please enter a modifier (+, - or nothing): ")
    combineGrade = letterGrade + letterMod

    if (combineGrade == "a") or (combineGrade =="a+"):
        gpa = gradeA
    elif combineGrade == "a-":
        gpa = gradeA + letterModMinus

    if combineGrade == "b":
        gpa = gradeB
    elif combineGrade == "b+":
        gpa = gradeB + letterModPlus
    elif combineGrade == "b-":
        gpa = gradeB + letterModMinus
    
    if combineGrade == "c":
        gpa = gradeC
    elif combineGrade == "c+":
        gpa = gradeC + letterModPlus
    elif combineGrade == "c-":
        gpa = gradeC + letterModMinus

    if combineGrade == "d":
        gpa = gradeD
    elif combineGrade == "d+":
        gpa = gradeC + letterModPlus
    elif combineGrade == "d-":
        gpa = gradeC + letterModMinus

    if combineGrade == "f" or combineGrade =="f-" or combineGrade == "f+":
        gpa = gradeF

    else:
        (letterGrade != "a") or  (letterGrade != "b") or  (letterGrade != "c") or  (letterGrade != "d") or  (letterGrade != "f") or (letterMod != "-") or (letterMod != "+")
        print("Invalid Letter/mod Grade.")
    print("Your GPA is: {0}".format(gpa))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()