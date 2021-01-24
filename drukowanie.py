import  copy
import os
import pprint

def egg(parameter):
    parameter.append("Hello")
    #return parameter

spam=[25,26,98]
print(id(spam))
print("kopiowanie ")
r=copy.copy(spam)
print(r)
print(id(r))

egg(spam)
print(spam)

er=spam
print(er)
er.append("Nowy string")
print(er)
print(spam)

print(r)
print(id(r))
#name=input("name - ")
#print(f"Maciej jest najlepszym przyjacielem {name}")

def dict():
    dict1={"Maciej":"8 listopad", "Magda":"15 pazdziernik", "Olek":"5 czerwiec"}
    print(dict1)
    dict1["Klaudia"]="11 czerwiec"
    e=dict1["Maciej"]
    print(e)
    while True:
        name=input("Wprowadz imie - ")
        if name ==" ":
         break
        if name in dict1:
            print(dict1[name] + "is the birthday of " + name)
        else:
            print("Nie mam jej w bazie to " + name)
            print("kiedy sa jej urodziny")
            bday=input(" podaj ta date - ")
            dict1[name]=bday
            print("Birthdate database update")

#dict()

def slowIter():
    dict = {"Maciej": "8 listopad", "Magda": "15 pazdziernik", "Olek": "5 czerwiec"}
    print(dict)
    for i,j in dict.items():
            print("{} have value {}".format(i,j))
slowIter()

character="My name ist Matthias. Ich wohne in Vien in Östereich"
count={}
for litery in character:
    count.setdefault(litery,0)
    count[litery]=count[litery]+1
print(pprint.pformat(count))

def drukow():
    file_path=("C:\\Users\\mltea\\OneDrive\\Pulpit\\sortiment.txt")    # DRUKOWANIE
    os.startfile(file_path,"print")
    file_path1=("C:\\Users\\mltea\\OneDrive\\Pulpit\\nowik.xlsx")
    os.startfile(file_path1,"print")
#drukow()
