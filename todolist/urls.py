from todolist.views import register
from django.urls import path
from todolist.views import show_todolist
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add_task
from todolist.views import get_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='newtask'),
    path('json/', get_json, name='get_json'),
]