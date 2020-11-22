#!user/bin/env/python3.9
# python3.9 run.py(how to run:)
from user import Credetials , User

def create_user(username,password):
    newuser = User(username,password)
    return newuser

def signin (username,password):
    userexist = User.user_exist(username,password)
    return userexist

def  save_user(user):
    user.save_user()

def create_credentials(acc_name,username,password):
    new_credentials = Credetials(acc_name,username,password)
    return new_credentials

def save_credentials(Credetials):
    Credetials.save_credentials()

def delete_credentials(Credetials):
    Credetials.delete_credentials()

def display_credetials():
    return Credetials.display_credentials()

def Credetialsuser_exist(acc_name):
    return Credetials.credetialsuser_exist(acc_name)

def find_acc_name(acc_name):
    return Credetials.find_acc_name(acc_name) 

def generate_password ():
    generate_password =Credetials.generate_password()
    return generate_password 

# def main():
#     while True:
#         print('login to password locker,use this command to procced use cr to create account, SG to sign in and EX to exit')
#         choice = input().lower()
#         if choice =='cr':
#             print("create account")
#             username =input("enter username")
#             print('use p to create password,au to auto generate password,and e for exit')
#             password =input().lower()
#             if password == "p":
#                 password = input("enter password")
#             elif password =="au":
#                     password=generate_password()
#             else:
#                 print("incorrect")
#                 save_user(create_user(username,password))
#                 print(f"Welcome {username} your locker  password is {password}")
#         elif choice =='sg':
#             print("enter username and password to signin")
#             print("enter username:")
#             username = input()
#             print("enter password:")
#             password = input()
#             exist_user =signin(username,password)
#             if exist_user == username:
#                 print(f"hie {username}")
#                 while True:
                    print("use C to creat credential,DEL to delet credential,DS to display F to find credential")
                    credentials_input == input().lower()
                    if credentials_input =="C":
                        print("create credentials")
                        input(" enter acc_name:")
                        acc_name= input()
                        print("enter username:")
                        username =input() 
                        print('use p to create password,au to auto generate password,and e for exit')
                        password =input().lower()
                        if password == input("p"):
                            password = input("enter password")
                        elif password =="g":
                                password=generate_password()

                        else:
                            print("incorrect")

                        save_credentials(create_credentials(acc_name,username,password))
                        print(f"your credentials are {acc_name},{username},{password} has been created")

                    elif credentials_input =="DEL":
                        print("enter account to delete")
                        account = input()
                        if find_acc_name(account):
                                account_to_delete = find_acc_name(account)
                                account_to_delete.delete_credentials()
                                print("account successfully delited")
                        else:
                            print("account does not exist")      

                    elif credentials_input =="DS":
                        print("your credentials are as the following")
                        if  display_credetials():
                            for account in display_credetials():
                                print(f"account: {account} \n username: {username} \n password: {password} \n")


                        else:
                            print("no credentials found")


                    elif credentials_input =="F":
                        print("enter account to find")
                        account = input("enter account name")
                        if find_acc_name(account):
                            account_name = find_acc_name(account)
                            print(f"account: {account} \n username: {username} \n password: {password} \n")  
                            
                    else:
                        print("exit")

        else:
            print("Goodbye")
if __name__ =="__main__":
    main()
 


   