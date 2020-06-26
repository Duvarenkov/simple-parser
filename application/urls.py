from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from application.views import scrape, ResultView

router = routers.SimpleRouter()
router.register(r'scrape/result', ResultView)

urlpatterns = [
    # url(r'^$', view=views.index, name='index'),
    url(r'scrape/?$', view=scrape, name='scrape'),
    path('admin/', admin.site.urls),
]
urlpatterns.extend([*router.urls])
print(urlpatterns)
