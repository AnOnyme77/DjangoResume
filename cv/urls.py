from django.conf.urls import url
from cv import views

urlpatterns = [
    url(r'^stats$', views.main_resume_stats, name='main_resume_stats'),
    url(r'^stats/gathering$', views.resume_cv, name='resume_stats'),
    url(r'^$', views.main_cv, name='main_cv'),
]
