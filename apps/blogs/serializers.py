from rest_framework import serializers

from apps.blogs.models import Blog,BlogImage



class BlogImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogImage
        fields = '__all__'


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

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['author']
