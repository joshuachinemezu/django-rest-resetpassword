""" URL Configuration for core auth
"""
from django.urls import re_path

from django_rest_resetpassword.views import reset_password_request_token, reset_password_confirm, reset_password_validate_token

app_name = 'reset_password'

urlpatterns = [
    re_path(r'^validate_token/', reset_password_validate_token, name="reset-password-validate"),
    re_path(r'^confirm/', reset_password_confirm, name="reset-password-confirm"),
    re_path(r'^', reset_password_request_token, name="reset-password-request"),
]
