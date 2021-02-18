from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from django.conf import settings


class BaseAPITest(APITestCase):
    def setUp(self, password=None) -> None:
        self.user = User(username="John Smith", email="john@example.com")
        self.user.set_password("123")
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def user_factory(self, username="peter", email="peter@example.com", password="123"):
        user = User(username=username, email=email, password=password)
        user.save()
        return user


class ResetPasswordAPITest(BaseAPITest):
    def test_request_password_with_no_settings(self):
        # make sure that if no setting, the default password request reset field is the email.
        user = self.user_factory()
        data = {"email": user.username}
        response = self.client.post(reverse("reset-password-request"), data=data)
        self.assertEqual(response.status_code, 400)

        data = {"email": user.email}
        response = self.client.post(reverse("reset-password-request"), data=data)
        self.assertEqual(response.status_code, 200)
        msg = "A password reset token has been sent to the provided email address"
        self.assertEqual(response.data["message"], msg)

    def test_request_password_with_django_rest_lookup_field_setting(self):
        # Make sure we can still use DJANGO_REST_LOOKUP_FIELD  setting for backward compatibility.
        settings.DJANGO_REST_LOOKUP_FIELD = "username"
        user = self.user_factory()
        data = {"email": user.username}
        response = self.client.post(reverse("reset-password-request"), data=data)
        self.assertEqual(response.status_code, 200)
        msg = "A password reset token has been sent to the provided email address"
        self.assertEqual(response.data["message"], msg)

    def test_request_password_with_django_rest_lookup_fields_setting(self):
        # Make sure new users can use  DJANGO_REST_LOOKUP_FIELDS  setting.
        settings.DJANGO_REST_LOOKUP_FIELDS = ["email", "username"]
        user = self.user_factory()
        data = {"email": user.username}
        response = self.client.post(reverse("reset-password-request"), data=data)
        self.assertEqual(response.status_code, 200)
        msg = "A password reset token has been sent to the provided email address"
        self.assertEqual(response.data["message"], msg)

        data = {"email": user.email}
        response = self.client.post(reverse("reset-password-request"), data=data)
        self.assertEqual(response.status_code, 200)
        msg = "A password reset token has been sent to the provided email address"
        self.assertEqual(response.data["message"], msg)
