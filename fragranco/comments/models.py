from django.db import models


class Comments(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    # author = 
    photo = models.ImageField(
        upload_to='comments/',
        blank=True,
        null=True
    )
    # rating = models.SmallIntegerField()