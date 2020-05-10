from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'cheikhnasall@gmail.com'
        password = 'aminatawelle'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_new_superuser(self):
        """Test creating a nex superuser"""
        user = get_user_model().objects.create_superuser(
            'saadbouhsall@gmail.com',
            'aminatawelle'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
