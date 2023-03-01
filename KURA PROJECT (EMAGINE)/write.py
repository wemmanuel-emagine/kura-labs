f = open("creds.txt", "a")
f.write("\n \n[customer-project]\nrole_arn = arn:aws:iam::123456789012:role/your-project-role-name\nsource_profile = customer-login")
f.close()


