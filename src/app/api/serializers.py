from rest_framework import serializers

from db.models import NavMenu, Page, PageContent


class NavMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavMenu
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = '__all__'
