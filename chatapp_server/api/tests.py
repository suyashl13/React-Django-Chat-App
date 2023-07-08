from django.test import TestCase

from api.users.models import CustomUser


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.custom_user = CustomUser()

    def make_super_user(self):
        self.custom_user.email = 'suyash.lawand@gmail.com'
        self.custom_user.username = 'suyashl13'
        self.custom_user.set_password('slaw1113')
        self.custom_user.phone = '919545731113'
        self.custom_user.save()

        self.assertEqual(self.custom_user.email, 'suyash.lawand@gmail.com')
