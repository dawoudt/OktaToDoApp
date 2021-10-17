# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register(r'todos', views.TodoViewSet, basename='todo')
urlpatterns = router.urls

# urlpatterns += [
#     path('todo/', views.Todo.as_view())
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)