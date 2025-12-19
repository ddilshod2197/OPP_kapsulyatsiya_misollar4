class User:
    def __init__(self, username):
        self.username = username    
        self.__password = None      

    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
            print("Parol o‘rnatildi.")
        else:
            print("Parol kamida 8 ta belgidan iborat bo‘lishi kerak!")

    def check_password(self, input_password):
        return input_password == self.__password

    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.set_password(new_password)
        else:
            print("Eski parol noto‘g‘ri!")


user = User("admin")

user.set_password("12345")        # xato
user.set_password("password123")  # to‘g‘ri

print(user.check_password("password123"))
print(user.check_password("12345678"))

user.change_password("password123", "newpass123")
print(user.check_password("newpass123"))

