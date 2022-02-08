from rest_framework.serializers import ModelSerializer
from peaks.models import Peak


class PeakSerializer(ModelSerializer):

    class Meta(object):
        model = Peak
        fields = '__all__'
