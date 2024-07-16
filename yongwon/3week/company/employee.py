class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay
    
    def get_details(self):
        print(f"{self.name} : {self.age}")
    
    def raise_pay(self, factor):
        self.pay*=factor
        print(f"{self.name}의 인상된 연봉은 {self.pay}입니다")