from .models import Student
from .serializers import StudentSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response



# pk is unique id for each Student entry.


class StudentViewSet(viewsets.ModelViewSet):
    # Use as reference for Database, we can customize it to filter data
    queryset = Student.objects.all()    

    serializer_class = StudentSerializer

    # SORRY
    '''
    I explicity created this method, but I realised that there is no need to do below stuff, I wasted my time a lot
    SORRY, I am not removing it, I kept is to remmeber my fault!
    '''

    # # GET
    # def list(self, request):
    #     serializer = self.serializer_class(self.queryset, many=True)
    #     return Response(serializer.data)


    # # POST
    # def create(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # # Get with ID
    # def retrieve(self, request, pk=None):
    #     student = self.queryset.get(pk=pk)
    #     serializer = self.serializer_class(student)
    #     return Response(serializer.data)


    # # PUT - Need full data
    # def update(self, request, pk=None):
    #     student = self.queryset.get(pk=pk)
    #     serializer = self.serializer_class(student, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # # PATCH - Flexible, no need entire data
    # def partial_update(self, request, pk=None):
    #     student = self.queryset.get(pk=pk)
    #     serializer = self.serializer_class(student, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # # DELETE
    # def destroy(self, request, pk=None):
    #     student = self.queryset.get(pk=pk)
    #     student.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    


