from django.urls import path, include
from .views import discussion_home_view, dynamic_post_view, delete_post_view, delete_reply_view

urlpatterns = [
    path("", discussion_home_view, name="discussion_home"),
    path("<int:id>/", dynamic_post_view, name="dynamic_post"),
    path("<int:id>/delete", delete_post_view, name="delete_post"),
    path("<int:rid>/delete_reply", delete_reply_view, name="delete_reply")
]
