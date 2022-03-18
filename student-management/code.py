import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "student.csv"

PROJECT_NAME = "STUDENTS MANAGEMENT SYSTEM"
INSTIUTION_TYPE = "SCHOOL"
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

def read_file():
    """
    This function reads the csv file and stores the student information in pandas dataframe.
    """
    global student_df 
    df = pd.read_csv(FILE_NAME)
    student_df = student_df.append(df)
    print("READ STUDENT INFORMATION FILE FROM FILE")
    print(student_df)
    print(student_df.info())
    
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
    7) ANALYSE CLASS PERFORMANCE\n
    """
    print(message)


def display_student_details(roll_no: str):
    """
    This function displays student details using roll number
    """
    global student_df

    print(student_df[student_df[ROLL] == roll_no])


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


def delete_student(roll_number):
    """
    This function deleted student by its roll number.
    """
    global student_df

    student_df = student_df.loc[student_df[ROLL] != roll_number]

    print("RECORD DELETED")
    print(student_df)


def modify_student_details(roll_no):
    """
    This function modifies student record by its roll number.
    """
    global student_df

    student_dict = dict()
    student_name = input("UPDATE STUDENT NAME : ")
    student_roll = roll_no
    student_address = input("UPDATE STUDENT ADDRESS : ")
    student_mobile = input("UPDATE MOBILE NUMBER : ")
    student_english_marks = float(input("UPDATE ENGLISH MARKS (OUT OF 100) : "))
    student_hindi_marks = float(input("UPDATE HINDI MARKS (OUT OF 100) : "))
    student_maths_marks = float(input("UPDATE MATHS MARKS (OUT OF 100) : "))
    student_sst_marks = float(input("UPDATE SST MARKS (OUT OF 100) : "))
    student_science_marks = float(input("UPDATE SCIENCE MARKS (OUT OF 100) : "))

    if (
        student_english_marks < 0
        or student_hindi_marks < 0
        or student_maths_marks < 0
        or student_science_marks < 0
        or student_sst_marks < 0
    ):
        return "\nINVALID MARKS ENTRY"
    delete_student(roll_no)

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
    return "\n RECORD UPDATED"

def get_percentage(marks_dic):
   """
   This function gets percentage of all marks obtained by student
   """
   return (marks_dic[ENGLISH]+marks_dic[HINDI]+marks_dic[MATH]+marks_dic[SST]+marks_dic[SCIENCE])/len(marks_dic)

def isPass(percentage):
   """
   This function prints whether student is passed or fail
   """
   return percentage>=33.33
   
def analyse_student_performance(roll_no):
   """
   This function generates student report card and graphically visualises student marks
   """
   global student_df
   roll_no = (roll_no)
   df = student_df[student_df[ROLL] == roll_no]
   student_name = df[NAME][0]
   data = {
      MATH: df[MATH][0],
      ENGLISH: df[ENGLISH][0],
      HINDI: df[HINDI][0],
      SST: df[SST][0],
      SCIENCE: df[SCIENCE][0] 
   }
   percentage = get_percentage(data)
   status = "PASSED" if(isPass(percentage)) else "FAILED"
   plt.bar(list(data.keys()),list(data.values()),width=0.5)
   plt.xlabel("SUBJECTS")
   plt.ylabel("MARKS OBTAINED OFF 100")
   plt.title(label=f"{student_name} {status} with {percentage}%")
   plt.show()

def analyse_class_performance():
   """
   This function generates a line chart which compares marks obtained by
   different students in different subjects
   """
   global student_df

   plt.figure()

   for _,every in student_df.iterrows():
      student_name = every[NAME]
      data = {
         MATH: every[MATH],
         ENGLISH: every[ENGLISH],
         HINDI: every[HINDI],
         SST: every[SST],
         SCIENCE: every[SCIENCE] 
      }
      weeks = data.keys()
      values = data.values()
      plt.plot(weeks,values,label=f"{student_name}")
   plt.ylabel('MARKS OBTAINED')
   plt.xlabel('SUBJECTS')
   plt.legend(loc='lower right')
   plt.title("PERFORMANCE OF CLASS")
   plt.show()

def main():

    global student_df
    
    read_file()

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
        elif choice == 4:
            roll_no = input("ENTER ROLL NUMBER TO SEARCH : ")
            print(modify_student_details(roll_no))
        elif choice == 5:
            roll_no = input("ENTER ROLL NUMBER TO SEARCH : ")
            delete_student(roll_no)
        elif choice == 6:
            roll_no = input("ENTER ROLL NUMBER TO SEARCH : ")
            analyse_student_performance(roll_no)
        elif choice == 7:
            analyse_class_performance()

if __name__ == "__main__":

    main()
