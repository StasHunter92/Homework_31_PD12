from django.urls import path

from ads import views

# ----------------------------------------------------------------------------------------------------------------------
# Create advertisement urls
urlpatterns = [
    path('', views.AdvertisementListView.as_view()),
    path('<int:pk>/', views.AdvertisementDetailView.as_view()),
    path('create/', views.AdvertisementCreateView.as_view()),
    path('<int:pk>/update/', views.AdvertisementUpdateView.as_view()),
    path('<int:pk>/delete/', views.AdvertisementDeleteView.as_view()),
    # path('<int:pk>/image_upload/', views.AdUploadImage.as_view()),
]
