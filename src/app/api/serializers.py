from rest_framework import serializers

from db.models import PageItemList, Page, PageContent


class PageItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageItemList
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = '__all__'
