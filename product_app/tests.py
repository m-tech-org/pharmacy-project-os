from django.test import TestCase
from django.contrib import auth, User
# Create your tests here.


class AuthTestCase(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('admin', 'admin@gmail.com', 'pass')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='admin', password='pass')