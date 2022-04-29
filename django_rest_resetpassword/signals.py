import django.dispatch

__all__ = [
    'reset_password_token_created',
    'pre_password_reset',
    'post_password_reset',
]

reset_password_token_created = django.dispatch.Signal()

pre_password_reset = django.dispatch.Signal()

post_password_reset = django.dispatch.Signal()
