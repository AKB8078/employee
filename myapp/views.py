
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer


@api_view(['GET'])
def index(request):
    employeedetails = {
        "name": "John Doe",
        "age": 30,
        "department": "HR",
        "salary": 50000
    }
    return Response(employeedetails)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def employee(request):
    if request.method == 'GET':
      
        objEmployee = Employee.objects.all()
        serializer = EmployeeSerializer(objEmployee, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
       
        data = request.data
        serializer = EmployeeSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
       
        data = request.data
        try:
            obj = Employee.objects.get(id=data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)

        serializer = EmployeeSerializer(obj, data=data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
      
        data = request.data
        try:
            obj = Employee.objects.get(id=data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)

        serializer = EmployeeSerializer(obj, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
       
        data = request.data
        try:
            obj = Employee.objects.get(id=data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)

        obj.delete()
        return Response({"message": "Employee deleted successfully"}, status=204)
