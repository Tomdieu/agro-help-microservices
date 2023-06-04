from django.dispatch import receiver
from django.db.models.signals import post_save,pre_delete

from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token

from .producer import publish

from .api.serializers import AdminSerializer

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_token(sender, created, instance, **kwargs):
    if created:
        Token.objects.create(user=instance)
        data = {
        'user':AdminSerializer(instance).data,
        'token':instance.auth_token.key
        }
        publish('user_created',data)
    else:
        data = {
        'user':AdminSerializer(instance).data,
        'token':instance.auth_token.key
        }
        publish('user_updated',data)

@receiver(pre_delete, sender=User)
def pre_delete_handler(sender, instance, **kwargs):
    # Perform actions before the deletion of the object
    # Access the instance being deleted using the `instance` parameter
    print("Object is being deleted:", instance)
    # ...
    publish('user_deleted',AdminSerializer(instance).data)



