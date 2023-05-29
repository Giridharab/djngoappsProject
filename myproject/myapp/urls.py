# from django.urls import path
# from .views import create_nugget, modify_nugget, delete_nugget, get_nugget, search_nugget
#
# urlpatterns = [
#     path('nugget/create/', create_nugget),
#     path('nugget/modify/<int:nugget_id>/', modify_nugget),
#     path('nugget/delete/<int:nugget_id>/', delete_nugget),
#     path('nugget/get/<int:nugget_id>/', get_nugget),
#     path('nugget/search/', search_nugget),
#  ]
#
# # #new
# from django.urls import path
# from .views import *
#
# urlpatterns = [
#     path("", Nuggetlist),
#     path("add/", post_Nugget),
#     path("modify/<int:id>/", Modify_Nugget),
#     path("delete/<int:id>/", delete_Nugget),
#     #path("search/", search_nugget)
#     path('search/', search_nugget, name='search_nugget'),
# ]
