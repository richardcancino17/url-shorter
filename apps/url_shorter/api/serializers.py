from apps.url_shorter.models import UrlShorter
from rest_framework import serializers
from corebackend.utils import url_generator_shorter
from django.conf import settings


class CreateUrlShorterSerializer(serializers.ModelSerializer):
    link_shorter = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UrlShorter
        fields = ('link_original', 'link_shorter')
        write_only_fields = ('code_shorter',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        url = UrlShorter.objects.create(
            link_original=validated_data['link_original']
        )
        url.code_shorter = url_generator_shorter(8)
        url.save()
        return url

    def get_link_shorter(self, obj):
        return settings.HOST_URL + obj.code_shorter


class SeeUrlShorterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlShorter
        fields = ('id', 'link_original', 'code_shorter', 'times_used',
                  'is_active', 'created_at', 'update_at')


class UrlShorterSerializer(serializers.Serializer):
    pass
