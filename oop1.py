# class BankApp: 
#     pass

# my_object = BankApp()

class School:
    def __init__(self, teacher, student):
        self.teacher = teacher
        self.student = student

    def teachers(self):
        return f'{self.teacher} is teacher'
    
    def students(self):
        return f'{self.student} is student'
    

melody = School('Miss Cynthia', 'Melody')
print(melody.teachers())
print(melody.students())

investor = School('Miss Cynthia', 'Investor')
print(investor.teachers())
print(investor.students())