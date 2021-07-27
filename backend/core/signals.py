import json
from django.db.models.signals import post_save
from django.dispatch import receiver


from core.models import Customer
from core.service import Producer


@receiver(post_save, sender=Customer)
def task_customer_create(sender, instance, **kwargs):
    """при сохранении модели Customer срабатывает receiver"""
    print("Customer создан")
    msg = {
        "seller": {"email": "test"},
        "customer": {
            "name": instance.name,
            "email": instance.email,
            "telephone": instance.telephone,
        },
    }
    task = Producer()
    task.publish(json.dumps(msg))
    task.close()
