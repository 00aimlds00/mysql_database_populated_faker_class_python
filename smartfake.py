#import what you need

import mysql.connector
from faker import Faker
import json

#create a connection
spcdatabase=mysql.connector.connect(
    user='root',
    host='localhost',
    password='r00tp@$$w0rd',
    database='company'
    )

spccur=spcdatabase.cursor()

# JSON template for a employee
person_template = {
    "id": 0,
    "name": "",
    "department": "",
    "designation": "",
    "salary": 0
}

#Create instance of class Faker
fake = Faker()

num_people = 100
people_data = []

for i in range(1, num_people + 1):
    person = {
        "id": i,
        "name": fake.name(),
        "department": fake.job(),
        "designation": fake.job(),
        "salary": fake.random_int(min=90000, max=300000, step=1000)
    }
    people_data.append(person)
    

insert_query = """
INSERT INTO employees (id, name, department, designation, salary)
VALUES (%s, %s, %s, %s, %s) """


for person in people_data:
    spccur.execute(insert_query, (
        person["id"],
        person["name"],
        person["department"],
        person["designation"],
        person["salary"]
    ))

spcdatabase.commit()
spccur.close()
spcdatabase.close()


