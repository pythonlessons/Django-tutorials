from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="hemepage"),
    path("<series>", views.series, name="article"),
    path("<series>/<article>", views.article, name="article"),
]