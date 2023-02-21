from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="Home"),
    path('admission/', views.admission, name="Admission"),
    path('result/', views.result, name="Result"),
    path('search/', views.searchResult, name="SearchResult"),
    path('artsearch/', views.searchArts, name="ResultArts"),
    path('onesearch/', views.searchOne, name="ResultOne"),
    path('jsssearch/', views.searchJss, name="ResultJss"),
    path('about/', views.about, name="About"),
    path('staff/', views.teacher, name="Staff"),
    path('news/', views.news, name="News"),
    path('single/<str:pk>/', views.single, name="Single"),
    path('classes/', views.classes, name="Classes"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)