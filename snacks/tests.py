from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from snacks.models import Snack

# Create your tests here.


class SnackTest(TestCase):

# TEST CASE 
    def test_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_base(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')

# TEST CASE ABOUT PAGE
    def test_about_page_status(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_base(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')

# TEST CASE NO PAGE FOUND
    def test_no_page_found(self):
        url = 'fakey_pagey_heart/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

# TEST CASE SNACKS LIST
    def test_snack_page_status(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_page_base(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')

    def test_snack_page_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

# TEST SNACK ITEM

    def test_detail_page_context(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        snack = response.context['snack']
        self.assertEqual(snack.name, "Chocodile")
        self.assertEqual(snack.purchaser, 'Tibi')
