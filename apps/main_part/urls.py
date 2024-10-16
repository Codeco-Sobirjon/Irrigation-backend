from django.urls import path
from apps.main_part.views import *


urlpatterns = [
    path('about', AboutInstitutionListView.as_view()),
    path('sliders', SliderMainPartListView.as_view()),
    path('partners', PartnersListView.as_view()),
    path('videos', VideoInstitutionListView.as_view()),
    path('announcement', AnnouncementListView.as_view()),
]

