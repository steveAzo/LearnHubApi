import pymongo
import json
from utils.db_connection import connect_to_database

client, db = connect_to_database()
collection = db["courses"]

# Read courses from courses.json
with open("courses.json", "r") as f:
    courses = json.load(f)

collection.create_index("name")

# Adding rating field to each course
for course in courses:
    course['rating'] = { 'total': 0, 'count': 0 }

# Adding rating field to each chapter
for course in courses:
    for chapter in course['chapters']:
        chapter['rating'] = {'total': 0, 'count': 0}

# Add courses to collection
for course in courses:
    collection.insert_one(course)

# Close MongoDB connection
client.close()

