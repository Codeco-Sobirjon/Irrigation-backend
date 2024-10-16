from django.urls import path
from apps.menu.views import *

urlpatterns = [
    path('categories', CategoryListView.as_view()),
    path('category/<int:id>/', CategoryDetailView.as_view())
]
