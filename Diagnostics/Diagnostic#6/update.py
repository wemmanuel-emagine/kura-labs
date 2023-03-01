import os

command1 = "sudo apt -y update >> updateLog.txt" 
command2 = "sudo apt -y upgrade >> updateLog.txt"

os.system(command1)
ans = input("Do you want to apply the upgrade to your machine (yes/no): ")

if ans == "yes":
    os.system(command2)

