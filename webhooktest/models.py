# Create your models here.

from django.db import models


class Transaction(models.Model):
    # NOTE: it is important to have a user property
    # as we use it to help find and trigger each Hook
    # which is specific to users. If you want a Hook to
    # be triggered for all users, add '+' to built-in Hooks
    # or pass user_override=False for custom_hook events
    # maybe user is off a related object, so try...
    # user = property(lambda self: self.intermediary.user)

    address = models.CharField(max_length=128)
    amount = models.PositiveIntegerField()

    # ... other fields here ...

    # def serialize_hook(self, hook):
    #     # optional, there are serialization defaults
    #     # we recommend always sending the Hook
    #     # metadata along for the ride as well
    #     return {
    #         'hook': hook.dict(),
    #         'data': {
    #             'id': self.id,
    #             'title': self.title,
    #             'pages': self.pages,
    #             'fiction': self.fiction,
    #             # ... other fields here ...
    #         }
    #     }


from rest_hooks.models import AbstractHook


class CryptoHook(AbstractHook):
    crypto_address = models.CharField(max_length=30, unique=True)


