from rest_framework.views import APIView


class BaseAPIView(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_user = None

    def dispatch(self, request, *args, **kwargs):
        self.current_user = request.user
        return super().dispatch(request, *args, **kwargs)
