from django.contrib import admin
from django.urls import path, include
import codex_judging.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit/', codex_judging.views.submit_code),
]