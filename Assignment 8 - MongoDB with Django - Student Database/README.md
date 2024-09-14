# **School - Student**
## **MongoDB with Django**

School App's 'Student' is created to manage Students with ease!

---

### Note: Postman export is provided that have each API with its showcase and explanation!

---

##  **What it includes:**

<h3 id="get">GET</h3>
Give list of all Students.

<h3 id="post">POST</h3>
Add new Student.

<h3 id="get-with-id">GET with ID</h3>
Give any specific Student data by its ID.

<h3 id="put">PUT</h3>
Update Student data by its ID, use when need to update entire.

<h3 id="patch">PATCH</h3>
Partial Update Student data by its ID, use when need to update specific part of Student.

<h3 id="delete">DELETE</h3>
Delete the Student.

---

## Dependencies:
- Python 3.10+

> _Virtual Environment for dependencies is recommended!_

Use `requirements.txt` for installing dependencies

```
pip install -r requirements.txt
```

### Overview for Dependencies:

- **Django**:
Framework for Backend.

- **Mongo Engine**: 
Use to make models for ODM.

- **Rest Framework**:
Use to Handle API endpoints.

- **Rest Framework Mongo Engine**:
Use for serializing data between model and API(Use as ODM)

---

## How to run this?

> _Activate Virtual Environment._

Open terminal/cmd in same folder of this program.
- `cd Student`: Change your directory to locate `manage.py`
- `python manage.py runserver`: It will host a local server at `8000`, for custom port, provide that port at the end.

## Student

- Use `student/` param to access Student app.
- Use `student/` param another time to access operations of Student.

Your URL should look like:
```
http://127.0.0.1:8000/student/student/
```

There are six HTTP method available.
1. `GET` : [Read More..](#get)
2. `POST` : [Read More..](#post)
3. `GET with ID` : [Read More..](#get-with-id)
4. `PUT` : [Read More..](#put)
5. `PATCH` : [Read More..](#patch)
5. `DELETE` : [Read More..](#delete)


---
## [Saadullah Khan.](https://www.linkedin.com/in/Saadullahkhan3)
