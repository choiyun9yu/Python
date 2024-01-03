from django.db import models
from .validators import validate_no_hash, validate_no_number, validate_no_above10

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100, validators=[validate_no_hash])
    content = models.TextField(validators=[validate_no_hash])
    feeling = models.CharField(max_length=80, validators=[validate_no_number])
    score = models.IntegerField(validators=[validate_no_above10])
    dt_created = models.DateField()
    # dt_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title