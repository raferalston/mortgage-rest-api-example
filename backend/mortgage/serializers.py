from rest_framework import serializers

from .models import BankModel


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankModel
        fields = [
            'id', 'bank_name', 'term_min', 'term_max', 'rate_min', 'rate_max',
            'payment_min', 'payment_max'
        ]
    
    def validate(self, data):
        if data.get('term_min') and data.get('term_max'):
            if data['term_min'] > data['term_max']:
                raise serializers.ValidationError(
                    {'term_error': "Minimum term must not be greater than maximum"}
                    )
        if data.get('rate_min') and data.get('rate_max'):
            if data['rate_min'] > data['rate_max']:
                raise serializers.ValidationError(
                    {'rate_error': "Minimum rate must not be greater than maximum"}
                    )
        if data.get('payment_min') and data.get('payment_max'):
            if data['payment_min'] > data['payment_max']:
                raise serializers.ValidationError(
                    {'payment_error': "Minimum payment must not be greater than maximum"}
                    )
        return data