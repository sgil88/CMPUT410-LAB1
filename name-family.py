class Student:
    courseMarks = {}
    name = ""
    def __init__(self, name, family):
        self.courseMarks = {}
        self.name = name + " " + family
    
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark
        
    def average(self):
        if len(self.courseMarks) > 0:
            sum = 0
            for course, mark in self.courseMarks.iteritems():
                sum += mark
            
            print(self.name + " has an average of " + str(sum / len(self.courseMarks)))
            return sum / len(self.courseMarks)
        print(self.name + " has no courses.")
    
s1 = Student("John", "Baker")
s1.addCourseMark("c401", 44)
s1.addCourseMark("c307", 88)
s1.average()
