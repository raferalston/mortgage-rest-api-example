from ast import mod
from rest_framework import viewsets
from rest_framework.response import Response

from .models import BankModel
from .serializers import BankSerializer


def calculate_payment(rate_max, price, deposit, term):
    monthly_rate = rate_max / 12 / 100
    overall_rate = (1 + monthly_rate) ** (term * 12)
    credit_amount = price - (price / 100 * deposit)
    monthly_payment = int(credit_amount * monthly_rate * overall_rate // (overall_rate - 1))
    return monthly_payment


class MortgageViewSet(viewsets.ModelViewSet):
    queryset = BankModel.objects.all()
    serializer_class = BankSerializer

    def list(self, request):
        '''Applying new field to serialized data if query_params exists'''
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        keys_param = request.query_params.keys()

        #TODO: refactor for DRY later
        if request.query_params and 'price' in keys_param and 'deposit' in keys_param and 'term' in keys_param:
            for d in serializer.data:
                d['payment'] = calculate_payment(
                    float(d['rate_max']), 
                    float(request.query_params['price']), 
                    float(request.query_params['deposit']), 
                    float(request.query_params['term'])
                    )
        if 'order' in keys_param and 'payment' in request.query_params.values():
            return Response(sorted(serializer.data, key=lambda data: data.get('payment')))
            
        return Response(serializer.data)

    def get_queryset(self):
        '''Queryset changed before modified serialized data'''
        queryset = self.queryset

        if self.request.query_params:
            keys = self.request.query_params.keys()
            values = self.request.query_params
            modified_query_params = {}
            fields_names = [field.name for field in BankModel._meta.get_fields()]

            for key in keys:
                if key in fields_names:
                    if 'min' in key:
                        modified_query_params[f'{key}__gte'] = values[key]
                    elif 'max' in key:
                        modified_query_params[f'{key}__lte'] = values[key]
                    else:
                        modified_query_params[key] = values[key]

            queryset = queryset.filter(**modified_query_params)

            if 'order' in keys and 'term' in values['order']:
                order = self.request.query_params['order']
                queryset = queryset.order_by(f'{order}_min')

        return queryset