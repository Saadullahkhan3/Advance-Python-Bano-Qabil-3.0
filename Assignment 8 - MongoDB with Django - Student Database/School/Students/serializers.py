from .models import Student

from rest_framework_mongoengine import serializers



'''
Serializers:
Use to handle data that it can be stored according to our model, data that not fit in our given model that will be discarded!
'''


class StudentSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Student
        fields = '__all__'
 

