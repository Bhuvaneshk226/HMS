from django.urls import path
from .import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    # path('Students',views.Students,name='Students'),
    path('Teachers',views.Teachers,name='Teachers'),
    path('Transport',views.Transport,name='Transport'),
    path('Accounts',views.Accounts,name='Accounts'),
    path('school_cards',views.school_cards , name='school_cards'),
    path('school_add',views.school_add , name='school_add'),

]