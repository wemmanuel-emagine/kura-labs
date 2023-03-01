# Hi Guys. Good night again. Like I mentioned, I'm in another meeting now.
# Our main task today is the script to create accounts in the Organisation.
# We then need the script to create an EC2 inside the new account.
# Other tasks will be in the main account, to set up an Elastic Beanstalk for a PHP application and connect this to an Amazon Aurora MySQL Database.

# Basic command to create an organization member account
import subprocess

# Inputing the email and the account name

def CreateAWSUser():
    email = input("Please enter students email: ")
    accName = input("Please enter student account name: ")

    # Creating User Account
    subprocess.run(['aws', 'organizations', 'create-account', '--email', email, '--account-name', accName])

def addUserCli():
    # Entering Student Information
    role_arn = input("Please enter the students ARN Role: ")
    role_identifier = input("Please enter the students Identifer in: ")
    source_profile = "default"

    # Writing to ~/.aws/credentials
    credentails = open("~/.aws/credentials","a")
    credentails.write(f"[{role_identifier}]\n") 
    credentails.write(f"role_arn = {role_arn}\n")
    credentails.write(f"source_profile = {source_profile}\n\n\n")
    credentails.close()
   

def switchUser():
    # To get current profile configured to the cli
    subprocess.run(["aws","sts","get-caller-identity"])

    # To switch to student user
    student_role_identifier = input("Please enter the account Identifer")
    subprocess.run(["aws","sts","get-caller-identity","--profile",student_role_identifier])


