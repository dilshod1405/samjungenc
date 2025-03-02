from django.db import models

class DocType(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField()
    
    class Meta:
        verbose_name = "Document Type"
        verbose_name_plural = "Document Types"
    
    def __str__(self):
        return self.name

class DocApp(models.Model):
    name = models.ForeignKey(DocType, on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=False, blank=False)
    
    class Meta:
        verbose_name = "Document Application"
        verbose_name_plural = "Document Applications"
    
    def __str__(self):
        return f'{self.name} - {self.user}'