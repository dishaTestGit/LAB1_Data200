import unittest
from LabAssignment import Student, Admin,Professor, Course
import csv
import time
import os
class TestStudent(unittest.TestCase):
    filename ='DummyStudent.csv'
    filename1 ='DummyProfessor.csv'
    filename2 ='DummyCourse.csv'
    @classmethod
    def tearDownClass(cls):
        """Delete the test file after all tests are completed."""
        
        if os.path.exists(cls.filename):
            os.remove(cls.filename)
        if os.path.exists(cls.filename1):    
            os.remove(cls.filename1)
        if os.path.exists(cls.filename2):    
            os.remove(cls.filename2)

        print(f"File {cls.filename},{cls.filename1},{cls.filename2} deleted after test execution.")
    # add, delete,modify,search,sort students    
    def test_100studentsinsertion(self):
        totalstuds =[]
        studentsinFile =[]
        studentsinFileAfterdel =[]
        filename ='DummyStudent.csv'
        adminuser = Admin()
        start_time = time.time()
        for i in range(1000):
            email = f'dr{i}@gmail.com'
            student = Student('Disha','Rawat',email,'data200')
            std = adminuser.add_new_student(filename,student)
            totalstuds.append(std)
        end_time =time.time()
        print('total time for adding 1000 students:: ',end_time - start_time)
        with open(filename,'r') as file2:
            reader = csv.reader(file2)
            for idx,val in enumerate(reader):
                studentsinFile.append(val)

        student1 = Student('Disha','Rawat','dr23@gmail.com','data200')
        start_time1 = time.time()
        adminuser.delete_new_students(filename,'dr23@gmail.com')
        end_time1 = time.time()
        print('total time for deleteing 1 students:: ',end_time1 -start_time1)
        start_time2 = time.time()
        adminuser.sortRecords('student',filename)
        end_time2 = time.time()
        print('Time taken to sort the students records ::: ',end_time2 -start_time2)
        
        with open(filename,'r') as file2:
            reader = csv.reader(file2)
            for idx,val in enumerate(reader):
                studentsinFileAfterdel.append(idx)

        self.assertEqual(len(studentsinFile), 1001)# including header        
        self.assertEqual(len(studentsinFileAfterdel), 1000)
        
    # add, delete professor
    def test_professorinsertion(self):
        totalstuds =[]
        professorinfile =set()
        profinFileAfterdel =set()
        proflist =[]
        ffilename1 ='DummyProfessor.csv'
        filename ='DummyStudent.csv'
        adminuser = Admin()
        start_time = time.time()
        for i in range(100):
            email = f'prof{i}@gmail.com'
            course = f'data20{i}'
            course_id =f'1{i}'
            prof = Professor('TestPtof',email,course,course_id)
            pr = adminuser.add_new_professor(ffilename1,prof)
            totalstuds.append(pr)
        end_time =time.time()
        print('total time for adding 100 prof:: ',end_time - start_time)
        with open(ffilename1,'r') as file2:
            reader = csv.reader(file2)
            for idx,val in enumerate(reader):
                professorinfile.add(idx)
                if idx ==12:
                    proflist.append(val)

        prof1 = Professor('TestPtof','prof23@gmail.com','data223','123')
        start_time1 = time.time()
        adminuser.delete_professor(ffilename1,'prof23@gmail.com')
        end_time1 = time.time()
        with open(ffilename1,'r') as file2:
            reader = csv.reader(file2)
            for idx,val in enumerate(reader):
                profinFileAfterdel.add(idx)
        print('total time for deleteing 1 professor:: ',end_time1 -start_time1)
        student2 = Student('Disha','Rawat','dr24@gmail.com','data200')
        marks ='98.5'
        grade ='A'
        start_time3 = time.time()
        prof = Professor('TestPtof','prof24@gmail.com','data223','124')
        prof.update_student_records(filename,student2,grade,marks)
        end_time3 = time.time()
        self.assertEqual(float(marks),98.5)
        print('Time taken to update the students records ::: ',end_time3 -start_time3)

        self.assertEqual(len(professorinfile), 101)# including header        
        self.assertEqual(len(profinFileAfterdel), 100)

    # add, delete course
    def test_courseinsertion(self):
        totalcourse =[]
        courseinfile =set()
        courinFileAfterdel =set()
        courselist =[]
        ffilename2 ='DummyCourse.csv'
        adminuser = Admin()
        start_time = time.time()
        for i in range(10):
            credits = '3'
            courseName = f'Python{i}'
            cou1 = Course(credits,courseName)
            adminuser.add_new_course(ffilename2,cou1)
        end_time =time.time()
        print('total time for adding 10 courses :: ',end_time - start_time)
        with open(ffilename2,'r') as file2:
            reader = csv.reader(file2)
            for idx,val in enumerate(reader):
                courseinfile.add(idx)

        start_time1 = time.time()
        adminuser.delete_course(ffilename2,'C10')
        end_time1 = time.time()
        with open(ffilename2,'r') as file2:
            reader = csv.reader(file2)
            for idx,val in enumerate(reader):
                courinFileAfterdel.add(idx)
        print('total time for deleteing 1 course:: ',end_time1 -start_time1)

        c2 = Course('3','Python1')
        start_time2 = time.time()
        adminuser.modifycourse(ffilename2,c2)
        end_time2 = time.time()
        print('total time for modifying 1 course:: ',end_time2 -start_time2)
        self.assertEqual(len(courseinfile), 11)# including header        
        self.assertEqual(len(courinFileAfterdel), 10)    
        
if __name__ == "__main__":
    unittest.main()
    