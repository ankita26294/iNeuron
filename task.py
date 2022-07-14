# single inheritance
class ineuron:

    def __init__(self,courses,blogs,jobs):
        self.courses = courses
        self.blogs = blogs
        self.jobs = jobs

    def internship(self):
        print("ineuron internship information")

obj = ineuron('datascience','xyz','datascientist')
print(obj)

class dashboard(ineuron):
    print("all detail information avilable from dashboard")

d = dashboard('data analysis','abc','data analyst')
print(d)
print(d.internship())
print(d.jobs)
print(d.blogs )
print(d.courses)
