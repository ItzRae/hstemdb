from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Author, Creates, Project, File
from .serializers import AuthorSerializer, CreatesSerializer, ProjectSerializer, FileSerializer
from urllib.parse import unquote
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Project
from .serializers import ProjectSerializer

@api_view(['POST'])
def create_project(request):
    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorList(generics.ListAPIView):
    # SQL Query: SELECT * FROM hstem_author;
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CreatesList(generics.ListAPIView):
    # SQL Query: SELECT * FROM hstem_creates;
    queryset = Creates.objects.all()
    serializer_class = CreatesSerializer

    


class CreatesDetailView(APIView):
    def get(self, request, title):
        decoded_title = unquote(title)

        # SQL Query: SELECT * FROM hstem_creates WHERE title=decoded_title;
        creates = get_object_or_404(Creates, title=decoded_title)
        creates_serializer = CreatesSerializer(creates)

        # SQL Query: SELECT * FROM hstem_file WHERE title=decoded_title;
        files = get_object_or_404(File, title=decoded_title)
        file_serializer = FileSerializer(files)

        # SQL Query: SELECT * FROM hstem_project WHERE title=decoded_title;
        projects = get_object_or_404(Project, title=decoded_title)
        project_serializer = ProjectSerializer(projects)

        response_data = {
            'creates': creates_serializer.data,
            'file': file_serializer.data,
            'project': project_serializer.data
        }

        return Response(response_data)


class ProjectList(generics.ListAPIView):
    # SQL Query: SELECT * FROM hstem_project;
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class FileList(generics.ListAPIView):
    # SQL Query: SELECT * FROM hstem_files;
    queryset = File.objects.all()
    serializer_class = FileSerializer


