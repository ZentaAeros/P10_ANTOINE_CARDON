from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import User

from projects.models import Project, Contributor, Issue, Comment
from projects.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def project(request):
    if request.method == 'GET':
        projects = Project.objects.filter(contributors__user=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data.copy()
        data['author'] = request.user.id

        serializer = ProjectSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            project = serializer.save()
            Contributor.objects.create(user=request.user, project=project, role='author')
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def project_details(request, project_pk):
    project = get_object_or_404(Project, id=project_pk)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = request.data.copy()
        data['author'] = project.author.id

        serializer = ProjectSerializer(project, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == 'DELETE':
        project.delete()
        return Response('Le contenu a bien été supprimé')