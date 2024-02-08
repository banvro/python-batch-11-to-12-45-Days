# OOPs:
#     Inheritance:
#         1) Single level inheritance
#             1 chile have one parent
#         2) Multiple Inheritance
#             1 child have multiple parents
        
#         3) Multilevel Inheritance:
            
# class saveuserdata:
#     def _init_(self, a, b, c):
#         self.name = a
#         self.age = b
#         self.number = c
    
#     def savedata(self):
#         print(f"""
#         user name is : {self.name}
#         user age is : {self.age}
#         user number is : {self.number}
#         """)

# obj = saveuserdata("hlo", 20, 982646234)
# obj.savedata()

# obj1 = saveuserdata("ok", 22, 982646234)
# obj1.savedata()

# obj2 = saveuserdata("no", 23, 982646234)
# obj2.savedata()


# class newusersavedata(saveuserdata):
#     def _init_(self, a, b, c, d):
#         super()._init_(a, b, c)
#         self.addres = d
    
#     def savedata(self):
#         print(f"""
#         user name is : {self.name}
#         user age is : {self.age}
#         user number is : {self.number}
#         user adress is : {self.addres}
#         """)

# obj3 = newusersavedata("go", 20, 98236498, "this is address")
# obj3.savedata()
    
    
    
# 4) Hirirachical Inheritance:
    # 1 parent have multple child
    
# class cls1:
#     def mthd1(self):
#         print("this is method 1")
    
#     def mthd2(self):
#         print("this ismethod 2")

# class cls2(cls1):
#     def mthd3(self):
#         print("this is method 3")

# class cls3(cls1):
#     def mthd4(self):
#         print("this is method 4")

# obj = cls3()
# obj.mthd3()
    
# 2) Hybrid Inheritance:
#     combination of tow or mre then two inheritance
    # herirachical + multiple
class cls1:
    def mthd1(self):
        print("this is metjod 1")

    def mthd2(self):
        print("this is method 2")

class cls2(cls1):
    def mthd3(self):
        print("this is metod 3")

class cls3(cls1):
    def mthd4(self):
        print("this is method 4")

class cls4(cls2, cls3):
    def mthd5(self):
        print("ths is meothod 4")

obj = cls4()
obj.mthd1()



# Abstraction
