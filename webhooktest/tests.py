from django.test import TestCase
from webhooktest.models import Transaction, CryptoHook
# Create your tests here.
from django.contrib.auth.models import User
from rest_hooks.models import Hook
jrrtolkien = User.objects.create(username='jrrtoasdfabfacqasw')

transaction = Transaction(
                address='bitaddress6',
                amount=120)


hook = CryptoHook(user=jrrtolkien,
                event='transaction.added',
                target='http://131283e6bf6a.ngrok.io/webhook/',crypto_address="17A16QmavnUfCW11DAApiJxp7ARnxN5pGX")
hook.save()     # creates the hook and stores it for later...



transaction.save()     # fires off 'bookstore.Book.created' hook automatically


hook = CryptoHook(user=jrrtolkien,
                 event='transaction.added',
                 target='http://127.0.0.1/webhook/',crypto_address="bitaddress6")
