from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('task_list/',views.task_list,name='task_list'),
    path('delete_task/<int:id>/',views.Delete_task,name='task'),
    path('update_task/<int:id>/',views.update_task,name='update_task'),
    path('',views.login_page,name='login_page'),
    path('register/',views.register_page,name='register_page')
]
