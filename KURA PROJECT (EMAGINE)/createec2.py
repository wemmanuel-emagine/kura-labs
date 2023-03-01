import os

def createEC2():
    ans = input("Dou you want to create a Test EC2? (y/n):")

    if ans == "y":
        os.system("cd","Terraform")
        os.system("Terraform init")
        os.system("Terraform plan")
        os.system("Terraform apply -auto-approve")
    else:
        breakpoint


def destroyEC2():
    ans = input("Dou you want to destroy the Test EC2? (y/n):")

    if ans == "y":
        path = os.getcwd() 
        if path  != "Terraform":
            os.system("cd Terraform")
            os.system("Terraform destroy -force")
        else:
            os.system("cd Terraform")
            os.system("Terraform destroy -force")
    else:
        breakpoint
