from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from users import models as users_models
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50, default='')
    user = models.ForeignKey(users_models.BaseUser, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    date_of_creation = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)


class Task(models.Model):
    name = models.CharField(max_length=50, default='')
    user = models.ForeignKey(users_models.BaseUser, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='tasks')
    start_time = models.DateTimeField()
    deadline = models.DateTimeField()

    class Meta:
        ordering = ('start_time', 'deadline', 'date_of_creation', )
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Task, self).save(*args, **kwargs)