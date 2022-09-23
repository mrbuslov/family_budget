from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls', namespace='account')),
    path('',include('family_budget.urls', namespace='autostop')),
]



if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns