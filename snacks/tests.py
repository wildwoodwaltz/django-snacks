from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.


class SnackTest(SimpleTestCase):

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


    def test_no_page_found(self):
        url = 'fakey_pagey_heart/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
