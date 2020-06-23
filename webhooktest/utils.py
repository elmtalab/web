from .models import CryptoHook, Transaction


def find_and_fire_hook(event_name, instance, **kwargs):
    # filters = {
    #     'event': event_name,
    #     'book_pages': 123
    # }
    transaction = Transaction.objects.latest('id')
    hooks = CryptoHook.objects.filter(event=event_name, crypto_address=transaction.address)
    for hook in hooks:
        print(f"the hook has been sent to {hook.user} to address {hook.target} and {hook.crypto_address}" )
        hook.deliver_hook(instance)
