from rest_framework import serializers
from .models import Author
from .models.author_template import Author_TEMPLATE


class BaseAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    author = BaseAuthorSerializer()
    class Meta:
        model = Author_TEMPLATE
        fields = '__all__'
