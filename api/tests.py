from django.test import TestCase
from .models import Menu, Booking

# Create your tests here.
class MenuItemTest(TestCase):
    def test_menu(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")


class BookingTest(TestCase):
    def test_booking(self):
        item = Booking.objects.create(name="Ash", number_of_guests=5, booking_date="2023-05-07T16:07:16Z")
        self.assertEqual(str(item), "Ash")