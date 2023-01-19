from django.urls import path
from .import views
urlpatterns = [
  
    path("",views.index,name="index"),
    path("home/",views.home,name="Home"), # route ...
    path("about/",views.about,name="About"),
    path("contact/",views.contact,name="Contact"),
   
    path("feedback/",views.feedback,name="Feedback"),
    path("register/",views.register,name="Register"), # register router ...
    path("login/",views.login,name="login"), # login router !!!
    path("logout/",views.logout,name="Logout"),

    path("private/",views.private,name="private"),
 
]