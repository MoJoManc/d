firstnames=[]
lastnames=[]
ages=[]
genders=[]
races=[]
raceoptions=['White','African-American','Asian','American-indian','Other']

def getFirstName():
    firstname=input("Enter firstname contains only letters: ")
    while True:
        if firstname.isalpha():
            break
        else:
            print("Please enter valid one :")
            firstname=input("Enter firstname contains only letters: ")
    return firstname

def getLastName():
    lastname=input("Enter lastname contains only letters: ")
    while True:
        if lastname.isalpha():
            break
        else:
            print("Please enter valid one :")
            lastname=input("Enter lastname contains only letters: ")
    return lastname

def getAge():
    age=input("Enter age: ")
    while True:
        try:
            if int(age)>0:
                break
            else:
                print("Please enter valid one :")
                age=input("Enter age: ")
        except Exception:
            print("Please enter valid one :")
            age=input("Enter age: ")
    return age

def getGender():
    gender=input("Enter gender (Male/Female): ")
    while True:
        if gender=="Male" or gender=="Female":
            break
        else:
            print("Please enter valid one :")
            gender=input("Enter gender (Male/Female): ")
            return gender
def getRace():
    race=input("Enter race (White/African-American/Asian/American-indian/Other): ")
    while True:
        if race in raceoptions:
            break
        else:
            print("Please enter valid one :")
            race=input("Enter race (White/African-American/Asian/American-indian/Other): ")
            return race
n=input("Enter number of patients: ")
while True:
    try:
        if int(n)>0:
            break
        else:
            print("Please enter valid one :")
            n=input("Enter number of patients: ")
    except Exception:
        print("Please enter valid one :")
        n=input("Enter number of patients: ")
i=0
while i<int(n):
    firstnames.append(getFirstName())
    lastnames.append(getLastName())
    ages.append(getAge())
    genders.append(getGender())
    races.append(getRace())
    exit=input("Type Exit to finish entering patient information: ")
    while True:
        if exit=="Exit":
           break
        else:
            print("Please enter valid one :")
            exit=input("Type Exit to finish entering patient information: ")

    i=i+1
print("patients report")
print("firstname"+" "+"lastname"+" "+"age"+" "+"gender"+" "+"race")
for firstname,lastname,age,gender,race in zip(firstnames,lastnames,ages,genders,races):
    print(f'{firstnames[i]}' + "lastnames"+  "age"+ "genders"+ "races")


