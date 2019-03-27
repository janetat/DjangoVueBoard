from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

from .boards import BoardAPIVIew
from .account import AccountAPIView
from .cards import CardAPIView
from .pipelines import PipeLineAPIView


router = DefaultRouter()
router.register(r'boards', BoardAPIVIew)
router.register(r'cards', CardAPIView)
router.register(r'pipelines', PipeLineAPIView)

urlpatterns = [
    path('account/', login_required(AccountAPIView.as_view())),
    path('', include(router.urls)),
]

# API docs
schema_view = get_swagger_view(title='KANBAN API')

urlpatterns += [
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='KANBAN API'))
]
