from django.db import models

class todo(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    exp = models.PositiveBigIntegerField(default = 0)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title
