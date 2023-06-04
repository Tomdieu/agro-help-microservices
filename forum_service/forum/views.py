from django.shortcuts import render

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, GenericViewSet

# from rest_framework.views

from .serializers import (
    ForumSerializer,
    ForumListSerializer,
    ForumCommentListSerializer,
    ForumCommentSerializer,
)

from rest_framework.permissions import IsAuthenticated

from .models import Forum, ForumComment

# Create your views here.


class ForumViewSet(ModelViewSet, GenericViewSet):
    """
    This api view get all the forums
    """

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ForumListSerializer
        return ForumSerializer

    queryset = Forum.objects.all()


class ForumCommentViewSet(ModelViewSet, GenericViewSet):
    """
    This api helps to get post created in a forum
    """

    permission_classes = [IsAuthenticated]
    queryset = ForumComment.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ForumCommentListSerializer

        return ForumCommentSerializer
