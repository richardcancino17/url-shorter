from django.db import models


class UrlShorter(models.Model):
    link_original = models.URLField()
    code_shorter = models.CharField(max_length=10, null=True)
    times_used = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Url shorter"
        verbose_name_plural = "Url's shorter"

    def __str__(self):
        return self.link_original
