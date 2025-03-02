from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.is_canceled == True:
            self.is_done = False
        if self.is_done == True:
            self.is_canceled = False
        super().save(*args, **kwargs)