# multilevel inheritance
class ineuron:

    def student(self):
        print("this will give student info")

    def student_info(self):
        print("this will give students education info")

class dashboard(ineuron):

    def __init__(self,course,product,company):
        self.course = course
        self.product = product
        self.company = company

class job(dashboard):
    pass

obj = job('java','xyz','oneneuron')
obj.student()
print(obj.product)
obj.student_info()
print(obj.company)
