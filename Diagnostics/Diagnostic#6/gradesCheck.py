
learnerGrades = open("grades.txt","r")
passGrade = open("pass.txt","w")
failGrade = open("fail.txt","w")

for line in learnerGrades:
 line_split = line.split()
 if line_split[2] == 'fail':
    failGrade.write(line)
 else:
    passGrade.write(line)


learnerGrades.close()
