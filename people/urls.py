from django.urls import path

from . import views

app_name = "people"
urlpatterns = [
    path(
        "relationships/",
        views.RelationshipsListView.as_view(),
        name="relationships_list",
    ),
    path("add/", views.PersonCreateView.as_view(), name="person_create"),
    path(
        "<str:username>/update/", views.PersonUpdateView.as_view(), name="person_update"
    ),
    path("<str:username>/", views.PersonDetailView.as_view(), name="person_detail"),
    path("", views.PeopleListView.as_view(), name="people_list"),
]
