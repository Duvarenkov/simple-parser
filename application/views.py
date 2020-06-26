import json

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from rest_framework import viewsets, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from application.models import WebPage
from application.serializers import WebPageSerializer
from application.utils import parse_url

validate = URLValidator()


class ResultView(mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """
    Parsed WebPages
    """
    serializer_class = WebPageSerializer
    queryset = WebPage.objects.all()
    permission_classes = [permissions.AllowAny]


@api_view(['GET', 'POST'])
def scrape(request):
    if request.method == 'POST':
        url = request.data
        try:
            validate(url)
        except ValidationError as e:
            return Response({'message': e, 'url': url})

        parsed = parse_url(url)
        WebPage.objects.create(url=url, parsed=json.dumps(parsed))

        return Response(parsed)

    return Response('Make a POST application/json request with a URL to parse as a simple string')
