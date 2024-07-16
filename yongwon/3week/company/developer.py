from .employee import Employee

class Developer(Employee):
    def __init__(self,name, age, pay, skills, marriage):
        super().__init__(name, age, pay)
        self.skills = skills
        self.marriage = marriage #Attribute : 속성
    def get_details(self):
        super().get_details()
        print(f"{self.name}의 특기는 {self.skills}이고 {self.marriage}입니다!")
