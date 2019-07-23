from django.urls import path

from . import views

urlpatterns = [
    path('inject-works', views.inject_works),
    path('request-scope-works', views.request_scope_works),
]
