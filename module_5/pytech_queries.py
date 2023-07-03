
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.uat4t1h.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})
print ("Displaying Student Documents from find query")
for doc in student_list:
     print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
kaladin = students.find_one({"student_id" : 1007})  
    
print ("\n -- Displaying Student Document from find_one query --")
print (" Student ID: " + kaladin["student_id"] + "\n First Name:" + kaladin["first_name"] + "\n Last Name:" + kaladin["last_name"] + "\n") 

input("\n End of Program, please press any key to exit")




