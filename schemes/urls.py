from django.urls import path, include
from .views import all_schemes_view, user_schemes_view, dynamic_scheme_view,catagory_scheme_view

urlpatterns = [
    path("", all_schemes_view, name="all_schemes"),
    path("user_schemes/", user_schemes_view, name="user_schemes"),
    path("<int:id>/", dynamic_scheme_view, name="dynamic_scheme"),
    path("<str:cat>/",catagory_scheme_view,name="catagory_schemes")
]
