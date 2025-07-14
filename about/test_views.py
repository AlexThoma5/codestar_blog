from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm

# Create your tests here.


class TestAboutViews(TestCase):

    def setUp(self):
        """ Creates about me content"""
        self.about_content = About(title="About title", content="some content for about")
        self.about_content.save()

    def test_render_about_page_with_collaboration_form(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIn(b"some content for about", response.content)
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)
