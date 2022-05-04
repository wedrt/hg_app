from django.urls import path
from . import views
from hg import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path("submit_kill/", views.submit_kill, name= "submit_kill"),
    path("submit_package/", views.submit_package, name= "submit_package"),
    path("rules/", views.rules, name="rules"),
    path("stats/", views.stats, name="stats"),
    path("players/", views.players, name="players"),
    path("submit_point/", views.submit_point, name="submit_point"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)