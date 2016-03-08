from django.conf.urls import url, include

from . import views

app_name = 'basics'
urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('registration.backends.hmac.urls', namespace='registration')),
    url(r'^acccounts/profile', views.user_profile, name='user_profile'),
    url(r'^add_problem/', views.add_problem, name='add_problem'),
    url(r'^add_problem_choices/', views.queue_add_problem_choices, name='add_problem_choices'),
    url(r'^all_problems/', views.all_problems, name='all_problems'),
    url(r'^problem/view/(?P<suppliedId>\d+)/$', views.view_problem, name='view_problem'),
    url(r'^problem/edit/(?P<suppliedId>\d+)/$', views.edit_problem, name='edit_problem'),
]
