from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo import serializers, models

class ToDoList(APIView):
    """
    List all todo lists when the GET method is called.
    Add new ToDo lists when the POST method is called.
    Delete a ToDo list when the DELETE method is called.
    """
    
    def get(self, request, format=None):
        """
        Return a list of all the ToDoList objects in the database.
        """
        # query the database for all instances of the ToDoList model
        todo_lists = models.ToDoList.objects.all()
        
        # serialize the data into a returnable format
        serializer = serializers.ToDoList(todo_lists, many=True)
        
        return Response(serializer.data)
        
    def post(self, request, format=None):
        """
        Creates a new ToDoList with the given request data.
        """
        # deserialize the data from the request
        serializer = serializers.ToDoList(data=request.data)
        # if the data validation done by the serialize passes
        if serializer.is_valid():
            # then save the ToDoList to the database and return the resulting ToDoList
            serializer.save()
            return Response(serializer.data)
        else:
            # Throw a 404 error if the serializer detected the data wasn't valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
