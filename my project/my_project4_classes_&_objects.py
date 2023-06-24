# create a class
from posixpath import supports_unicode_filenames
from types import new_class
from unicodedata import name
from post import Post


class User:
    def __init__(self, name, surname, age, email_adress, continent, nationality, job_tittle, religion, language, password):
        self.name = name  
        self.surname = surname
        self.age = age
        self.email_adress = email_adress
        self.continent =  continent
        self.nationality = nationality
        self.job_tittle = job_tittle
        self.religion = religion
        self.language = language
        self.password = password


    def update_email_adress(self, new_email_adress):
        self.email_adress = new_email_adress
        print(f"user {self.name} has changed his email to {new_email_adress}")

    def change_password(self, new_password):
        self.password = new_password
        print(f"user {self.name} has changed his email adress from {self.password} to {new_password}")

    def get_user_info(self):
        print(f" user {self.name} from {self.nationality} currently works as an {self.job_tittle} for 4 years, you can contact him via his email adress at {self.email_adress}")



current_user = User("AHMAD", "YAKUBU AHMAD", "25", "engrahmadaya@gmail.com", "Africa", "Nigeria", "Engineer", "Islam", "Hausa", "ahmad222")
current_user.get_user_info()
current_user.update_email_adress("ahmadyakubuaya@gmail.com")
current_user.get_user_info()
new_post = Post("I wish an evalasting and peaceful mooments for all my connections.....", current_user.name +' '+ current_user.surname)
new_post.get_post_info()