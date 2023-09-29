

print('')
print('')
print('Please enter the following information:')
print('')

first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email Address: ")
phone_no = input("Phone number: ")

# handle the job title
job_title = input("Job title: ")
aryJobTitles = job_title.split()
tempAry = []
for i in range(len(aryJobTitles)):
    tempAry.append(aryJobTitles[i].capitalize())
newJobTitle = " ".join(tempAry)

id_no = input("ID Number: ")

#hair color and eye color
hair_color = input("What is your hair color?  ")
eye_color = input("What is your eye color?  ")
# month and advanced training
month = input("Which month did you start, type the name of the month. ex : Jane.  ")
hasTrained = input("Have you completed advance training? Please answer Yes or No.  ")

divider = "-------------------------------------"
print("The ID Card is:")
print(divider)
print("%s, %s" % (last_name.upper(), first_name))
print(newJobTitle)
print("ID: %s" % id_no)
print("")
print(email.lower())
print(phone_no)
print("Hair: %s \t\t Eyes: %s" % (hair_color, eye_color))
print("Month: %s \t Training: %s" % (month, hasTrained))
print(divider)
