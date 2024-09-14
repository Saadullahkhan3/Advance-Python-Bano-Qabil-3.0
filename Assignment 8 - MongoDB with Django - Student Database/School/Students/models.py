from mongoengine import Document, StringField, DateField, IntField



class Student(Document):
    name = StringField(required=True, max_length=200)
    father_name = StringField(required=True, max_length=100)
    phone = IntField(required=True)
    age = DateField(required=True)
    gender = StringField(required=True, choices=('m', 'f'))


    def __str__(self):
        return f"{self.name} | {self.father_name}"
  


# Schema for Student Model
{
    "name": "Saadullah Khan",
    "father_name": "Muhammad Ali Shahzad",

    # Don't include +91, etc. Use direct 92000...
    "phone": 920123456789,

    # YYYY-MM-DD
    "age": "2010-05-09",

    # Choice between m(male) and f(female)
    "gender": "m"
}



