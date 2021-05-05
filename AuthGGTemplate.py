import os
import requests
import time
import getpass
import platform
import discord
from AuthGG.client import Client
from AuthGG.admin import AdminClient

GetOS = platform.system()
GetOSVer = platform.release()
AllOS = GetOS + " " + GetOSVer

client = Client(api_key="yourapikey", aid="youraid", application_secret="youapplicationsecret")

lcre = """
YOUR
LOGO
"""

OptionList = """
1. Login
2. Register
3. Forgot Password
4. Admin Pannel

Pick Your Option: """

def LoginPage():
    LoiginUsername = input("Username: ")
    LoginPassword = input("Password: ")

    try:
        client.login(username=LoiginUsername, password=LoginPassword)
        DiscordWebhook = "webhookgoeshere"
        logembed = {
            "title": "Login Detected",
            "description": LoiginUsername + " Has Logged In",
            "color": "14177041"
        }

        logdata = {
            "username": "Login Bot",
            "embeds": [
                logembed
            ],
        }

        requests.post(DiscordWebhook, json=logdata)
        print("You Are Logged In As " + LoiginUsername)
        # RUN CODE HERE LOL
    except Exception as cheese:
        print(cheese)


def RegisterPage():
    RegisterEmail = input("Email: ")
    RegisterLicenseKey = input("License Key: ")
    RegisterUsername = input("Username: ")
    RegisterPassword = input("Password: ")

    try:
        client.register(email=RegisterEmail, username=RegisterUsername, password=RegisterPassword, license_key=RegisterLicenseKey)
        print("Registerd " + RegisterUsername)
        Webhook = "yourwebhook"
        regdata = {
            "username": "webhookusername",
            "content": RegisterUsername + " Has Registered On " + AllOS 
        }
        requests.post(Webhook, json=regdata)
    except Exception as Cheese2:
        print(Cheese2)


def ResetPassword():
    username = input("Your Username: ")
    
    try:
        client.forgotPassword(username=username)
    except Exception as Cheese3:
        print(Cheese3)


def ResetUserHWID():
    try:
        AdminKey = input("PLEASE ENTER YOUR ADMIN KEY IN ")
        AdminClientKey = AdminClient(AdminKey)
        usernameHWID = input("WHICH USERS HWID DO YOU WANT TO RESET: ")
        AdminClientKey.resetHWID(username=usernameHWID)
        AdminPage()
    except Exception as HWIDErr:
        print(HWIDErr)


def ChangeUsersPassword():
    try:
        AdminKey = input("PLEASE ENTER YOUR ADMIN KEY IN ")
        AdminClientKey = AdminClient(AdminKey)
        resetusername = input("What Users ")
        resetpassword = input("New password ")
        AdminClientKey.changeUserPassword(username=resetusername, password=resetpassword)
        print("Reset " + resetusername + " With The Password " + resetpassword)
        AdminPage()
    except Exception as Cheese5:
        print(Cheese5)


def GetUserHWID():
    try:
        AdminKey = input("PLEASE ENTER YOUR ADMIN KEY IN ")
        AdminClientKey = AdminClient(AdminKey)
        username = input("Which Users HWID Would You Like To Get ")
        AdminClientKey.getHWID(username=username)
        AdminPage()
    except Exception as Cheese6:
        print(Cheese6)


def DeleteUser():
    try:
        AdminKey = input("PLEASE ENTER YOUR ADMIN KEY IN ")
        AdminClientKey = AdminClient(AdminKey)
        username = input("Who are you deleting ")
        AdminClientKey.deleteUser(username=username)
        print("Deleted " + username)
        AdminPage()
    except Exception as Cheese7:
        print(Cheese7)
    

def AdminPage():
    try:
        AdminClientKey = input("Admin Key ")
        AdminKey = AdminClient(AdminClientKey)
        Users = AdminKey.getUserCount()
        print("Welcome " + Users + "Are Registerd")
    except Exception as Cheese4:
        print(Cheese4)
        os.sys.exit(0)


    
    OptionsListAdmin = """
    1. Reset A Users HWID
    2. Change A Users Password
    3. Get A User HWID
    4. Delete Users

    Pick Your Option: """
    Options = input(OptionsListAdmin)

    if Options == "1":
        ResetUserHWID()
    elif Options == "2":
        ChangeUsersPassword()
    elif Options == "3":
        GetUserHWID()
    elif Options == "4":
        DeleteUser()
    else:
        print("INVALID OPTION")
        time.sleep(2)
        os.system("cls")
        AdminPage()



def ChooseOption():

    print(lcre)
    Option = input(OptionList)

    if Option == "1":
        LoginPage()
    elif Option == "2":
        RegisterPage()
    elif Option == "3":
        ResetPassword()
    elif Option == "4":
        AdminPage()
    else:
        print("Invalid Option")
        time.sleep(2)
        os.system("cls")
        ChooseOption()


def lol():
    User = getpass.getuser()
    print("Welcome " + User)
    print(lcre)
    print("Coded By The Bezopasnyy")
    time.sleep(3)
    os.system("cls")
    ChooseOption()

if GetOS == "Windows":
    lol()
else:
    print("YOUR OS IS NOT SUPPORTED SORRY")
    os.sys.exit(0)
