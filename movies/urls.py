from django.urls import path

from .views import *

urlpatterns = [
    path("", MoviesView.as_view(), name="main"),
    path("detail/<slug:slug>", MovieDetailView.as_view(), name="detail_view"),
    # path("test_for_forms/", ActorsAdd.as_view(), name="test_forms")
    path("review/<int:pk>", ReviewView.as_view(), name="create_review"),

]
