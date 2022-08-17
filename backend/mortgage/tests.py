from django.urls import reverse
from django.test import TestCase, Client

from rest_framework import status
from rest_framework.test import APITestCase

from .models import BankModel


c = Client()

class MortgageTest(TestCase):
    """Basic django testing"""
    def setUp(self):
        bank_1 = BankModel(bank_name='bank_1')
        bank_1.save()
    
    def test_setup_bank_count(self):
        bank_count = BankModel.objects.count()
        self.assertEqual(bank_count, 1)

    def test_all_urls(self):
        mortgage_list = reverse('mortgage-list')
        response = self.client.get(mortgage_list)
        self.assertTrue(response.status_code == 200)

    
class FunctionalityTest(TestCase):
    """DRF testing"""
        
    def test_post_bank(self):
        url = reverse('mortgage-list')
        data = {'bank_name': 'test_bank_1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BankModel.objects.count(), 1)
        self.assertEqual(BankModel.objects.get().bank_name, 'test_bank_1')

    def test_patch_bank(self):
        url = reverse('mortgage-list')
        data = {'bank_name': 'test_bank_1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BankModel.objects.count(), 1)
        self.assertEqual(BankModel.objects.get().bank_name, 'test_bank_1')

        url = reverse('mortgage-detail', args=(1,))
        import json 
        data = json.dumps({'bank_name': 'edited_name'})
        response = self.client.patch(url, data, content_type='application/json')
        self.assertEqual(BankModel.objects.get().bank_name, 'edited_name')

    def test_delete_bank(self):
        url = reverse('mortgage-detail', args=(1,))
        response = self.client.delete(url)
        self.assertEqual(BankModel.objects.count(), 0)