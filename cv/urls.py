from django.conf.urls import url
from cv import views

urlpatterns = [
    url(r'^$', views.main_cv, name='main_cv'),
    url(r'^(?P<cvId>\d+)$', views.cv, name='cv'),
    url(r'^user/(?P<username>\w+)$', views.usercv, name='cv'),
    url(r'^admin/login$', views.login, name='cv_login'),
    url(r'^admin$', views.admin, name='cv_admin'),
    url(r'^stats$', views.main_resume_stats, name='main_resume_stats'),
    url(r'^stats/gathering$', views.resume_cv, name='resume_stats'),
]
