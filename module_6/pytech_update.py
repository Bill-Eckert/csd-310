"""Title: pytech_update.py
   Author: William Eckert
   Date:7/8/2023
   Descrption: Program for updating a document in the collection
   
"""
""" importing the statements"""
from pymongo import MongoClient

# Connection String
url = "mongodb+srv://admin:admin@cluster0.uat4t1h.mongodb.net/pytech?retryWrites=true&w=majority"

#Connecting to the Cluster
client = MongoClient(url)

#Connect to the Database
db = client.pytech

#Get the students collection
students = db.students

#Find all the students in the collection
student_list = students.find({})

# display message
print("\n --Displaying students from find() query")

# looping over the collection and output the results
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Stormblesss, Radiant"}})

# find the updated student document 
kaladin = students.find_one({"student_id": "1007"})


# output the updated document to the terminal window
print("  Student ID: " + kaladin["student_id"] + "\n  First Name: " + kaladin["first_name"] + "\n  Last Name: " + kaladin["last_name"] + "\n")

# exit message 
input("\n End of program, press any key to exit...")



