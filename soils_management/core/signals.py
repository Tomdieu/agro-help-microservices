from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Soil

from .serializers import _SoilSerializer


@receiver(post_save, sender=Soil)
def notify_culture_service(sender, instance, created, **kwargs):
    try:
        from .producer import publish

        data = _SoilSerializer(instance).data

        if created:
            message = {"type": "soil_created", "data": data}
            publish("soil_created", message)
        else:
            message = {"type": "soil_updated", "data": data}
            publish("soil_updated", message)
    except:
        pass