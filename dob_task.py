'''
This program reads the data from a text file and seperates the name and
the dates of each person in the file into seperate sections.
'''
content = []
list_of_people = []      
names_of_people =[]
dates_of_people = []

with open("DOB.txt","r+") as file:
  '''
  This code will take the name and dates of each person from one
  list and seperate those values to two seperate lists. 
  '''
  content = file.readlines()
  for item in content:
    list_of_people.append(item.split())
  for person in list_of_people:
    name_of_person = " ".join([person[0], person[1]])
    date_of_person = " ".join([person[2], person[3], person[4]])
    names_of_people.append(name_of_person)
    dates_of_people.append(date_of_person)

  print("Name")
  for name in names_of_people:
    print(name)
  print("\n")
  print("Birthdate")
  for date in dates_of_people:
    print(date)


        
        
 