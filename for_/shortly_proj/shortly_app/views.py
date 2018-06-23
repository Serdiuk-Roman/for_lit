
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from shortly_app.permissions import IsOwnerOrReadOnly
from shortly_app.models import Snippet, Shortly
from shortly_app.serializers import SnippetSerializer, UserSerializer, \
    ShortlySerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        'shortly': reverse('shortly-list', request=request, format=format)
    })


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Этот набор представлений автоматически создает действия `list` и `detail`.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShortlyViewSet(viewsets.ModelViewSet):
    queryset = Shortly.objects.all()
    serializer_class = ShortlySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
