class student:
    def get(self):
        self.en=input("Enter Enrollment ==")
        self.name=input("Enter name ==")
        self.dept=input("Enter department ==")
class display(student):
    def put(self):
        print("\nDetails of student are: ")
        print("Enrollment no: ",self.en)
        print("NAME==",self.name)
        print("DEPT==",self.dept)
ob=display()
ob.get()
ob.put()