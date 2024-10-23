from rest_framework import serializers, viewsets
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'  # Include all fields

    def get_image(self, obj):
        request = self.context.get('request')
        # Return the full URL for the image if it exists
        return request.build_absolute_uri(obj.image.url) if obj.image else None

