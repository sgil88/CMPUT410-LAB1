class Student:
    courseMarks = {}
    name = ""
    def __init__(self, name, family):
        self.courseMarks = {}
        self.name = name
    
    def addCourseMarks(self, course, mark):
        self.courseMarks[course] = mark;
        
    def average(self):
        if len(self.courseMarks) > 0:
            sum = 0
            for course, mark in self.courseMarks.iteritems():
                sum += mark
                return sum / len(self.courseMarks)
        return 0