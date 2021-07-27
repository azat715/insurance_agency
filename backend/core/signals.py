from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Customer

@receiver(post_save, sender=Customer)
def task_customer_create(sender, instance, **kwargs):
    print("Customer создан")
    print(instance.name)
    print(instance.email)
    print(instance.telephone)



