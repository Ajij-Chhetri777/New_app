from django.urls import path
from quiz.views import home, register, search, addForm, delet, updat, login_view 
# from django.contrib.auth import views as auth_views
from quiz.forms import LoginForm
urlpatterns = [
    path('home/',home,name='home'),
    path('',register,name ='register'),
    # path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm), name = 'login_view'),
    path('search/',search,name='search'),
    path('add/',addForm,name='add'),
    path('<int:id>/',delet,name='delete'),
    path('update/<int:id>/',updat,name='update'),
    path('login/',login_view,name='login_view'),
]
