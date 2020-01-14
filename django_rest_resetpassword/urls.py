""" URL Configuration for core auth
"""
from django.conf.urls import url

from django_rest_resetpassword.views import reset_password_request_token, reset_password_confirm, reset_password_validate_token

app_name = 'reset_password'

urlpatterns = [
    url(r'^validate_token/', reset_password_validate_token, name="reset-password-validate"),
    url(r'^confirm/', reset_password_confirm, name="reset-password-confirm"),
    url(r'^', reset_password_request_token, name="reset-password-request"),
]
