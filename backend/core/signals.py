import json
from django.db.models.signals import post_save
from django.dispatch import receiver


from core.models import Customer, Seller
from core.service import Producer


@receiver(post_save, sender=Customer)
def task_customer_create(sender, instance, **kwargs):
    """при сохранении модели Customer срабатывает receiver"""

    product = instance.product
    seller = Seller.objects.get(products__id=product.id)
    msg = {
        "seller": {"email": seller.email},
        "product": {"name": product.name},
        "customer": {
            "name": instance.name,
            "email": instance.email,
            "telephone": instance.telephone,
        },
    }
    task = Producer()
    task.publish(json.dumps(msg))
    task.close()
