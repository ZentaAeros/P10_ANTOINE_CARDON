from django.db import models
from django.conf import settings

# Create your models here.
TYPES = [
    ("backend", "backend"),
    ("frontend", "frontend"),
    ("android", "android"),
    ("ios", "ios"),
]

tags = [("bug", "bug"), ("upgrade", "upgrade"), ("task", "task")]

prioritys = [("low", "low"), ("medium", "medium"), ("high", "high")]

states = [("todo", "todo"), ("in progress", "in progress"), ("done", "done")]

roles = [("author", "author"), ("contributor", "contributor")]


class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    type = models.CharField(choices=TYPES, max_length=10)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author"
    )


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="contributors"
    )
    role = models.CharField(choices=roles, max_length=15)


class Issue(models.Model):
    title = models.CharField(max_length=500)
    desc = models.CharField(max_length=1000)
    tag = models.CharField(choices=tags, max_length=10)
    priority = models.CharField(choices=prioritys, max_length=10)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(choices=states, max_length=15)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    assignee_user_id = models.ForeignKey(to=Contributor, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
