# multiple inheritance
class ineuron:

    def student(self):
        print("this will give student info")

    def student_info(self):
        print("this will give students education info")

    def test(self):
        print("this test method from ineuron")

class dashboard(ineuron):

    def __init__(self,course,product,company):
        self.course = course
        self.product = product
        self.company = company

    def managment(self):
        print("information about managment")

class job(dashboard,ineuron):
    pass

obj = job('java','xyz','oneneuron')
obj.student_info()
obj.student()
obj.managment()
print(obj.company)
