from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base_app.views import home, dashboard, upgrade_to_pro, forum_room, expenses, income, room, private_room, payments_page, death_of_a_bird, update_death_database


class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)


    def test_dashboard_url(self):
        url = reverse("dashboard")
        self.assertEqual(resolve(url).func, dashboard)


    def test_pro_url(self):
        url = reverse("Pro")
        self.assertEqual(resolve(url).func, upgrade_to_pro)


    def test_forum_url(self):
        url = reverse("Forum")
        self.assertEqual(resolve(url).func, forum_room)


    def test_expenses_url(self):
        url = reverse("expense")
        self.assertEqual(resolve(url).func, expenses)


    def test_income_url(self):
        url = reverse("income")
        self.assertEqual(resolve(url).func, income)


    def test_room_url(self):
        url = reverse("room", args=['roomname'])
        self.assertEqual(resolve(url).func, room)


    def test_privateRoom_url(self):
        url = reverse("private room", args=[2])
        self.assertEqual(resolve(url).func, private_room)


    def test_paymentPage_url(self):
        url = reverse("payment page")
        self.assertEqual(resolve(url).func, payments_page)


    def test_deadPage_url(self):
        url = reverse("dead page")
        self.assertEqual(resolve(url).func, death_of_a_bird)


    def test_updateDeathDatabase_url(self):
        url = reverse("death form", args=[11-11-2000, "animal"])
        self.assertEqual(resolve(url).func, update_death_database)
