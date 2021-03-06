from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include
from django.views.generic import TemplateView

from .accounts import signup as signup_view
from .api.urls import urlpatterns as api_urls

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('account/signup/', signup_view.SignUpView.as_view(), name='signup'),
    path('api/', include(api_urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

# let vue-router take care of the rest of urls
urlpatterns += [re_path('.*', login_required(TemplateView.as_view(template_name='index.html')))]
