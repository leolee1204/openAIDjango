from django.db import models

class OpenAI_Photo(models.Model):
    id = models.AutoField(primary_key=True)
    describe = models.CharField(max_length=255, null=True)
    file_name = models.CharField(max_length=255, null=True)
    file_path = models.FileField(upload_to='artAI/', null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    deleted_at = models.DateTimeField(null=True)