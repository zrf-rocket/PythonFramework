from django.db import models
from django.db.models import F, Index, Value
from django.db.models.functions import Lower, Upper

class IndexModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    height = models.IntegerField()
    weight = models.IntegerField()
    class Meta:
        indexes = [
            Index(
                Lower('first_name'),
                Upper('last_name').desc(),
                name="first_last_name_idx",
            ),
            Index(
                F('height') / (F('weight') + Value(5)),
                name='calc_ids',
            ),
        ]