# 繼承
# 開頭要大寫
# 父
class Member:
    def __init__(self, new_gender, new_major, new_id):
        self.__gender = new_gender
        self.major = new_major
        self.id = new_id

    def get_gender(self):
        return self.__gender

    def set_gender(self, new_gender):
        if new_gender == 'M' or new_gender == 'F':
            self.__gender = new_gender
        else:
            print('=====請傳入"M"或"F"====')

    def borrow_resources(self):
        pass

    def check_auth(self):
        pass


# 繼承
# 子
class Student(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def borrow_resources(self):
        print('student borrow')


def join_class(self):
    pass


def quit_class(self):
    pass


# 多型
# 父
class Member:
    def __init__(self, new_gender, new_major, new_id):
        self.__gender = new_gender
        self.major = new_major
        self.id = new_id

    def borrow_resources(self):
        pass


# 子
class Student(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def borrow_resources(self):
        print('student borrow')


class Professor(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def borrow_resources(self):
        print('student borrow')


student1 = Student('M', '工管系', 'D0239867')
student2 = Student('F', '多媒系', 'D0239874')
professor1 = Professor('F', '經濟系', 'T0239867')
professor2 = Professor('M', '經濟系', 'T0239829')

Is = [student1, student2, professor1, professor2]
for item in Is:
    item.borrow_resources()

#     def get_gender(self):
#         """回傳private屬性"""
#         return self.__gender
# #set搭配get讓使用者不能直接取值,比較不會出錯
#
#     def set_gender(self, new_gender):
#          if new_gender == 'M' or new_gender == 'F':
#              self.__gender = new_gender
#          else:
#              print('=====請傳入"M"或"F"====')
#
# #每個類別的每個方法都要有self,因為python跑的方式是:studentA.join_class(studentA)
# #會把自己傳入括號裡,所以每個方法都要self,才能使用studentA.join_class()
#     def join_class(self):
#         pass
#     def quit_class(self):
#         pass
#
# #取出資料
# studentA = Student('M', '工管系', 'M10821000')
# #studentA.set__gender('dog')
# #print(studentA.gender)
# print(StudentA.get_gender())


print('123456')
