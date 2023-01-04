from django.test import TestCase, Client
from django.urls import reverse



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse("home")
        self.pro_url = reverse("Pro")



    def test_home_get(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "views_temp/home.html")



    def test_pro_get(self):
        response = self.client.get(self.pro_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "views_temp/upgradeToPro.html")
