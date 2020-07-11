from rest_framework import serializers

from blog.models import blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = (
            'author',
            'title',
            'slug',
            'bmemo',
            'category',
            'status',
            'publish',
            )