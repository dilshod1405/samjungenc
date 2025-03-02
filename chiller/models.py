from django.db import models


class Chiller(models.Model):
    company_name = models.CharField(max_length=100)
    charasteristic = models.FileField(upload_to='media/chillers/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Chiller"
        verbose_name_plural = "Chillers"


class ChillerImage(models.Model):
    chiller = models.ForeignKey(Chiller, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/chillers/')

    def __str__(self):
        return self.chiller