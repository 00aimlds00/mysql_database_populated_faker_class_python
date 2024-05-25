# mysql_database_populated_faker_class_python
Loading a database with fake data using Faker class of Python
This procedure can be followed to create random data using faker class in Python and perform query in MySQL after uploading the same. 
It will be useful for software testing and can be easily scaled as per requirements.

MySQL table is created first, give a name employee

![image](https://github.com/00aimlds00/mysql_database_populated_faker_class_python/assets/114329091/e019bdd5-4283-4223-9e58-fd1fb1bc9c65)

Python Code for creating a connection and using a JSON template for storing the faker class data

#import what you need

import mysql.connector
from faker import Faker
import json

#create a connection
spcdatabase=mysql.connector.connect(
    user='root',
    host='localhost',
    password='HAHAHAHAHA',
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

After running the Python code the table gets populated with the fake data which is ready for further useful query and demonstration.

![image](https://github.com/00aimlds00/mysql_database_populated_faker_class_python/assets/114329091/1d1de05e-98e8-46ab-a582-2cf793ed156d)
![image](https://github.com/00aimlds00/mysql_database_populated_faker_class_python/assets/114329091/de5919a6-0380-45a6-b7ff-9f4618f2d19a)
![image](https://github.com/00aimlds00/mysql_database_populated_faker_class_python/assets/114329091/4116bca3-9e6d-4fa0-a95f-bb8508a1f721)


You have run into the end of the file, thanks for reading

You can contribute to the author paypal.me/somnathpaulchoudhury



