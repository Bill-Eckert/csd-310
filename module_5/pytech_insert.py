"""William Eckert
Cybr 350
Student Insertion
"""

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.uat4t1h.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
kaladin = {
    "student_id": "1007",
    "first_name":"Kaladin",
    "last_name:": "Stormblessed"
   
}

dalinar = {
    "student_id": "1008",
    "first_name": "Dalinar",
    "last_name" : "Kholin"
}

shallan = {
    "student_id" : "1009",
    "first_name" : "Shallan",
    "last_name" : "Davar"
}

students = db.students

print("\n --INSERT STATEMENTS --")
kaladin_student_id = students.insert_one(kaladin).inserted_id
print ("Inserted record Kaladin Stormblessed into the students collection with document_id" + str(kaladin_student_id))

dalinar_student_id = students.insert_one(dalinar).inserted_id
print ("Inserted record Kaladin Stormblessed into the students collection with document_id" + str(dalinar_student_id))

shallan_student_id = students.insert_one(shallan).inserted_id
print ("Inserted record Kaladin Stormblessed into the students collection with document_id" + str(shallan_student_id))

input("\n End of program. press any button to exit")