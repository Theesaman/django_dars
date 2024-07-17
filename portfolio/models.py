from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin, HitCount

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    img = models.ImageField(upload_to='Portfolio/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    now_date=models.DateField(auto_now=True)
    title=models.CharField(max_length=70)
    url = models.URLField()
    
    def __str__(self):
        return self.title


class Team(models.Model):
    img=models.ImageField(upload_to='Team/images')
    description=models.TextField()
    full_name=models.CharField(max_length=50)
    job=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.full_name} by {self.job}"

class Blog(models.Model, HitCountMixin):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Blogs/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)
    content = RichTextField()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"
