from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('update_student/<int:id>/', views.update_student, name='update_student'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('teachers/', views.teachers, name='teachers'),
    path('update_teacher/<int:id>/', views.update_teacher, name='update_teacher'),
    path('delete_teacher/<int:id>/', views.delete_teacher, name='delete_teacher'),
    path('expenses/', views.expenses, name='expenses'),
    path('update_expense/<int:id>/', views.update_expense, name='update_expense'),
    path('delete_expense/<int:id>/', views.delete_expense, name='delete_expense'),
    path('calculate/', views.calculate, name='calculate'),
]
