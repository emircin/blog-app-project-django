from django.urls import path
from .views import new_tag, tag_list, tag_detail, add_comment_to_post

urlpatterns = [
    path("list/", tag_list, name="list"),
    path("newtag/", new_tag, name="new_tag"),
    path("detail/<int:id>/", tag_detail, name="tag_detail"),
    path('detail/<int:id>/comment/', add_comment_to_post, name='add_comment_to_post'),

    
]