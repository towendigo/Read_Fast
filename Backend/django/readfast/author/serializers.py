from rest_framework import serializers
from .models import Author, Author_en, LanguageSet

Author_Models = LanguageSet().values()

class BaseAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    author = BaseAuthorSerializer()
    class Meta:
        model = Author_Models
        fields = "__all__"
