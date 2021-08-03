from django.contrib.auth.models import User

class Seller(User):
    class Meta:
        proxy = True

    def __repr__(self):
        return "Seller({self.username}, {self.email})".format(self=self)

    def __str__(self):
        return  self.__repr__()
