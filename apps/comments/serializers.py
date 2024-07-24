from rest_framework import serializers

from apps.comments.models import Comment,CommentFavorite


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['text','blog',]


class CommentLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentFavorite
        fields = '__all__'


class CommentLikeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentFavorite
        fields = ['like_comment',]