from django.urls import path
from apps.news.views import *

urlpatterns = [
    path('', NewsListView.as_view()),
    path('news/details/<int:id>/', NewsDetailsView.as_view()),
    path('achievement/quality', AchievementsCategoryListView.as_view()),
]
