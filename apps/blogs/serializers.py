from rest_framework import serializers

from apps.blogs.models import Blog,BlogImage,BlogFavorite



class BlogImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogImage
        fields = '__all__'


class BlogLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogFavorite
        fields = '__all__'

class BlogLikeCreateSeralizer(serializers.ModelSerializer):

    class Meta:
        model = BlogFavorite
        fields = ['blog']


class BlogCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = [
            'title',
            'description',
            'tag',
        ]


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id','title']


class BlogRetrieveSerializer(serializers.ModelSerializer):
    blog_image = BlogImageSerializer(read_only = True,many=True)
    like_blog = BlogLikeSerializer(read_only = True,many =True)
    total_like = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['author']

    def get_total_like(self,instance):
        return instance.like_blog.all().count()