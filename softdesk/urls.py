"""softdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from projects.views import project, project_details, contributors, contributor_detail, issue, issue_detail, comment, comment_detail
from users.views import SignupView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/signup/", SignupView.as_view(), name="signup"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/projects/", project, name="project"),
    path("api/projects/<int:project_pk>/", project_details, name="project_details"),
    path("api/projects/<int:project_pk>/contributors/", contributors, name="contributors"),
    path("api/projects/<int:project_pk>/contributors/<int:contributor_pk>/", contributor_detail, name="contributors_details"),
    path("api/projects/<int:project_pk>/issues/", issue, name="issues"),
    path('api/projects/<int:project_pk>/issues/<int:issue_pk>/', issue_detail, name="issues_details"),
    path('api/projects/<int:project_pk>/issues/<int:issue_pk>/comments/', comment, name="comment"),
    path('api/projects/<int:project_pk>/issues/<int:issue_pk>/comments/<int:comment_pk>/', comment_detail, name="comment_details"),
]
