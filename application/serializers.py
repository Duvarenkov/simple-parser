import json

from rest_framework import serializers

from application.models import WebPage


class WebPageSerializer(serializers.ModelSerializer):
    """
    WebPage serializer
    """
    parsed = serializers.SerializerMethodField()

    def get_parsed(self, obj):
        """
        Returns correct JSON without escaping.
        This is used due to SQLite not supporting JSON field in models.
        Postgres and latest MySQL support JSON fields.
        """
        return json.loads(obj.parsed)

    class Meta:
        model = WebPage
        fields = '__all__'
