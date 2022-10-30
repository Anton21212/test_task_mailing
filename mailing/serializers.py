from rest_framework import serializers
from .models import Mailing, Client


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = '__all__'

    def create(self, validated_data):
        mailing = Mailing.objects.create(**validated_data)
        return mailing


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    phone_number = serializers.IntegerField(max_value=79999999999, min_value=70000000000)
    mobile_operator_code = serializers.IntegerField(max_value=9999, min_value=0)

    def validate(self, data):
        phone_number = str(data['phone_number'])
        mobile_operator_code = str(data['mobile_operator_code'])
        if mobile_operator_code not in phone_number:
            raise serializers.ValidationError('incorrect mobile_operator_code')
        return data
