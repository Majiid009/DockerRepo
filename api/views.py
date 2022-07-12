from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request, birthYear):
    person = {"name":"Abdelmadjid", 'age':2022-birthYear}
    return Response(person)
