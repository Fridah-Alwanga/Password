import random
import string

class User:

    user_list =[]

    def __init__(self, user_name,password):
      self.user_name =user_name
      self.password =password

    def save_user(self):
            User.user_list.append (self)
            
    @classmethod
    def user_exist(cls,user_name,password):
        current_user =""
        for user in User.user_list:
            if user.user_name ==user_name and user.password ==password:
                current_user =user.user_name
                return current_user
         
class Credetials:

    user_credetials =[]

    def __init__(self,acc_name, user_name,password):
      self.acc_name =acc_name
      self.user_name =user_name
      self.password =password

    def save_credetials(self):
            Credetials.user_credetials.append (self)

            
    # def delete_credentials(self):
    #         Credetials.user_credetials.remove(self)

    @classmethod
    def credetialsuser_exist(cls,acc_name):
        for credetial in cls.user_credetials:
            if credetial.acc_name ==acc_name:
                return True
        return False

    @classmethod
    def find_acc_name(cls,acc_name):
        for credetial in cls.user_credetials:
            if credetial.acc_name ==acc_name:
                return credetial
    @classmethod
    def display_credentials(cls):
        return cls.user_credetials
 
    def generate_password (self,stringfri=1):
                 password =string.ascii_uppercase + string.ascii_lowercase + string.digits + "(/|~!.@,)#{?&[%]^}&*"
                 return "".join(random.choice(password) for i in range(stringfri))
                    
