from django.test import TestCase

# Create your tests here.
from .models import post
from django.urls import reverse


class postModelTest(TestCase):
    def setUp(self):
        post.objects.create(text='just a test')

    def test_text_context(self):
        post = post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')


class HomePageView(TestCase):
    def setUp(self):
        post.objects.create(text='this is another test')

    def test_view_url_exists(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
