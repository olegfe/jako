"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase


# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
   # -*- coding: utf-8 -*-
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Домашняя страница', 1, 200)

    def test_contact(self):
       """Tests the contact page."""
       response = self.client.get('/contact')
       self.assertContains(response, 'Наши контакты', 3, 200)

    def test_about(self):
       """Tests the about page."""
       response = self.client.get('/about')
       self.assertContains(response, 'Информация о сайте', 3, 200)
def test_about(self):
        """Tests the about page."""
        response = self.client.get('/sale')
        self.assertContains(response, 'акции', 3, 200)
def test_abt(self):
         """Tests the brend page."""
         response = self.client.get('/brend')
         self.assertContains(response, 'бренды', 3, 200)
        