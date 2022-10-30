from .models import Mailing, Client
from .serializers import MailingSerializer, ClientSerializer
from rest_framework import viewsets, mixins


class MailingViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class ClientViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

