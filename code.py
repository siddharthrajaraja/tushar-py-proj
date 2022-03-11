import pandas as pd
import numpy as np

PROJECT_NAME = "MY UNIVERSITY"
INSTIUTION_TYPE = "UNIVERSITY"
NAME = "name"
ROLL = "roll"
ADDRESS = "address"
MOBILE = "mobile"
ENGLISH = "english"
HINDI = "hindi"
MATH = "math"
SST = "sst"
SCIENCE = "science"

student_df = pd.DataFrame()


def print_welcome_message():
    """
    This function prints the welcome message.
    """

    message = f"""
    Hello Geek, welcome to {PROJECT_NAME}, this project helps you manage the {INSTIUTION_TYPE} digitally.
    """
    print(message)


def print_helper_message():
    """
    This function prints the steps needed to be followed.
    """

    message = f"""
    {PROJECT_NAME} supports the following :\n 
    0) EXIT\n
    1) INSERT STUDENT DETAILS\n
    2) DISPLAY SPECIFIC STUDENT DETAILS USING ROLL NO\n
    3) DISPLAY ALL STUDENT DETAILS\n
    4) MODIFY STUDENT DETAILS USING ROLL NO\n
    5) DELETE STUDENT DETAILS USING ROLL NO\n
    6) ANALYSE STUDENT PERFORMANCE\n
    """
    print(message)


def display_student_details(roll_no: str):
    """
    This function displays student details using roll number
    """
    global student_df
    print(student_df.query(f"roll=={roll_no}"))


def display_students_details():
    """
    This function displays entire dataframe
    """
    global student_df
    print(student_df)


def insert_student_details() -> str:
    """
    This function helps the admin to insert student details.
    """
    global student_df

    student_dict = dict()
    student_name = input("ENTER STUDENT NAME : ")
    student_roll = input("ENTER ROLL NUMBER : ")
    student_address = input("ENTER STUDENT ADDRESS : ")
    student_mobile = input("ENTER MOBILE NUMBER : ")
    student_english_marks = float(input("ENTER ENGLISH MARKS (OUT OF 100) : "))
    student_hindi_marks = float(input("ENTER HINDI MARKS (OUT OF 100) : "))
    student_maths_marks = float(input("ENTER MATHS MARKS (OUT OF 100) : "))
    student_sst_marks = float(input("ENTER SST MARKS (OUT OF 100) : "))
    student_science_marks = float(input("ENTER SCIENCE MARKS (OUT OF 100) : "))

    if (
        student_english_marks < 0
        or student_hindi_marks < 0
        or student_maths_marks < 0
        or student_science_marks < 0
        or student_sst_marks < 0
    ):
        return "\nINVALID MARKS ENTRY"
    student_dict[NAME] = student_name
    student_dict[ROLL] = student_roll
    student_dict[ADDRESS] = student_address
    student_dict[MOBILE] = student_mobile
    student_dict[ENGLISH] = student_english_marks
    student_dict[HINDI] = student_hindi_marks
    student_dict[MATH] = student_maths_marks
    student_dict[SST] = student_sst_marks
    student_dict[SCIENCE] = student_science_marks

    student_df = student_df.append(student_dict, ignore_index=True)

    return "\nRECORD INSERTED"


def main():

    global student_df

    print_welcome_message()

    while True:
        print_helper_message()
        choice = int(input("ENTER CHOICE :"))
        if choice == 0:
            break
        elif choice == 1:
            print(insert_student_details())
        elif choice == 2:
            roll_no = input("ENTER ROLL NUMBER TO SEARCH : ")
            display_student_details(roll_no)
        elif choice == 3:
            display_students_details()


if __name__ == "__main__":

    main()
