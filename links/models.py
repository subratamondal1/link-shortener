from django.db import models
from django.utils.text import slugify

# Create your models here.
# Save a shortened link => name, url, slug, no. of clicks.
class Link(models.Model):
    # 'id' field is created by default and starts auto-increment from 1
    name = models.CharField(max_length=50, unique=True) 
    url = models.URLField(max_length=200) # the original long url
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.name} | Clicks {self.clicks}"
    
    def click(self):
        self.clicks += 1
        self.save() # Save the current instance

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(value=self.name)
        return super().save(*args, **kwargs)