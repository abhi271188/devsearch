from dataclasses import fields
from importlib.metadata import files
from pyexpat import model
from rest_framework import serializers
from projects.models import Project, Tags, Reviews
from users.models import Profile

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    owner = profileSerializer(many = False)
    #tag = tagSerializer(many = True)
    tag = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.reviews_set.all()
        serializer = reviewSerializer(reviews, many = True)
        return serializer.data

    def get_tag(self, obj):
        tags = obj.tag.all()
        serializer = tagSerializer(tags, many = True)
        return serializer.data