"""Title: pytech_delete.py
   Author: William Eckert
   Date:7/8/2023
   Descrption: Program for inserting and deleting a document in the collection
   
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

# creating the test document 
test_document = {
    "student_id": "1010",
    "first_name": "Adolin",
    "last_name": "Kholin"
}

# inserting the test document into MongoDB atlas 
test_document_id = students.insert_one(test_document).inserted_id

# inserting statements with output 
print("\n  -- insert statement --")
print("  Inserted student record into the students collection with document_id " + str(test_document_id))

# calls the find_one() method of student_id 1010
student_test_document = students.find_one({"student_id": "1010"})

# displaying the results 
print("\n  -- Displaying the doc  -- ")
print("  Student ID: " + student_test_document["student_id"] + "\n  First Name: " + student_test_document["first_name"] + "\n  Last Name: " + student_test_document["last_name"] + "\n")

# call the delete_one method to remove the student_test_doc
deleted_student_test_document = students.delete_one({"student_id": "1010"})

# find all students in the collection 
new_student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")