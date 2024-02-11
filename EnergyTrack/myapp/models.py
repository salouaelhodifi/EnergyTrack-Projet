from django.db import models

# Create your models here.


# Create your models here.
from django.db import models

# Create your models here.
# models.py

from django.db import models

class EMail(models.Model):
    mail = models.EmailField(unique=True)

    def __str__(self):
        return self.mail



