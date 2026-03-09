'''
1 Standard Library : 없음
2 Third-party: django 
3 Local application : 없음
'''
# 2. django
from django.db import models
from django.utils import timezone

class todo(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    exp = models.PositiveBigIntegerField(default = 0)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    img = models.ImageField(upload_to='todo_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    #*에는 list가 들어오고 **kwargs는 딕셔너리 값이 들어오는데 뭐가 들어오길래 다 필요한거지?
    def save(self, *args, **kwargs):
        if self.complete and self.completed_at is None:
            self.completed_at = timezone.now()
        
        if not self.complete and self.completed_at is not None:
            self.completed_at = None
        
        super().save(*args, **kwargs)
