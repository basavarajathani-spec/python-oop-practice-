# class Notification:
#     def __init__(self,message):
#         self.message = message
#     def send(self):
#         pass
# class EmailNotification(Notification):
#     def send(self):
#         return (f"Email:{self.message}")
# class SMSNotification(Notification):
#     def send(self):
#         return (f"sms:{self.message}")
# class PushNotification(Notification):
#     def send(self):
#         return (f"Push:{self.message}")

# email = EmailNotification("hello world")
# sms = SMSNotification("hello basu")
# push = PushNotification("hello siddu")
# notifications = [email, sms, push]
# for i in notifications:
#     print((i.send()))


# class Payment:
#     def __init__(self,amount,detail):
#         self.amount = amount
#         self.detail = detail
#     def pay(self):
#         pass
# class CrediteCard(Payment):
#     def pay(self):
#         return f"credite Card {self.detail}:  {self.amount}"
# class Upi(Payment):
#     def pay(self):
#         return f"upi {self.detail}  : {self.amount}"
# class Cash(Payment):
#     def pay(self):
#         return f"Cash {self.detail} : {self.amount}"
# cred = CrediteCard(5000,"123" )
# upi = Upi(500,"basu@upi")
# cash = Cash(600,"paid")
# payments = [cred,upi,cash]
# for i in payments:
#     print(i.pay())

# class Shape:
#     def __init__(self,redius):
#         self.redius = redius
        
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# class Circle(Shape):
#     def area(self):
#         return (22/7)*self.redius**2
# rect = Rectangle(10,5)
# circ = Circle(5)
# shapes = [rect,circ]
# for i in shapes:
#     print(i.area())

# class Product:
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#     def get_price(self):
#         return self.__price
#     def final_price(self):
#         pass
# class Physical(Product):
#     def final_price(self):
#         return self.get_price() + 100
# class Digital(Product):
#     def final_price(self):
#         return self.get_price()
# phy = Physical("Phone",200000)
# dig = Digital("PhythonEbook",500)

# l = [phy,dig]
# for i in l:
#     print(i.final_price())

# class LibraryItem:
#     def __init__(self,title):
#         self.__title = title
#     def get_title(self):
#         return self.__title
#     def get_info(Self):
#         pass
# class Book(LibraryItem):
#     def get_info(self):
#         return f"Book: {self.get_title()}"
# class Magazine(Book):
#     def get_info(self):
#         return f"Magazine: {self.get_title()}"
# class DVD(Magazine):
#     def get_info(self):
#         return f"DVD: {self.get_title()} "
# book = Book("Python Basics")
# magazine = Magazine("Tech Today")
# dvd = DVD("Inception")

# librry_itm = [book,magazine,dvd]
# for i in librry_itm:
#     print(i.get_info())


# import numpy as np
# lisyt = np.array([29.8,844,7756,56567.0,567567,576756,7667,76675657,6775])
# total = np.mean(lisyt)
# print(total)

# import numpy as np 
# pyhton_array = np.array([1,2,3,43,5,6])
# print(pyhton_array)
# import numpy as np 
# python_arr = np.array([1,2,3,4])
# print(type(python_arr))
# import time
# class Employee:
#     def __init__(self,name,empl_id,Department):
#         self.name = name
#         self.empl_id = empl_id
#         self.department = Department
# class Salary(Employee):
#     def __init__(self,name,empl_id,Department,basicsalary,HRA,DA,bonus):
#         super().__init__(name,empl_id,Department)
#         self.basicsalary = basicsalary
#         self.HRA = HRA
#         self.DA = DA
#         self.bonus = bonus
# class Calculate(Salary):
#     def __init__(self, name,empl_id,Department,basicsalary, HRA, DA, bonus):
#         super().__init__(name,empl_id,Department,basicsalary, HRA, DA, bonus)
        
#     def GrossSalary(self):
#         return (self.basicsalary + self.HRA + self.DA + self.bonus)
#     def Annualsalary(self):
#         monthly =  self.basicsalary + self.HRA + self.DA + self.bonus 
#         return monthly * 12
#     def HighestSalary(self):
#         high = (self.basicsalary , self.HRA , self.DA , self.bonus) 
#         return max(high)
#     def avgsalary(self):
#         gross =  (self.basicsalary , self.HRA , self.DA , self.bonus )
#         return sum(gross)/len(gross)

# details = Calculate(
#         input("Enter your name: "),int(input("Enter your empl_id: ")),input("Enter your department: "),int(input("Enter your basic salary : "))
#         ,int(input("Enter your HRA salary: ")),int(input("Enter your DA salary : ")),int(input("Enter bonus salary: "))
#     )
# while True:
#     print("==salary calaculation==")
#     print("====choicesss====")
#     print("1.gross salary \n2.annual salary \n3.Highest salary \n4.avarage salary \n5.exit")
#     choice = int(input("Enter your choice(1,2,3,4,5): "))
#     if choice == 1:
#         print(details.GrossSalary())
#     elif choice == 2:
#         print(details.Annualsalary())
#     elif choice == 3:
#         print(details.HighestSalary())
#     elif choice == 4:
#         print(details.avgsalary())
#     elif choice == 5:
#         print("THANK YOU FOR USING CALCULATION...")
#         time.sleep(2)
#         break
#     else:
#         print("invalid input Try again!")

# class Student:
#     def __init__(self,name,rol_num):
#         self.name = name
#         self.rol_num = rol_num
#         self.__marks = {}
#     def add_marks(self,subject,mark):
#         self.__marks[subject] = mark

#     def show_marks(self):
#         return (f"{self.name} ---{self.__marks}")
#     def cal_avg(self):
#         total = 0
#         for i in self.__marks.values():
#             total += i
#         return total / len(self.__marks)
#     def is_passed(self):
#         is_passed =  all(mar>=35 for sub,mar in self.__marks.items())
#         if is_passed == True:
#             return (f"{self.name} is passed")
#         else:
#             return (f"{self.name} is failed")
#     def grade(self):
#         s = self.cal_avg()
#         if s > 90 and s<100:
#             return ("A")
#         elif s>80 and s<100:
#             return ("B")
#         else:
#             return("C")
# class ReportCard:
#     @staticmethod
#     # TODO fix this
#     def generate(Student : Student):
#         print("==REPORT CARD OF THE STUDENET==  ")
#         print("---------details---------")
#         print(f"Name: {Student.name} \t Rollno: {Student.rol_num}")
#         print("------- MARKS---------")
#         print(f"{Student.show_marks()}")
#         print(f"{Student.name} got avg marks:{Student.cal_avg()}")
#         print(f"{Student.is_passed()}")
#         print(f"{Student.grade()}")
# b = Student("basu",18)
# b.add_marks("Biology",98)
# b.add_marks("maths",34)
# a = Student("akash",76)
# a.add_marks("Biology",98)
# a.add_marks("maths",64)

# ReportCard.generate(a)


class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance
    def deposite(self,amount):
        if amount > 0 :
            self.__balance += amount
            return (f"current balance = {self.__balance}")
        return "Invalid deposite"
    def withdraw(self,amount):
        if amount > 0 and amount < self.__balance :
            self.__balance -= amount
            return (f"withdraw succesfull : current balance{self.__balance}")
        return "Invalid transaction"
    def get_balance(self):
        return self.__balance
account = BankAccount("Basu", 1000)
account.deposite(500)
(account.withdraw(200))
print(account.get_balance())