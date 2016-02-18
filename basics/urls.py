from django.conf.urls import url

from . import views

app_name = 'basics'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_problem/', views.add_problem, name='add_problem'),
    url(r'^all_problems/', views.all_problems, name='all_problems'),
    url(r'^problem/view/(?P<suppliedId>\d+)/$', views.view_problem, name='view_problem'),
    url(r'^problem/edit/(?P<suppliedId>\d+)/$', views.edit_problem, name='edit_problem')
]