from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("home/", views.TestPage.as_view(), name="test"),
    path("thanks/", views.ThanksPage.as_view(), name="thanks"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("posts/", include("posts.urls")),
    path("groups/", include("groups.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/",include(debug_toolbar.urls))
    ] + urlpatterns
