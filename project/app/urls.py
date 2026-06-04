from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('task_list/',views.task_list,name='task_list'),
    path('delete_task/<int:id>/',views.Delete_task,name='task'),
    path('update_task/<int:id>/',views.update_task,name='update_task'),
]
