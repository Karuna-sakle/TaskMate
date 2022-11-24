from django.contrib import admin
from django.urls import include, path
from todo_app import views as todolist_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",todolist_view.index, name="index"),
    path("todolist/",include("todo_app.urls")),
    path("account/",include("users_app.urls")),
    path("about", todolist_view.about, name="about"),
    path("contact", todolist_view.contact, name="contact"),
]
