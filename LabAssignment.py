import csv
import os
import numpy as np
from pprint import pprint
from hashlib import md5
from hashlib import sha256



grades_db ={}
class Student:
    studentId =0
    studentIdMap ={}
    def __init__(self,fname,lname,email,courseId):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.courseId =courseId
        
        if self.email in Student.studentIdMap :
            self.studentId = Student.studentIdMap[self.email]
        else :    
            Student.studentId +=1
            self.studentId = 'S'+str(Student.studentId)
            Student.studentIdMap[self.email] = 'S'+str(Student.studentId)
    
    def check_my_grades(self, filename):
        if fileExists(filename):
            with open(filename,'r',newline='') as file1 :
                reader = csv.reader(file1)
                print('below are the course_id with grades :: ')
                for idx, row in enumerate(reader):
                    if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                        continue 
                    if row[0] == self.email:
                        print(row[3] +'-'+ row[4])
        else:
            print('No grades exists')
        
    def check_my_marks(self,filename):
        if fileExists(filename):
            with open(filename,'r',newline='') as file1:
                    reader = csv.reader(file1)
                    for idx,row in enumerate(reader):
                        if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                            continue 
                        if row[0] == self.email :
                            print(row[4]+'-'+row[5])
        else :
            print('No marks added for you !!')    

class Course:
    courseId =0
    courseIdMap ={}
    def __init__(self,credits,courseName):
        self.credits = credits
        self.courseName = courseName

        if self.courseId in Course.courseIdMap :
            self.courseId = Course.courseIdMap[self.courseId]
        else :    
            Course.courseId +=1
            self.courseId = 'C'+str(Course.courseId)
            Course.courseIdMap[self.courseId] = 'C'+str(Course.courseId)

    
class Professor:
    professorId =0
    ProfIdMap ={}
    def __init__(self,name,email,rank,course_id):
        self.name = name
        self.email = email
        self.rank = rank
        self.course_id = course_id
        
        if self.email in Professor.ProfIdMap:
            self.professorId = Professor.ProfIdMap[self.email]
        else :
            Professor.professorId +=1
            self.professorId = 'P'+str(Professor.professorId)
            Professor.ProfIdMap[self.email] = 'P'+str(Professor.professorId)  

    # UPDATE STUDENT RECORD
    def update_student_records(self,filename,student,grade,marks):
        print('Professor can only update the marks and grades of the student !!!!!')
        marksval = marks.replace('.','')
        updatedStudents =[]
        studFound = False
        if marksval.isdigit():
            if fileExists(filename) :
                with open(filename,'r',newline='') as file1:
                    reader = csv.reader(file1)
                    header = next(reader, None)
                    if header:
                        updatedStudents.append(header)
                    for idx,row in enumerate(reader):
                        if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                            continue 
                        if(row[0].lower() == student.email.strip().lower() and row[3].lower() == student.courseId.lower()):
                            row[4] = grade
                            row[5] = float(marks)
                            updatedStudents.append(row)
                            studFound = True
                        else:
                            updatedStudents.append(row)  
                if studFound:             
                    with open(filename,'w',newline='') as file2:
                        writer = csv.writer(file2)
                        writer.writerows(updatedStudents) 
                    print(f'{student.email} marks has been updated to {float(marks)}')    
        else:
            print('Marks can only be integer or float values !!!')          

    def add_grade(self,filename) :
        studentemail = input('Enter the student email address :: ')
        courseid = input('Enter the course id :: ')
        studFound = False
        if fileExists(filename):
            with open(filename,'r') as file1:
                reader = csv.reader(file1)
                for idx, row in enumerate(reader):
                    if row[0] == studentemail.strip() and row[3] == courseid.strip():
                        studFound = True
                        break
                else:
                    print(f'No student found with {studentemail} email address in {courseid} course')
                    return
                if studFound :
                    gradeval = input('Enter the grade :: ')
                    marks = input('enter the marks :: ')
                    marksval = marks.replace('.','')
                    if marksval.isdigit():
                        grade = Grades(gradeval,marks,None)
                        self.addModifyGrade(grade,'Student.csv',studentemail,courseid)
                    else:
                        print('Marks can only be integres or float values !!!')  
        else :
            print('No student found!!!')              

    def addModifyGrade(self, grade, filename,studentemail,courseid):
        updaterows =[]
        if fileExists(filename):
            with open(filename ,'r') as file1:
                reader = csv.reader(file1)
                for idx, row in enumerate(reader):
                    if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                        continue 
                    if row[0] == studentemail.strip() and row[3] == courseid.strip():
                        row[4] = grade.grade
                        row[5] = float(grade.marks)
                        updaterows.append(row)
                    else:
                        updaterows.append(row) 
            with open(filename,'w') as file2:
                writer = csv.writer(file2)
                writer.writerows(updaterows)
                print('grade updated successfully')
        else:
            print('No student found !!')

    def deletegrade(self,filename):
        studentemail = input('Enter the student email address')
        courseid = input('Enter the course id')
        studFound = False
        updaterows =[]
        if fileExists(filename):
            with open(filename,'r') as file1:
                reader = csv.reader(file1)
                for idx, row in enumerate(reader):
                    if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                        continue 
                    if row[0] == studentemail.strip() and row[3] == courseid.strip():
                        row[4] =''
                        row[5] =0
                        updaterows.append(row)
                        studFound = True
                    else:
                        updaterows.append(row)
            if studFound:
                with open(filename,'w') as file1:
                    writer = csv.writer(file1)
                    writer.writerows(updaterows)
                    print('Grade deleted successfully !!')
            else :
                print(f'No such student found with {studentemail}') 
        else:
            print('No student found!!')        

    # MODIFY STUDENTS MARKS . In add grade method logic for modify is also written                   
    def modifyGrades(self, filename):
        self.add_grade(filename)
    
# grades will be added, deleted and modified for the students by professor       
class Grades:
    def __init__(self,grade,marks, marksrange):
        self.grade = grade
        self.marksrange = marksrange
        self.marks = marks

class LoginUser:
    def __init__(self,email,password,role):
        self.email = email
        self.password = password
        self.role = role
    # works for both encryption and decryption
    def getHashValue(self,message,type):
        if type.upper() == 'MD5':
           return md5(message.encode())
        elif type.upper() == 'SHA256':
           return sha256(message.encode())
        else:
            print("Did not find the algo to produce the hash value. Possible types are MD5/SHA256")
    

    def login(self):
        if fileExists('LoginDB.csv'):
            with open('LoginDB.csv', 'r') as file1:
                reader = csv.reader(file1)
                next(reader)
                for row in reader:
                    if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                        continue 
                    if self.email.lower() == row[0].strip().lower():
                        hasedpass = self.getHashValue(self.password,'sha256').hexdigest()
                        if hasedpass.strip() == row[1].strip().lower():
                            return True, row[2]
                        else:
                            print('Incorrect password !!')
                            return False, None
                print('No user exists !!!')
                return False, None     
        else:
            return False, None
    def signup(self) :
        file_exists = fileExists('LoginDB.csv')
        with open('LoginDB.csv', 'a+', newline='') as file1:
            writer = csv.writer(file1)
            file1.seek(0)
            reader = csv.reader(file1)
            if not file_exists:
                writer.writerow(['Email', 'Password', 'Role'])
            for row in reader: 
                if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                    continue   
                if self.email == row[0].strip():
                    print('User email already exists !!!')
                    return  
            enc_password = self.getHashValue(self.password,'sha256').hexdigest()
            writer.writerow([self.email, enc_password.strip(), self.role])
            print('User signed up successfully!')

    def logout(self):
        print('Logged Out!!!')
        mainmethod()

    def change_password(self):
        if fileExists('LoginDB.csv'):
            filetoUpdate =[]
            userfound = False
            with open('LoginDB.csv', 'r') as file1:
                reader = csv.reader(file1)
                for idx, row in enumerate(reader):
                    if row[0].strip().lower() == self.email.strip().lower():
                        userinput = input('Enter your new password :: ')
                        enc_password = self.getHashValue(userinput,'sha256').hexdigest()
                        row[1] = enc_password.strip()
                        filetoUpdate.append(row)
                        userfound = True
                    filetoUpdate.append(row)  
                if  userfound :
                    with open('LoginDB.csv', 'r') as file1:
                        writer = csv.writer(file1) 
                        writer.writerows(filetoUpdate) 
                        print('Password changed !!!')
                else :
                    print('No user found with this email address !!')         

class Admin :
    def __init__(self):
        pass
        
    # SHOW STUDENTS RECORDS  
    def display_records(self,filename):

        if fileExists(filename): 
            with open(filename,mode ='r',newline='') as file1:
                reader = csv.reader(file1)
                print('Below are the all students records')
                for idx,rows in enumerate(reader):
                    print(rows) 

    # ADD NEW STUDENT
    def add_new_student(self,filename, student):
        if(any(value is None or value =='' for value in vars(student).values())):
            print('You have missed to provide some information. Please try again')
        else :    
            
            with open (filename,'a',newline='') as file2:
                writer = csv.writer(file2)
                if fileExists(filename) == False :
                    writer.writerow(['Email','FirstName','LastName','CourseId','Grades','Marks','StudentId'])    
                writer.writerow([student.email,student.fname,student.lname,student.courseId,'','',student.studentId])
                print(f'Student added succesfully with student id as {student.studentId}')
                return  student.email,student.fname,student.lname,student.courseId,'','',student.studentId 

    # DELETE STUDENT
    def delete_new_students(self,filename, email):
        filteredStuds =[]
        student_found = False  
        if fileExists(filename):
            with open(filename,'r',newline='') as file1 :
                reader = csv.reader(file1)
                for idx, row in enumerate(reader):
                    if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                        continue 
                    if row[0].lower() != email.strip().lower() :
                        filteredStuds.append(row)
                    elif row[0] == email.strip().lower() : 
                        student_found = True  
            if student_found:                               
                with open(filename, 'w',newline='') as file2:
                    writer = csv.writer(file2)
                    writer.writerows(filteredStuds) 
                    print(f'Student with {email} deleted !!!')
            else:
                print('No student found with this email address')                       
    # SHOW PROFESSOR DETAILS
    def professor_details(self,filename, professor):
        if fileExists(filename):
            with open(filename,'r') as file1:
                reader = csv.reader(file1)
                for idx, row in enumerate(reader):
                    if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                        continue 
                    if row[2].lower() == professor.email.lower():
                        print(row)
                        break
                else:
                    print('No professor with such email address exists !!!') 
    
    # ADD PROFESSOR DETAILS
    def add_new_professor(self,filename, professor):
        with open(filename,'a') as file2:
            writer = csv.writer(file2)
            if fileExists(filename) == False :
                writer.writerow(['ProfessorId','Name','Email','Rank','CourseId'])    
            writer.writerow([professor.professorId,professor.name,professor.email,professor.rank,professor.course_id])
    
    # DELETE PROFESSOR
    def delete_professor(self,filename, emailadd):
        updateProfs =[]
        proffound = False
        with open(filename,'r') as file1:
            reader = csv.reader(file1)
            for idx, row in enumerate(reader):
                if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                    continue 
                if row[2].lower() == emailadd.strip().lower():
                    proffound = True
                    continue
                updateProfs.append(row)
        if proffound: 
            with open(filename,'w') as file2:   
                writer = csv.writer(file2) 
                writer.writerows(updateProfs) 
                print(f"Professor with email {emailadd} has been deleted.")
        else :
              print(f"No professor with email {emailadd} found.")
    
    # MODIFY PROFESSOR DETAILS
    def modify_professor_details(self,filename,professor): 
        pemail =input('enter the email address of the professor you want to modify :: ')
        name = input('Enter the modified name if any :: ')
        rank = input('Enter the modified rank if any :: ')
        course_id = input('Enter the course_id if any :: ')
        updateProfs =[]
        proffound = False
        with open(filename,'r') as file1:
            reader = csv.reader(file1)
            for idx, row in enumerate(reader):
                if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                    continue 
                if row[2].lower() == pemail.strip.lower():
                    row[1] = name.strip()
                    row[3] = rank.strip()
                    row[4] = course_id.strip()  
                    updateProfs.append(row) 
                    proffound = True 

                updateProfs.append(row)     
        if proffound :
            with open(filename,'w') as file2:
                writer = csv.writer(file2)
                writer.writerows(updateProfs)
                print('Professor details are updated!!')
        else:
            print('No professor found with this email address')        

    # SHOW COURSE OF A PROFESSOR            
    def show_course_details_by_professor(self,filename,email):
        updateProfs =[]
        if fileExists(filename):
            with open(filename,'r') as file1:
                reader = csv.reader(file1)
                for idx, row in enumerate(reader):
                    if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                        continue 
                    if row[2].lower() == email.strip().lower():
                        print('Course Id ::: ',row[4])

                else:
                    print('No professor found with this email id')  
    # ADD COURSE
    def add_new_course(self, filename, course):
        if fileExists(filename):
            with open(filename, 'r', newline='') as file1:
                reader = csv.reader(file1)
                for row in reader:
                    if row and row[0].strip().lower() == course.courseId.strip().lower():  # Course already exists
                        print('Course already exists!')
                        return
        self.add_course(filename, course)

    def add_course(self, filename, course):        
        file_exists = fileExists(filename)
        with open(filename, 'a', newline='') as file1:
            writer = csv.writer(file1)
            if not file_exists:
                writer.writerow(['CourseId', 'Credits', 'CourseName'])    
            writer.writerow([course.courseId, course.credits, course.courseName])
            print('New course added!')  
    
    # DELETE A COURSE
    def delete_course(self,filename,courseid):
        rows =[]
        coursefound = False
        if fileExists(filename):
            with open(filename, 'r',newline='') as file1:
                reader = csv.reader(file1)
                for idx, row in enumerate(reader):
                    if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                        continue
                    if row[0].strip().lower() == courseid.strip().lower():
                        coursefound = True 
                    else :    
                        rows.append(row)     
                if coursefound == False:
                    print('Course Id not found')
                    return
                elif coursefound == True:
                    print(f'Course id {courseid} deleted !!')
                    with open(filename,'w',newline='') as file2:
                        writer = csv.writer(file2)
                        writer.writerows(rows) 
    # MODIFY COURSE                
    def modifycourse(self, filename, course):
        updatedCourse =[]
        coursefound = False
        if fileExists(filename):
            with open(filename,'r',newline='') as file1:
                    reader = csv.reader(file1)
                    header = next(reader, None)
                    if header:
                        updatedCourse.append(header)
                    for idx,row in enumerate(reader):
                        if not row or all(not cell.strip() for cell in row):  # Skip blank rows
                            continue 
                        if(row[0].lower() == course.courseId.strip().lower()):
                            row[1] = course.credits.strip()
                            row[2] = course.coursName.strip()
                            coursefound =True
                            updatedCourse.append(row)
                        else:
                            updatedCourse.append(row)
            if not coursefound:
                print('No course Found with this id') 
                return  
            elif coursefound:                
                with open(filename,'w',newline='') as file2:
                    writer = csv.writer(file2)
                    writer.writerows(updatedCourse)
                print('Course is updated succesfully')
    # DISPLAY ALL COURSES
    def display_Allcourses(self, filename):
        if fileExists(filename): 
            with open(filename,'r',newline='') as file1:
                reader = csv.reader(file1)
                for idx,row in enumerate(reader):
                    print(row)     

    def showDetails(self, searchId):
        if searchId is None or searchId == '':
            raise Exception('Search Id cannot be blank or none')
        SP=[]
        if fileExists('Student.csv') :
            with open('Student.csv','r') as file1:
                reader = csv.reader(file1)
                for idx,val in enumerate(reader):
                    if not val or all(not cell.strip() for cell in val):  # Skip blank rows
                        continue  
                    if val[6] == searchId:
                        SP.append(val)

        if len(SP) ==0 :
            if fileExists('Professor.csv'):
                with open('Professor.csv','r') as file1:
                    reader = csv.reader(file1)
                    for idx,val in enumerate(reader):
                        if not val or all(not cell.strip() for cell in val):  # Skip blank rows
                            continue 
                        if val[0] == searchId:
                            SP.append(val)
        if len(SP) >0:
            print('below is the search result : ')
            print(SP) 
        else:
            print('No records exists for this Id')                   

    def sortRecords(self,professororStudent,filename):
        returnnone =[]
        if fileExists(filename):
            print('Sorting done on email address provided !!! ')
            if professororStudent.lower() == 'professor' :
                with open(filename,'r') as file1:
                    reader = csv.reader(file1)
                    next(reader) #removes header
                    data = list(reader)  
                    for row in data:
                        print('row[0] :: ', row[0])
                    sorted_professor = sorted(
                    data,
                    key=lambda x: x[0].strip().lower()  # Sorting by the first column (email) in lowercase
                    ,reverse=False)
                pprint(sorted_professor)
                return sorted_professor
                
            elif  professororStudent.lower() == 'student' :
                with open(filename,'r') as file2:
                    reader = csv.reader(file2)
                    next(reader) #removes header
                    data = list(reader)
                    sorted_students = sorted(
                        data,
                        key=lambda x: x[2].strip().lower(),reverse=False
                    )
                    pprint(sorted_students)
                    return sorted_students
            else:
                print('Incorrect Input')  
                return returnnone 

    def getmarkslist(courseId) :
        markslist =[]
        if fileExists('Student.csv'):
            with open('Student.csv','r') as file2:
                reader = csv.reader(file2)
                for idx, row in enumerate(reader):
                    if row[3] == courseId:
                        markslist.append(float(row[5]))

                print('Below is the markslist :::')
                print(markslist)
            return markslist

    def getMean(self,courseId) :
        markslist = self.getmarkslist(courseId)
        if len(markslist) > 0 :        
            mean = np.mean(markslist)
            print(f'mean of marks in {courseId} is {mean}')
        else :
            print('No data found')    

    def getMedian(self,courseId) :
        markslist = self.getmarkslist(courseId)
        if len(markslist) >0:         
            median = np.median(markslist)
            print(f'median of marks in {courseId} is {median}')  
        else :
            print('No data found')  

    def display_grades_report(self,filename):
        studreps =[]
        if fileExists(filename):
            with open(filename, 'r') as file1:
                reader = csv.reader(file1)
                next(reader)
                for idx,row in enumerate(file1):
                    studreps.append(row) 
            if len(studreps) >0:
                print('Below is the grade reports of all the students:: ')          
                pprint(studreps)            

def mainmethod():
    while True:
        print("****************************")
        print('Welcome to GradeApp !!!')
        print('1. Login')
        print('2. SignUp')
        print('3. Change Password')
        print("****************************")
        loginorSignup = input('select one :: ')
        if loginorSignup == '1':
            loginEmail = input('enter your email address :: ')
            loginpass = input('enter your password :: ')
            lguser = LoginUser(loginEmail,loginpass,None)
            status,type = lguser.login()
            if status == True:
                    if type.lower() == 'admin':
                        adminuser = Admin()
                        while True:
                            print("************WELCOME ADMIN****************")
                            print('1. Add Students')
                            print('2. Delete Student')
                            print('3. Search a Student or Professor')
                            print('4. add professor')
                            print('5. delete professor')
                            print('6. Get courses of a professor')
                            print('7. Get Professsor details')
                            print('8. Modify professor details')
                            print('9. sort professor or student')
                            print('10. Find mean of marks of a particular course')
                            print('11. Find median of marks in a particular course')
                            print('12. Add Course')
                            print('13. Delete a course')
                            print('14. Modify the course')
                            print('15. Display all courses')
                            print('16, show grade reports')
                            print('17. Logout')
                            print("*****************************************************")
                            pInput = input('Select your choice :: ')

                            if pInput =='1':
                                fname,lname,email,courseId = getStudentInfo()
                                student = Student(fname,lname,email,courseId)
                                adminuser.add_new_student('Student.csv',student)
                            elif pInput =='2':
                                email = getStudentEmail()
                                adminuser.delete_new_students('Student.csv', email)    
                            elif pInput == '3' :
                                searchId = getId()
                                adminuser.showDetails(searchId)
                            elif pInput == '4':
                                pname,email,rank,courseId = getProfInfo()
                                prof = Professor(pname,email,rank,courseId)
                                adminuser.add_new_professor('Professor.csv',prof)
                            elif pInput =='5' :
                                email = getpemailId()  
                                adminuser.delete_professor('Professor.csv',email)
                            elif pInput =='6':
                                email = getpemailId()  
                                adminuser.show_course_details_by_professor('Professor.csv', email)
                            elif pInput == '7':
                                email = getpemailId()
                                prof = Professor(None,email,None,None)
                                adminuser.professor_details('Professor.csv',prof)    
                            elif pInput =='8':
                                print('Professor name, rank and course id can be changed!!')
                                adminuser.modify_professor_details('Professor.csv')     
                            
                            elif pInput == '9':
                                userinput =input('enter \'professor\' or \'student\' whom to sort :: ')  
                                filename = 'Student.csv' if userinput.lower() =='student' else 'Professor.csv'
                                adminuser.sortRecords(userinput,filename)  
                            elif pInput =='10':
                                courseId = getcourseId()
                                adminuser.getMean(courseId)
                            elif pInput =='11' :
                                courseId = getcourseId()
                                adminuser.getMedian(courseId)
                            elif pInput == '12':
                                credits,courseName = getcoursedetails() 
                                course = Course(credits,courseName)
                                adminuser.add_new_course('Course.csv',course) 
                            elif pInput == '13':
                                courseId = getcourseId()
                                adminuser.delete_course('Course.csv',courseId)
                            elif pInput =='14':
                                cours_id =input('Enter the course id :: ')
                                creds = input('enter the course modified credits  :: ')
                                coursName = input('enter the coursename  modified :: ')
                                course = Course(cours_id,creds,coursName)
                                adminuser.modifycourse('Course.csv', course) 
                            elif pInput == '15':
                                adminuser.display_Allcourses('Course.csv')  
                            elif pInput =='16':
                                adminuser.display_grades_report('Student.csv')          
                            elif pInput == '17':
                                loggout= LoginUser(loginEmail,loginpass,None)
                                loggout.logout() 
                            else:
                                print('wrong input !!')
                                break                        
                    elif type == 'professor' :
                        prof = Professor(None,loginEmail,None,None)
                        while True:
                            print("************WELCOME PROFESSOR****************")
                            print('1. Update Student Records')
                            print('2. Add grade to a student')
                            print('3. Modify grade of a student')
                            print('4. Delete grade to a student')
                            print('5. Logout')
                            print("****************************")
                            pInput = input('Select your choice :: ')

                            if pInput == '1':
                                email = input('enter the email of the student :: ')
                                courseid = input('enter the course if for which you want to make changes :: ')
                                grade = input('Enter the new grade :: ')
                                marks = input('enter the new marks :: ')
                                student = Student(None,None,email,courseid)
                                prof.update_student_records('Student.csv',student,grade,marks)        
                            elif pInput =='2':
                                prof.add_grade('Student.csv')
                            elif pInput == '3':     
                                prof.modifyGrades('Student.csv') 
                            elif pInput == '4':     
                                prof.deletegrade('Student.csv')      
                            elif pInput == '5':
                                loggout= LoginUser(loginEmail,loginpass,None) 
                                loggout.logout() 
                            else :
                                print('wrong input!!')
                                break         
                    elif type =='student':
                        student = Student(None,None,loginEmail,None)
                        while True:
                            print("*********WELCOME STUDENT*******************")
                            print('1. Check Grades')
                            print('2. Check Marks')
                            print('3. Logout')
                            print("****************************")
                            sInput = input('select your choice :: ')
                            if sInput =='1' :
                                student.check_my_grades('Student.csv')
                            elif sInput == '2' :
                                 student.check_my_marks('Student.csv')  
                            elif sInput =='3' :
                                loggout= LoginUser(loginEmail,loginpass,None)
                                loggout.logout()  
                            else:
                                print('wrong input !!!')
                                break            
        elif loginorSignup == '2':
            email,password,role = getNewUserDetails()
            signup = LoginUser(email,password,role)
            signup.signup()

        elif loginorSignup == '3' :
            email,currentpassword = getdetailsToCP() 
            log = LoginUser(email,currentpassword,None)
            log.change_password()   
        else :
            print('wrong input selection. Program ended.') 
            with open('LoginDB.csv','w') as file1:
                pass
            with open('passwordKey.csv','w') as file1:
                pass
            exit() 

def getcourseInfo():
    print('Only credits and courseName can be edited !!')
    course_id = input('enter course_id ::: ')
    credits = input('Enter new credits for the course :: ')
    courseName = input('Enter the new courseName ::: ')
    return course_id,credits,courseName
def getcoursedetails():
     credits =input('Enter the credits for this course :: ')
     courseName = input('enter the course name :: ')
     return credits,courseName               

def getdetailsToCP():
    email = input('Enter your email address :: ')
    currentpassword = input('Enter your current password')
    return email,currentpassword    

def fileExists(filename):
    file_exists = os.path.isfile(filename) and os.path.getsize(filename) > 0
    return file_exists
def getpemailId():
    email = input('Enter professor email :: ')
    return email
def getcourseId():
    courseid = input('Provide the course id ::')
    return courseid

def getNewUserDetails():
    fname = input('Enter your first name :: ')
    lname = input('Enter your last name :: ')
    useremail =input('Enter your email address :: ')
    password = input('Enter the password :: ')
    role = input('Enter your role : Professor or Student or Admin:: ')
    return useremail,password,role
def getProfInfo():
    name = input('Enter the professor name :: ')
    email = input('Enter the email address :: ')
    rank =input('Enter the rank of the professor :: ')
    courseid = input('Enter the courseId he will teach :: ')
    return name,email,rank,courseid

def getStudentInfo():
    fname = input('Enter student first name :: ')
    lname = input('Enter studentlast name :: ')
    email = input('Enter student email :: ')
    courseId = input('Enter student courseid :: ')
    return fname,lname,email,courseId

def getStudentEmail():
    email = input('enter the email address of the student :: ')
    return email



def getId():
    userinput = input('Enter the Id(studentId/ProfessorId) :: ')
    return userinput
    
if __name__ == "__main__":
    mainmethod()

