from rest_framework import serializers

from .models import Forum, ForumComment, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "type"]
        extra_kwargs = {
            "email": {
                "required": True,
            },
        }


class ForumCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = ForumComment
        fields = "__all__"

    def get_replies(self, obj: ForumComment):
        replies = ForumComment.objects.filter(parent=obj)

        return ForumCommentSerializer(replies, many=True).data


class ForumCommentListSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    author = UserSerializer()

    class Meta:
        model = ForumComment
        fields = "__all__"

    def get_replies(self, obj: ForumComment):
        replies = ForumComment.objects.filter(parent=obj)

        return ForumCommentSerializer(replies, many=True).data


class ForumCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = ForumComment

        fields = "__all__"

    def get_replies(self, obj: ForumComment):
        comments = ForumComment.objects.filter(parent=obj)

        return ForumCommentListSerializer(
            comments, many=True, context={"request": self.context["request"]}
        ).data


class ForumCommentListSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    author = UserSerializer()

    class Meta:
        model = ForumComment

        fields = "__all__"

    def get_replies(self, obj: ForumComment):
        comments = ForumComment.objects.filter(parent=obj)

        return ForumCommentListSerializer(
            comments, many=True, context={"request": self.context["request"]}
        ).data


class ForumSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Forum
        fields = "__all__"

    def get_comments(self, obj: Forum):
        messages_instance = ForumComment.objects.filter(forum=obj)
        message_serializer = ForumCommentListSerializer(
            messages_instance, many=True, context={"request": self.context["request"]}
        )
        return message_serializer.data


class ForumListSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    author = UserSerializer()

    class Meta:
        model = Forum
        fields = "__all__"

    def get_comments(self, obj: Forum):
        messages_instance = ForumComment.objects.filter(forum=obj)
        message_serializer = ForumCommentListSerializer(
            messages_instance, many=True, context={"request": self.context["request"]}
        )
        return message_serializer.data
